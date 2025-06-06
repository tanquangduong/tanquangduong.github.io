---
title: "Do We Know What LLMs Don't Know? Consistency in Knowledge Probing"
subtitle: "Evaluating the Robustness and Reliability of Knowledge Gap Probes in Large Language Models"
date: "2025-05-27"
---

**Authors:** R. Zhao et al.<br>
**Published on Arxiv:** 2025-05-27<br>
**Link:** <http://arxiv.org/abs/2505.21701v2><br>
**Institutions:** LMU Munich • Munich Center for Machine Learning (MCML)<br>
**Keywords:** large language models, knowledge probing, model consistency, knowledge gaps, hallucinations, abstention, prompt sensitivity, robustness, MMLU, Hellaswag, calibration, self-consistency, decision metrics<br>

<img src="https://picsum.photos/id/487/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

Large language models (LLMs) have become widely used but suffer from hallucinations—generating fluent yet incorrect outputs. Identifying areas where LLMs lack knowledge is critical for building trust and reliability in their applications. While various knowledge probing methods exist, little is known about the robustness and reliability of these methods themselves.

<!-- Approach and contributions -->

To address this gap, the authors propose a new framework and set of metrics for systematically studying the consistency of knowledge probing methods in LLMs. Their main approach and contributions include:

- Distinguishing between intra-method consistency (stability of a method under small prompt changes) and cross-method consistency (agreement between different probes on the same prompt and model).
- Designing and evaluating prompt variants (e.g., spacing, typos, shuffled answer options, one-shot prompts) to test probe robustness under real-world perturbations.
- Comparing six representative probing methods across four main categories (calibration, embedding/training, prompting, consistency/NOTA) on several popular LLMs (such as Mistral, LLaMA-3, OLMo) using standard datasets (MMLU, Hellaswag).
- Introducing new consistency metrics to quantify probe agreement across conditions and variants.

<!-- Results -->

Their experiments yield important empirical findings:

- Even minimal surface-level prompt changes can lead to drastic drops in intra-method consistency (intersection-over-union (IoU) scores as low as 0.04).
- Cross-method consistency is even weaker, with probe decision agreement dropping below 7% in some cases.
- Larger models do not consistently provide more reliable or robust probing outcomes (e.g., LLaMA-3 70B doesn't always outperform smaller versions).
- Widely used metrics such as Abstain F1 can be deceptive: overall scores may remain stable while the underlying individual decisions swing dramatically across prompt variants.
- Calibration-based probing methods are highly sensitive to thresholding strategies, leading to instability that must be addressed via careful correction.

<!-- Conclusions -->

Building on these results, the authors draw several key conclusions:

- Existing knowledge probes for LLMs show marked inconsistency both within methods (under minor prompt changes) and across different probing methods (on the same test cases).
- This inconsistency challenges the trustworthiness of current frameworks for knowledge gap detection and abstention, which are essential for safe LLM usage.
- Consistency metrics should become a standard element of probe evaluation, and efforts to develop more robust probing strategies are urgently needed.
