<div align="center">

# LÊ MINH HÙNG

### AI / ML Engineer · Computer Vision · Deep Learning · AI Systems

<br/>

<a href="https://github.com/hungle2006">
  <img src="https://img.shields.io/badge/GitHub-hungle2006-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>
<a href="https://huggingface.co/leminhhung0101">
  <img src="https://img.shields.io/badge/Hugging%20Face-Models%20%26%20Demos-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
</a>
<a href="mailto:hungle06.01.01@gmail.com">
  <img src="https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

<br/><br/>

> **Building intelligent systems from research ideas to efficient, deployable AI applications.**

<br/>

<img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,cpp,opencv,sklearn,github,docker,linux,git" />

</div>

---

## 🧠 About

I'm **Lê Minh Hùng**, an AI-focused developer working across **deep learning, computer vision, medical AI, 3D vision, NLP, multimodal systems, and efficient AI inference**.

My projects are centered around one idea:

```text
Research
   ↓
Model Design
   ↓
Training
   ↓
Evaluation
   ↓
Optimization
   ↓
Efficient Inference
   ↓
Deployment
```

I enjoy turning research-oriented architectures into systems that are **measurable, optimized, reproducible, and practical**.

### Currently interested in

`Deep Learning` · `Computer Vision` · `Medical AI` · `3D Vision` · `LLM Systems` · `NLP` · `Multimodal AI` · `Model Optimization`

---

# 🧭 AI Portfolio

<div align="center">

| 🧠 Medical AI | 👁️ Computer Vision | 🧊 3D Vision | 🤖 LLM / NLP |
|:---:|:---:|:---:|:---:|
| Brain MRI | Image Retrieval | 3D Gaussian Splatting | LFM Serving |
| Knee MRI | Anomaly Detection | Mip-Splatting | Vietnamese NLP |
| Lung Audio | Feature Matching | Neural View Synthesis | Hate Speech |
| Diabetes AI | Representation Learning | Depth-guided Refinement | Transformer Models |

</div>

---

# ⭐ Featured Projects

## 🧊 01 — 3D Gaussian Splatting & Neural View Synthesis

My main computer-vision research direction focuses on **3D scene reconstruction and novel-view synthesis**.

### `gaussian-splatting-LPIPS-Fine-tuning`

**COLMAP → Depth Anything V2 → 3DGS → Pruning → LPIPS → Quantization**

```text
Images
  │
  ▼
COLMAP
  │
  ├───────────────┐
  │               │
  ▼               ▼
Camera Poses   Depth Anything V2
  │               │
  └───────┬───────┘
          ▼
 Depth-guided Densification
          │
          ▼
      3D Gaussian Splatting
          │
          ▼
   Gaussian Refinement
          │
          ▼
 LPIPS Fine-tuning
          │
          ▼
     Quantization
          │
          ▼
 Novel View Synthesis
```

**Focus**

`COLMAP` `Depth Anything V2` `3DGS` `LPIPS` `Gaussian Pruning` `Quantization` `PSNR` `SSIM`

---

### `Mip-Splatting-Fine-tuning`

A more advanced NVS workflow combining **Mip-Splatting, depth-guided densification, pruning, appearance correction and perceptual fine-tuning**.

```text
COLMAP
   ↓
Depth Estimation
   ↓
Metric Alignment
   ↓
Depth-guided Densification
   ↓
Mip-Splatting
   ↓
Gaussian Pruning
   ↓
Appearance Optimization
   ↓
LPIPS Fine-tuning
   ↓
Quantization
```

**Why it matters**

The project explores the trade-off between:

- visual fidelity
- Gaussian count
- rendering quality
- optimization stability
- model size
- inference efficiency

---

### `OmniGS`

A broader experimental direction around **high-quality Gaussian Splatting and scene reconstruction**, with emphasis on geometric refinement, adaptive optimization and efficient representation.

---

# 🏥 02 — Medical AI

A large part of my portfolio focuses on applying deep learning to **medical imaging and biomedical signals**.

## `BrainModel`

Deep-learning research framework for brain-related AI.

**Core stack**

`PyTorch` · `Computer Vision` · `Neural Networks` · `Model Training` · `Evaluation`

---

## `Gold58-ConvNeXt2.5D`

Study-level **multi-label knee MRI classification**.

### Architecture

```text
MRI Study
   │
   ▼
Protocol-aware Selection
   │
   ▼
Uniform Slice Sampling
   │
   ▼
2.5D Slice Construction
   │
   ▼
ConvNeXtV2
   │
   ▼
Feature Aggregation
   │
   ▼
Multi-label Prediction
```

### Main ideas

- 2.5D MRI representation
- ConvNeXtV2 backbone
- Study-level aggregation
- Multi-label classification
- Fixed validation subset
- Efficient feature extraction

---

## `knee-detection`

A study-level knee MRI system exploring:

