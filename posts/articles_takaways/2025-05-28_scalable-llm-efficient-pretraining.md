---
title: "Scalable, Parameter- and Memory-Efficient Pretraining for Large Language Models"
subtitle: "Recent Algorithmic Advances and Comprehensive Benchmarking"
date: "2025-05-28"
---

**Authors: ** A. Glentis et al.<br>
**Published on Arxiv: ** 2025-05-28<br>
**Link: ** <http://arxiv.org/abs/2505.22922v1><br>
**Institutions:** University of Minnesota • Peking University • University of Sydney<br>
**Keywords:** large language models, parameter-efficient pre-training, memory-efficient optimization, low-rank factorization, weight refactorization, momentum reset, GaLore, Fira, SLTrain, LLaMA, LoRA, C4 dataset, scaling laws, AdamW, model compression, benchmarking

<!-- Change the folliwng id_value randomly between 1 and 1000 to get different random images. -->
<img src="https://picsum.photos/id/487/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

The exponential growth in the scale of large language models (LLMs), now reaching trillions of parameters, is driving significant challenges for both computation and memory, especially during pre-training and fine-tuning phases. Techniques for parameter-efficient fine-tuning like LoRA have succeeded in downstream tasks, but applying such efficiency methods directly to LLM pre-training remains difficult due to scale and data requirements.

<!-- Write a sentence to link to previous part and introduce the following part:  proposed solution, approach, main contributions, etc present all of them in bullet format.  -->

To address these issues, the authors conducted an in-depth examination of current strategies and proposed new practical improvements:

- Comprehensive review of state-of-the-art parameter- and memory-efficient pre-training methods, focusing on those evaluated for LLM pre-training.
- Benchmarking leading memory-efficient pre-training approaches, including memory-efficient optimizers (GaLore, Fira) and weight factorization (Low-rank, LoRA, SLTrain) across various LLaMA model sizes (60M to 1B parameters) using the C4 dataset.
- Rigorous optimization technique comparison using hyperparameter sweeps, and best practices like momentum reset and adaptive gradient clipping to ensure fair baselines.
- Introduction of two practical innovations: weight refactorization (periodic SVD updates of factorized weights), and momentum reset (periodically zeroing optimizer momentum in AdamW), to boost the efficiency and performance of low-rank/SLTrain methods.

<!-- Write a sentence to link to previous part introduce the following part: Results and present them in bullet format -->

Building on these approaches, their benchmarking uncovered several notable findings:

- Full-rank models remain highest-performing when optimally trained.
- Plain low-rank factorization yields surprisingly competitive perplexity for small models, with performance degrading for larger models but never entirely failing as previously thought.
- Restoring full-rankness in factorization- or optimizer-based methods (SLTrain, Fira) substantially reduces the performance gap compared to full-rank models.
- The newly introduced weight refactorization and momentum reset techniques further improved low-rank/SLTrain models, approaching performance of leading memory-efficient optimizers (e.g., for Llama 1B: SLTrain-restarts achieved 14.37 perplexity vs. 13.97 for full-rank, saving ~25% memory).
- Scaling law analysis reveals that final perplexity depends primarily on the total computation (FLOPs) rather than on specific model configuration.

<!-- Write a sentence to link to the previous part present the following part: Conclusions, then prensent them as a bullet format  -->

These results lead to several important conclusions and directions for future work:

- Well-designed and well-tuned efficient pre-training methods can reach performance close to full-model training, though a minor gap persists for the largest models.
- Practical techniques like weight refactorization and momentum reset play a critical role in narrowing this gap.
- Future research aims to extend benchmarking across more models and datasets, and to develop further efficient pre-training techniques.
