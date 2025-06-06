---
title: "Towards Reliable Large Audio Language Model"
subtitle: "Improving Reliability and Trustworthiness in Universal Audio Understanding via LALMs"
date: "2025-05-25"
---

**Authors: ** Z. Ma et al.<br>
**Published on Arxiv: ** 2025-05-25<br>
**Link: ** <http://arxiv.org/abs/2505.19294v1><br>
**Institutions:** X-LANCE Lab, School of Computer Science, MoE Key Lab of Artificial Intelligence, Shanghai Jiao Tong University • ByteDance • Shanghai Innovation Institute<br>
**Keywords:** Large Audio Language Model, LALM, Reliability, Reliability Gain Index, RGI, Supervised Fine-Tuning, SFT, LoRA, Qwen2-Audio, IDK Prompting, Multi-Modal Chain-of-Thought, MCoT, Audio Understanding, Speech, Music, Sound, Trustworthiness, Humbleness, Truthfulness, Conservativeness, Transfer Learning, Benchmark, Evaluation Metrics

<img src="https://picsum.photos/id/216/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

Large Audio Language Models (LALMs) have recently emerged as universal tools for audio understanding and reasoning across modalities including speech, music, and general sound. Despite notable advancements, these models exhibit a critical weakness: they are unable to recognize their own knowledge boundaries and fail to refuse questions that exceed their capabilities. This shortcoming poses threats to reliability in practical scenarios such as healthcare, autonomous driving, and interactive agents. Moreover, conventional evaluation metrics do not adequately assess the effectiveness of LALMs in striking the balance between providing answers (being helpful) and refraining from guessing (demonstrating humbleness).

To address these challenges, the authors propose and systematically evaluate solutions that enhance the reliability of LALMs:

- Systematic investigation into LALM reliability through both training-free and training-based approaches.
- Training-free methods include IDK (I Don't Know) prompting, Multi-Modal Chain-of-Thought (MCoT) prompting, and Task Agent strategies, all designed to encourage the model to admit uncertainty without requiring additional training.
- A training-based strategy using Supervised Fine-Tuning (SFT) on custom IDK datasets teaches the model to respond 'I don't know' when unsure, thereby directly improving reliability.
- Introduction of the Reliability Gain Index (RGI), a novel metric gauging the improvement in humbleness versus conservativeness, to accurately assess model reliability.
- Experimental evaluations primarily focus on the Qwen2-Audio-7B-Instruct model and the MMAU benchmark, and results are compared with leading open-source LALMs like SALMONN and Qwen-Audio-Chat across a variety of quantitative metrics.

The authors validate their approach with detailed experiments, and the results reveal several important findings:

- Both training-free and training-based methods contribute to enhanced LALM reliability, with supervised fine-tuning delivering the best trade-off between helpfulness and truthfulness.
- The newly introduced RGI metric effectively distinguishes genuine reliability improvements from excessive conservativeness.
- Reliability awareness emerges as a transferable skill or 'meta ability,' with positive results observed even when training and testing across different audio modalities such as sound, speech, and music.
- Benchmarks using the MMAU dataset confirm that Qwen2-Audio-7B-Instruct, especially with reliability-focused methods, outperforms or matches other state-of-the-art open-source LALMs across accuracy, truthfulness, reliability, and RGI metrics.

In conclusion, the study makes significant contributions by initiating the exploration of reliability in large audio language models and offering effective solutions and metrics for evaluation:

- This is the first systematic exploration of reliability in LALMs, providing both new methodological solutions and a new evaluation metric (RGI).
- Reliability awareness, particularly the capacity to answer with 'I don't know,' is demonstrated to be transferable between modalities despite structural differences.
- Future directions include extending reliability transfer to cross even broader modality gaps—such as from audio to video—as well as developing models capable of interactive justifications or clarification requests when uncertain.