`Multi-Instance Learning` · `Transformer Aggregation` · `MRI Feature Caching` · `Study-level Prediction`

The project focuses on converting **multiple MRI slices and series into a single study-level decision**.

---

## `Lung_Multi-taskLearning`

AI pipeline for respiratory sound analysis.

```text
Lung Audio
    │
    ▼
Audio Preprocessing
    │
    ▼
Multi-task CNN
    │
    ├───────────────┐
    ▼               ▼
Crackle/Wheeze   Disease
Detection        Classification
    │               │
    └───────┬───────┘
            ▼
        Explainability
            │
            ▼
          Grad-CAM
```

**Focus**

`Audio AI` · `Multi-task Learning` · `Attention` · `Prototype Learning` · `Grad-CAM`

---

## `Diabetes-AI`

Medical AI system exploring diabetes prediction using:

`Retinal / Eye Data` + `Clinical Information` + `Machine Learning`

---

# 👁️ 03 — Computer Vision

## `Deep-Image-Retrieval-using-DINOv2-OpenCLIP-ConvNeXt-and-LightGlue`

A hybrid image retrieval system combining **global semantic representations with local visual verification**.

```text
                  Query Image
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      DINOv2         OpenCLIP       ConvNeXt
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                 Feature Fusion
                       │
                       ▼
                  Global Top-K
                       │
                       ▼
            ┌──────────┴──────────┐
            ▼                     ▼
         LightGlue             Texture
            │                     │
            └──────────┬──────────┘
                       ▼
                   Re-ranking
                       │
                       ▼
                  Final Results
```

### Representation stack

`DINOv2` · `OpenCLIP` · `ConvNeXt` · `LightGlue` · `Texture Features`

The important idea is to combine **semantic similarity** with **local geometric evidence** instead of relying on a single embedding.

---

## `anomaly_3branch`

Normal-only anomaly detection using three complementary feature branches.

```text
                 Normal Images
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      DINOv2        ConvNeXt      WideResNet50
        │              │              │
        ▼              ▼              ▼
     Global         Hierarchical     Patch-level
     Features        Features        Features
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                 Score Fusion
                       │
                       ▼
                 Anomaly Score
```

**Focus**

`DINOv2` · `ConvNeXt` · `PatchCore` · `Anomaly Detection`

---

# 🇻🇳 04 — Vietnamese NLP

## `VietnameseMulti-scale-CNN`

A character-level Vietnamese language identification model designed for **real-world noisy text**.

### Architecture

```text
Character Input
      │
      ▼
Character Embedding
      │
      ▼
Multi-scale CNN
 ┌────┼────┬────┐
 │    │    │    │
3x3  5x5  7x7  11x11
 └────┼────┴────┘
      ▼
Residual Blocks
      ▼
Squeeze-and-Excitation
      ▼
Transformer Encoder
      ▼
Multi-Head Attention Pooling
      ▼
Angular Margin Loss
      ▼
Temperature Scaling
      ▼
Prediction
```

### Designed for noisy Vietnamese

`Missing Diacritics` · `OCR Errors` · `Typos` · `Slang` · `Emoji` · `URLs` · `Mixed Language`

---

## `R-ViHSDModel`

Vietnamese hate-speech and text-noise classification.

### Strategy

```text
Vietnamese Text
       │
       ├──────────────┐
       ▼              ▼
   ViSoBERT       Character TF-IDF
       │              │
       └──────┬───────┘
              ▼
       Base Predictions
              │
              ▼
       OOF Stacking
              │
              ▼
       Final Classifier
```

**Focus**

`ViSoBERT` · `TF-IDF` · `Linear Models` · `OOF Stacking`

---

# 🤖 05 — LLM Serving & Efficient AI

## `lfm-serving`

A lightweight LLM serving system built around **LFM inference with a public Hugging Face demo**.

### System idea

```text
Request
   │
   ▼
Prompt Processing
   │
   ▼
Inference Engine
   │
   ▼
LFM Model
   │
   ▼
Streaming Response
```

---

## `speedLfmServing`

A more performance-oriented direction for **high-efficiency LFM inference and serving**.

```text
Incoming Requests
       │
       ▼
Prompt Normalization
       │
       ▼
Request Scheduling
       │
       ▼
Resource-aware Admission
       │
       ▼
Efficient LLM Engine
       │
       ▼
LFM Inference
       │
       ▼
Response
```

### Main goals

- Lower inference overhead
- Efficient GPU utilization
- Request scheduling
- Lightweight serving
- Practical deployment

---

# 🚗 06 — Multimodal & Autonomous Systems

## `Traffic_AV`

Multimodal traffic understanding using both **visual and audio information**.

```text
Video ───────────────┐
                     ├──► Feature Extraction
Audio ───────────────┘
                           │
                           ▼
                    CNN / Attention
                           │
                           ▼
                      Transformer
                           │
                           ▼
                   Scene Understanding
```

