---
title: "From Images to Signals: Are Large Vision Models Useful for Time Series Analysis?"
subtitle: "A Systematic Evaluation of LVMs on Classification and Forecasting Tasks in Time Series"
date: "2025-05-29"
---

**Authors:** Z. Zhao et al.<br>
**Published on Arxiv:** 2025-05-29<br>
**Link:** <http://arxiv.org/abs/2505.24030v1><br>
**Institutions:** University of Houston • University of Illinois at Urbana-Champaign • University of Connecticut • Squirrel Ai Learning<br>
**Keywords:** Large Vision Models, Vision Transformer (ViT), Swin Transformer, Masked Autoencoders (MAE), SimMIM, Time Series Analysis, Time Series Classification, Time Series Forecasting, Imaging methods, Self-supervised learning, Transfer learning, Ablation study, Multimodal learning, Foundation models, Benchmark datasets, Inductive bias<br>

<img src="https://picsum.photos/id/236/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

Large Vision Models (LVMs) such as ViT, Swin, MAE, and SimMIM have shown impressive results in computer vision tasks, sparking interest in applying these models to other domains like time series analysis. Traditionally, transformers and Large Language Models (LLMs) have been explored for time series with mixed success, and mapping time series data to images offers a way to leverage pretrained vision models for non-visual problems. The trend towards multimodal and foundational models in time series research boosts the relevance of this approach for both classification and forecasting tasks.

To address these challenges, the authors propose and systematically evaluate several approaches and contributions:

- The study benchmarks 4 Large Vision Models (ViT, Swin, MAE, SimMIM) pretrained on images, applied to 8 distinct time series imaging methods.
- They use 18 datasets (10 for classification, 8 for forecasting) spanning various domains, ensuring comprehensive evaluation.
- A comparison is performed across 26 models (covering traditional, ML, LLM, CNN, RNN, Transformer, and LVMs) for both classification and forecasting baselines.
- The time series data is converted to images using a variety of methods (Line Plot, GAF, MVH, UVH, STFT, Wavelet, Filterbank, RP) and LVMs are tailored for both high-level (classification) and low-level (forecasting) tasks.
- Customizations include input alignment, imaging, normalization, resizing, and specific decoder/head architectures by task.
- The work includes ablation studies exploring architectural complexity, impact of pretrained components, and differences between fine-tuning and training from scratch.

Following the detailed methodological setup, the study reports key experimental findings:

- LVMs achieve superior accuracy in time series classification tasks across 10 UEA datasets, outperforming all non-LVM baselines.
- In forecasting, the self-supervised MAE model achieves state-of-the-art or highly competitive results on multiple datasets, often outperforming existing methods.
- In classification, Gramian Angular Field (GAF) imaging synergizes best with LVMs; for forecasting, period-based imaging (UVH, MVH) combined with self-supervised LVMs yields the highest performance.
- Self-supervised LVMs demonstrate better transferability for forecasting than supervised versions; normalization layer fine-tuning is especially vital for TSF.
- Pretrained decoders are more critical than encoders in forecasting tasks, signaling a unique property in time series problems.
- LVMs are sensitive to temporal order, experiencing marked accuracy drops under sequence perturbations.
- While LVM-based methods incur higher computational costs, they deliver strong results and are poised to benefit further from hardware advancements.

In light of these results, the researchers draw several important conclusions and outline future directions:

- Pretrained LVMs are highly effective for time series classification but currently face challenges in direct application to time series forecasting.
- The best forecasting outcomes appear when combining self-supervised LVMs with specific imaging methods, though these are biased toward periodic data and struggle with long-range dependencies.
- Pretraining enables robust knowledge transfer for high-level tasks; nonetheless, improvements are needed in encoder capabilities and inductive biases for low-level forecasting.
- Promising research directions include improving LVM encoders for forecasting, addressing period-combination bias, enabling longer input windows, and advancing multimodal time series learning.
