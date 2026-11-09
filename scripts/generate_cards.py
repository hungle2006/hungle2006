#!/usr/bin/env python3
"""Keep the profile README and SVG project cards in sync with public GitHub repositories."""
import html
import json
import os
import textwrap
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "profile" / "cards"
OWNER = "hungle2006"
TOKEN = os.getenv("GITHUB_TOKEN", "")
OUT.mkdir(parents=True, exist_ok=True)

# Curated copy is optional: every public repository is discovered independently.
CURATED = {
    item["name"].casefold(): item
    for item in json.loads((ROOT / "scripts" / "repos.json").read_text(encoding="utf-8"))
}

PALETTE = {
    "Medical AI": ("#ff3d81", "#141322"),
    "Clinical NLP": ("#00d8b4", "#101d1d"),
    "Computer Vision": ("#40a9ff", "#122033"),
    "3D Vision": ("#a78bfa", "#1e1733"),
    "NLP": ("#ff6b7d", "#25131c"),
    "LLM Systems": ("#f6c344", "#251f10"),
    "Reasoning / AGI": ("#d56cff", "#24142d"),
    "Autonomous Driving": ("#20d6ea", "#10252a"),
}

def list_public_repositories():
    """Fetch ALL pages, never silently shrink the profile if GitHub API fails."""
    repos = []
    page = 1
    while True:
        url = (
            f"https://api.github.com/users/{OWNER}/repos"
            f"?type=owner&sort=pushed&direction=desc&per_page=100&page={page}"
        )
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "hungle2006-profile-sync",
        }
        if TOKEN:
            headers["Authorization"] = f"Bearer {TOKEN}"
        with urlopen(Request(url, headers=headers), timeout=30) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise RuntimeError("GitHub repository API did not return a list")
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    public = [
        r for r in repos
        if (not r.get("private")) and r.get("name", "").casefold() != OWNER.casefold()
    ]
    public.sort(
        key=lambda r: (
            r.get("pushed_at") or r.get("created_at") or "",
            r.get("created_at") or "",
            r.get("name", "").casefold(),
        ),
        reverse=True,
    )
    return public


def wrap_text(value, max_chars):
    return textwrap.wrap(str(value).replace("\n", " "), width=max_chars,
                         break_long_words=True, break_on_hyphens=True)


def safe_name(name):
    return "".join(c.lower() if c.isalnum() else "-" for c in name).strip("-")

