---
title: "Leveraging Large Language Models for Bengali Math Word Problem Solving"
subtitle: "Advancing Multistep Reasoning with Chain-of-Thought and Efficient Fine-Tuning"
date: "2025-05-27"
---

**Authors:** B. Paul et al.<br>
**Published on Arxiv:** 2025-05-27<br>
**Link:** <http://arxiv.org/abs/2505.21354v1><br>
**Institutions:** Ahsanullah University of Science and Technology, Tejgaon, Dhaka<br>
**Keywords:** Natural Language Processing, Chain of Thought, Low-Resource Language, Large Language Models, LoRA, Math Word Problems, Bengali, Fine-tuning, Few-shot Learning, Prompt Engineering, Reasoning, Educational Technology<br>

<!-- Change the folliwng seed_value randomly between 1 and 1000000 to get different random images. -->
<img src="https://picsum.photos/seed/571032/300/200" alt="Random Unsplash-style image"  style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em;">

<!-- Context -->

Solving Math Word Problems (MWPs) in Bengali poses unique challenges in natural language processing, given Bengali's status as a low-resource language requiring complex reasoning. Existing resources often lack reasoning-focused annotations, limiting progress in AI models for mathematical problem-solving. While Chain-of-Thought (CoT) prompting has shown improvements in high-resource languages, systematic exploration for Bengali MWPs is lacking.

Building on these needs, the authors propose a comprehensive solution and present several main contributions:

- Introduction of SOMADHAN, a manually curated dataset containing 8,792 complex Bengali MWPs with detailed step-by-step (CoT) solutions.
- Evaluation of various large language models (GPT-4o, GPT-3.5 Turbo, LLaMA-3, Deepseek, Qwen) on zero-shot and few-shot tasks, with and without CoT reasoning.
- Adaptation of prompting techniques and system instructions for CoT, alongside experimentation with multiple prompt styles.
- Application of LoRA (Low-Rank Adaptation) for efficient fine-tuning of large models on the Bengali MWP task.

After presenting their methodological advances, the authors detail their experimental results:

- CoT prompting consistently enhanced accuracy across all tested large language models on complex MWPs in Bengali.
- LLaMA-3.3 70B achieved the best result, with 88% accuracy in few-shot CoT prompting on SOMADHAN.
- GPT-4o attained a strong 83% accuracy under the same settings.
- LoRA fine-tuning allowed efficient, memory-friendly adaptation, achieving up to 17% accuracy improvement on a subset of the dataset with minimal computational cost.
- Fine-tuned GPT-3.5 did not surpass GPT-4o's zero-shot performance, demonstrating the importance of intrinsic model capabilities over fine-tuning alone.

Drawing their conclusions from these results, the article highlights future directions and the impact of their contributions:

- SOMADHAN fills a critical resource gap by providing a high-quality, step-annotated Bengali MWP dataset.
- Chain-of-Thought prompting demonstrably strengthens the reasoning abilities of large models for Bengali MWPs, notably for cutting-edge architectures.
- LoRA presents an effective pathway for resource-efficient fine-tuning in low-resource language settings.
- Future work will extend the dataset, refine fine-tuning methodologies, and enhance output alignment for multilingual models.
