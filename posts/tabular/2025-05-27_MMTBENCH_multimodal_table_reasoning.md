---
title: "MMTBENCH: A Unified Benchmark for Complex Multimodal Table Reasoning"
subtitle: "Advancing Evaluation of Vision–Language Models with Real-World Multimodal Tables"
date: "2025-05-27"
---

**Authors:** P. Y. Titiya et al.<br>
**Published on Arxiv:** 2025-05-27<br>
**Link:** <http://arxiv.org/abs/2505.21771v1><br>
**Institutions:** Arizona State University<br>
**Keywords:** multimodal tables, question answering, vision-language models, large language models, benchmark dataset, table reasoning, visual reasoning, machine learning evaluation, real-world data, image-text integration<br>

<img src="https://picsum.photos/id/327/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

Multimodal tables—combining structured data with visual elements like charts and maps—are increasingly prevalent in real-world domains, yet they pose ongoing challenges for current Vision–Language Models (VLMs) and Large Language Models (LLMs). Existing research has largely concentrated on text-only tables, leaving complex multimodal table reasoning underexplored and lacking robust benchmarks that reflect real-world complexity.

To address these gaps and introduce a comprehensive evaluation tool, the authors propose an innovative approach rooted in the following main contributions:

- Introduction of MMTBENCH, a benchmark dataset compiled from 500 real-world multimodal tables, annotated with 4,021 diverse question–answer pairs.
- Coverage of eight multimodal table types with integrated visual elements, including charts, maps, images, and hierarchical structures.
- Questions designed to span mathematical, logical, fact-verification, and visual reasoning, capturing both direct and multi-step inference needs.
- Systematic benchmarking of state-of-the-art open and closed-source models (e.g., Google Gemini, GPT-4o Mini, LLaMA 3, Mixtral-8x7B), across five experimental baselines reflecting different accesses to textual and visual information.

Building on this approach, the authors report empirical results that highlight current model capabilities and limitations:

- Substantial performance gaps are observed, particularly for questions requiring advanced visual-based reasoning and multi-step inference.
- The Entity Replaced Baseline—where tables are fully textualized—yields the highest model performance, while the Missing Image and Image Captioning baselines lag behind significantly.
- Closed-source models generally lead in vision-based tasks, but select open-source models (for instance, Qwen 2.5 VL-7b-Instruct) demonstrate competitive results in some settings.
- All models show notable struggles with complex, implicit visual reasoning and tasks requiring image interpretation within tables.
- Human evaluators consistently outperform AI models but still encounter challenges, especially with subtle visual cues and domain-specific knowledge demands.

Reflecting on these findings, the article draws significant conclusions and outlines future directions for the field:

- MMTBENCH provides a rigorous new benchmark, exposing the substantial limitations of current LLMs and VLMs in multimodal table reasoning.
- There exists a critical research gap in achieving deep visual–textual integration for practical multimodal data analysis.
- The benchmark's complexity and scope open new avenues of model development and evaluation, underlining the need for improved architectures.
- Future work includes dataset expansion and testing of larger models, while also acknowledging potential societal risks stemming from model misinterpretation in real-world applications.