def make_svg(item, meta):
    name = item["name"]
    desc = item["desc"]
    cat = item["category"]
    accent, bg2 = PALETTE.get(cat, ("#58a6ff", "#161b22"))
    language = meta.get("language") or "Code"
    stars = meta.get("stargazers_count", 0)
    forks = meta.get("forks_count", 0)

    name_lines = wrap_text(name, 34)[:2]
    desc_lines = wrap_text(desc, 58)[:2]

    title_nodes = []
    base_y = 48
    for i, line in enumerate(name_lines):
        title_nodes.append(
            f'<text x="58" y="{base_y + i*27}" font-size="21" font-weight="700" fill="{accent}">{html.escape(line)}</text>'
        )

    desc_nodes = []
    desc_y = 105 if len(name_lines) == 1 else 122
    for i, line in enumerate(desc_lines):
        desc_nodes.append(
            f'<text x="30" y="{desc_y + i*21}" font-size="14" fill="#d5e7ff">{html.escape(line)}</text>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="520" height="170" viewBox="0 0 520 170">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#11111d"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
  </defs>

  <rect x="1" y="1" width="518" height="168" rx="7" fill="url(#bg)" stroke="#b7beca" stroke-width="1.2"/>

  <g transform="translate(30,31)">
    <path d="M2 2h14v17H2z" fill="none" stroke="{accent}" stroke-width="2"/>
    <path d="M5 19v4m8-4v4" stroke="{accent}" stroke-width="2" stroke-linecap="round"/>
  </g>

  {''.join(title_nodes)}
  {''.join(desc_nodes)}

  <circle cx="38" cy="145" r="7" fill="#3b8bc2"/>
  <text x="56" y="151" font-size="15" fill="{accent}">{html.escape(str(language))}</text>

  <g transform="translate(180,135)" stroke="{accent}" stroke-width="1.8" fill="none">
    <path d="M10 1l2.7 5.5 6.1.9-4.4 4.2 1 6-5.4-2.9-5.4 2.9 1-6L1.2 7.4l6.1-.9z"/>
  </g>
  <text x="205" y="151" font-size="15" fill="#d5e7ff">{stars}</text>

  <g transform="translate(270,136)" stroke="{accent}" stroke-width="1.8" fill="none">
    <circle cx="4" cy="3" r="2.3"/>
    <circle cx="4" cy="15" r="2.3"/>
    <circle cx="16" cy="6" r="2.3"/>
    <path d="M4 5.5v7M6 4h4c4 0 6 1 6 4"/>
  </g>
  <text x="298" y="151" font-size="15" fill="#d5e7ff">{forks}</text>

  <text x="435" y="151" font-size="12" fill="#8b9bb0">OPEN</text>
</svg>"""

START_MARKER = "<!-- AUTO-REPOS:START -->"
END_MARKER = "<!-- AUTO-REPOS:END -->"


def refresh_readme(repos):
    readme_path = ROOT / "README.md"
    current = readme_path.read_text(encoding="utf-8")
    rows = [
        f"**{len(repos)} public repositories**, automatically discovered and ordered by recent code activity.",
        "",
        "<table>",
    ]
    for index in range(0, len(repos), 2):
        rows.append("  <tr>")
        for repo in repos[index:index + 2]:
            name = repo["name"]
            url = f"https://github.com/{OWNER}/{quote(name)}"
            svg = f"./profile/cards/{safe_name(name)}.svg"
            rows.extend([
                '    <td width="50%" valign="top">',
                f'      <a href="{html.escape(url, quote=True)}">',
                f'        <img src="{html.escape(svg, quote=True)}" width="100%" alt="{html.escape(name, quote=True)}" />',
                '      </a>',
                '    </td>',
            ])
        if index + 1 == len(repos):
            rows.append('    <td width="50%"></td>')
        rows.append("  </tr>")
    rows.append("</table>")
    block = START_MARKER + "\n" + "\n".join(rows) + "\n" + END_MARKER

    if START_MARKER in current and END_MARKER in current:
        start = current.index(START_MARKER)
        end = current.index(END_MARKER) + len(END_MARKER)
        updated = current[:start] + block + current[end:]
    else:
        heading = "## 🚀 My Repositories"
        footer = '\n---\n\n<div align="center">'
        start = current.find(heading)
        end = current.find(footer, start)
        if start < 0 or end < 0:
            raise RuntimeError("README.md is missing the expected project section; refusing to overwrite it.")
        introduction = (
            heading + "\n\n"
            "> Public projects are added automatically when created; cards, language, stars, forks "
            "and ordering refresh on the scheduled GitHub Action.\n\n"
        )
        updated = current[:start] + introduction + block + "\n" + current[end:]
    if updated != current:
        readme_path.write_text(updated, encoding="utf-8")
        print(f"README.md updated with {len(repos)} repositories")
    else:
        print("README.md unchanged")


def main():
    repos = list_public_repositories()
    if not repos:
        raise RuntimeError("No public repositories returned; refusing to delete cards")
    expected = set()
    for meta in repos:
        name = meta["name"]
        custom = CURATED.get(name.casefold(), {})
        item = {
            "name": name,
            "desc": custom.get("desc") or meta.get("description")
                    or "Explore this repository's source code, documentation and updates.",
            "category": custom.get("category") or "Other Projects",
        }
        filename = f"{safe_name(name)}.svg"
        if filename in expected:
            raise RuntimeError(f"Card filename collision: {filename}")
        expected.add(filename)
        svg = make_svg(item, meta)
        path = OUT / filename
        if not path.exists() or path.read_text(encoding="utf-8") != svg:
            path.write_text(svg, encoding="utf-8")
            print(f"updated {filename}")
    refresh_readme(repos)
    for path in OUT.glob("*.svg"):
        if path.name not in expected:
            path.unlink()
            print(f"removed stale card {path.name}")
    print(f"Profile synchronized: {len(repos)} public repositories.")


if __name__ == "__main__":
    main()