**Focus**

`Audio-Visual Learning` · `CNN` · `Attention` · `Transformer` · `Traffic AI`

---

# 🧩 Research Map

<div align="center">

```text
                         AI / ML
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
    Medical AI        Computer Vision      NLP / LLM
        │                  │                  │
   ┌────┼────┐        ┌────┼────┐        ┌────┼────┐
   │    │    │        │    │    │        │    │    │
 Brain Knee Lung   Retrieval 3DGS Anomaly ViSoBERT LFM  CNN
   │    │    │        │    │    │        │    │    │
   └────┴────┘        └────┴────┘        └────┴────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                   Efficient AI Systems
                           │
                 ┌─────────┼─────────┐
                 ▼         ▼         ▼
             Fine-tuning  Pruning  Quantization
                 │         │         │
                 └─────────┼─────────┘
                           ▼
                       Deployment
```

</div>

---

# ⚙️ Tech Stack

### Deep Learning

<p>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white"/>
<img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black"/>
<img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>
</p>

### Computer Vision

<p>
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white"/>
<img src="https://img.shields.io/badge/COLMAP-3D%20Vision-black?style=flat-square"/>
<img src="https://img.shields.io/badge/3DGS-Gaussian%20Splatting-purple?style=flat-square"/>
</p>

### LLM / NLP

<p>
<img src="https://img.shields.io/badge/Transformers-FF6F00?style=flat-square"/>
<img src="https://img.shields.io/badge/vLLM-Inference-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/QLoRA-Fine--tuning-green?style=flat-square"/>
<img src="https://img.shields.io/badge/NLP-Vietnamese%20AI-orange?style=flat-square"/>
</p>

### Engineering

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white"/>
<img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"/>
<img src="https://img.shields.io/badge/Git-181717?style=flat-square&logo=git&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
</p>

---

# 📊 GitHub Analytics

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=hungle2006&show_icons=true&theme=tokyonight&hide_border=true&rank_icon=github" />

<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=hungle2006&layout=compact&theme=tokyonight&hide_border=true" />

<br/><br/>

<img src="https://streak-stats.demolab.com?user=hungle2006&theme=tokyonight&hide_border=true" />

</div>

---

# 🏆 What I Like Building

```text
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  🧠 Models that solve real problems                      │
│                                                          │
│  👁️ Vision systems that understand images & 3D scenes   │
│                                                          │
│  🏥 AI systems for healthcare                            │
│                                                          │
│  🤖 Efficient LLM inference                              │
│                                                          │
│  ⚡ Optimized training and deployment                    │
│                                                          │
│  🔬 Research ideas turned into working systems            │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

# 📌 Repository Highlights

| Project | Area | Key Technologies |
|:---|:---|:---|
| **Gold58-ConvNeXt2.5D** | Medical AI | ConvNeXtV2 · MRI · Multi-label |
| **R-ViHSDModel** | NLP | ViSoBERT · TF-IDF · OOF Stacking |
| **knee-detection** | Medical AI | MRI · MIL · Transformer |
| **anomaly_3branch** | Vision | DINOv2 · ConvNeXt · PatchCore |
| **BrainModel** | Medical AI | PyTorch · Deep Learning |
| **speedLfmServing** | LLM Systems | LFM · Serving · Optimization |
| **lfm-serving** | LLM Systems | LFM · Hugging Face · Gradio |
| **VietnameseMulti-scale-CNN** | NLP | CharCNN · Transformer |
| **Mip-Splatting-Fine-tuning** | 3D Vision | Mip-Splatting · LPIPS |
| **OmniGS** | 3D Vision | Gaussian Splatting |
| **Deep-Image-Retrieval** | Vision | DINOv2 · CLIP · LightGlue |
| **gaussian-splatting-LPIPS-Fine-tuning** | 3D Vision | 3DGS · Depth · LPIPS |
| **Traffic_AV** | Multimodal AI | Audio · Vision · Transformer |
| **Lung_Multi-taskLearning** | Medical AI | Audio · Multi-task Learning |
| **Diabetes-AI** | Medical AI | Clinical + Vision |

---

# 🔭 Current Direction

I'm currently pushing my work toward:

**Efficient AI → Better representations → Stronger evaluation → Practical deployment**

Especially interested in:

`3D Vision` · `Medical AI` · `Efficient LLM Serving` · `Multimodal Learning` · `Model Compression` · `AI Systems`

---

<div align="center">

### Let's build something intelligent. 🚀

<br/>

<a href="mailto:hungle06.01.01@gmail.com">
  <img src="https://img.shields.io/badge/Contact%20Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

<a href="https://github.com/hungle2006">
  <img src="https://img.shields.io/badge/Explore%20My%20Repos-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>

<br/><br/>

**Research · Build · Optimize · Deploy**

</div>
