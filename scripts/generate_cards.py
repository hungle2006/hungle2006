#!/usr/bin/env python3
import os, json, html, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "profile" / "cards"
OUT.mkdir(parents=True, exist_ok=True)

repos = json.loads((ROOT / "scripts" / "repos.json").read_text(encoding="utf-8"))
TOKEN = os.getenv("GITHUB_TOKEN", "")
OWNER = "hungle2006"

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

def api_get(repo):
    url = f"https://api.github.com/repos/{OWNER}/{repo}"
    headers = {"Accept":"application/vnd.github+json","User-Agent":"github-profile-card-generator"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)

def wrap_text(text, max_chars):
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = word if not current else current + " " + word
        if len(test) <= max_chars:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

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

for item in repos:
    try:
        meta = api_get(item["name"])
    except Exception as e:
        print(f"Warning: {item['name']}: {e}")
        meta = {"language":"Code","stargazers_count":0,"forks_count":0}
    path = OUT / f"{safe_name(item['name'])}.svg"
    path.write_text(make_svg(item, meta), encoding="utf-8")
    print("generated", path)
