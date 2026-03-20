---
title: "Towards Fully FP8 GEMM LLM Training at Scale"
subtitle: "Introducing FOG Architectures for Efficient and Stable Low-Precision Transformer Training"
date: "2025-05-26"
---

**Authors: ** A. Hernández-Cano et al.<br>
**Published on Arxiv: ** 2025-05-26<br>
**Link: ** http://arxiv.org/abs/2505.20524v1<br>
**Institutions:** EPFL • ETHZ<br>
**Keywords:** FP8, GEMM, Large Language Models, LLM training, Transformers, FP8DPA, FOG architecture, Delayed scaling, Kurtosis, Outlier mitigation, Deep learning efficiency, Language modeling, Benchmarking, FineWeb-Edu, BF16, Transformer Engine, Megatron-LM

<img src="https://picsum.photos/id/457/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

Efficient training of large language models (LLMs) demands significant computational resources, prompting growing interest in the use of lower-precision numerical formats like FP8 to accelerate training and reduce resource requirements. Recent adoption of FP8, however, has been hampered by training instabilities, largely due to FP8's narrow dynamic range and outlier activations encountered in LLMs. Most existing FP8 training methods limit FP8 application to certain components, relying on higher-precision formats for critical matrix multiplications, particularly in attention mechanisms, which restricts the full potential of throughput gains from FP8.

To address these challenges, the authors present their proposed solution, approach, and the main contributions:

- Introduction of FOG (fast and outlier-guarded) architectures, a set of transformer-based LLM designs that enable stable and efficient FP8 computation for all GEMMs, including those within the attention mechanism.
- Incorporation of architectural modifications such as removal of pre-normalization, inclusion of entropy-regularization in attention using non-trainable RMSNorm or tanh activation, input activation scaling, and post-normalization before residual connections to manage outlier activations and enhance robustness to FP8 precision limitations.
- Utilization of low-overhead delayed scaling for FP8 casting, use of kurtosis as a metric to monitor outlier activations, and application of early diagnostic techniques to predict and counteract training instabilities.
- Experimental comparison involving models of 390M, 1.5B, and 8B parameters trained on the FineWeb-Edu dataset, benchmarking against state-of-the-art baselines such as Llama3, OLMo2, and SmoothSwiGLU, and assessment using standard LLM downstream tasks.

Having defined the approach and innovations, the results of the study are presented as follows:

- FOG architectures enable all GEMMs in the transformer block, including attention, to be performed in FP8, leading to throughput improvements of up to 40% at the 8B parameter scale compared to BF16 baselines, while retaining or surpassing performance on downstream tasks like HellaSwag, ARC, PIQA, and others.
- Stable and robust training is achieved across prolonged token counts (up to 420B tokens for 1.5B models), with FOG significantly outperforming prior architectures that tend to diverge when trained completely with FP8 in attention layers.
- Monitoring with kurtosis effectively forecasts the appearance of outlier activations and alerts to possible divergences earlier than traditional indicators such as loss curves or gradient norms, providing a reliable early-warning system for maintaining stability during FP8 training.
- All FOG model variants match or exceed the accuracy of baseline BF16 models across benchmarks, validating the practicality and efficiency of the proposed approach at scale.

Upon reviewing these results, the study concludes with the following key takeaways:

- This work demonstrates, for the first time, that it is feasible to achieve stable, high-performance LLM training with full FP8 computations, including in attention mechanisms, at scale—showing up to 40% improvement in throughput and equal or superior downstream effectiveness compared to higher-precision baselines.
- The proposed FP8 training framework enables early and reliable prediction of long-term training instabilities using kurtosis analysis, which helps reduce experimental costs and mitigates training risks.
- The approach paves the way for extending full FP8 GEMM training, even in output heads, although future work will need to validate these findings at scales beyond 8B parameters and further explore FP8's role in optimizer state representation and training.
