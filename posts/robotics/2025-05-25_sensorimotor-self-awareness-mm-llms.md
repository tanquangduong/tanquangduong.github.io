---
title: "Sensorimotor Features of Self-Awareness in Multimodal LLMs Embedded in Robots"
subtitle: "Emergence of Artificial Self-Awareness via Sensorimotor Integration and Memory"
date: "2025-05-25"
---

**Authors: ** I. Dellibarda Varela et al.<br>
**Published on Arxiv: ** 2025-05-25<br>
**Link: ** [http://arxiv.org/abs/2505.19237v1](http://arxiv.org/abs/2505.19237v1)<br>
**Institutions:** Center for Automation and Robotics, Spanish National Research Council (CSIC-UPM), Madrid, Spain • Department of Electronic Engineering, University of Azuay, Cuenca, Ecuador<br>
**Keywords:** Self-Awareness, Robotic Embodiment, Artificial Intelligence, Multimodal Large Language Models, Sensorimotor Integration, Episodic Memory, Gemini 2.0, Mobile Robot, Structural Equation Modeling, Embodied Cognition

<img src="https://picsum.photos/id/764/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

Self-awareness is fundamental for intelligent and autonomous behavior, but its mechanisms in artificial systems remain largely unexplored compared to the extensive research in humans and animals. Recent advances in large language models, especially multimodal variants, have shown human-like capacities in integrating sensory input, raising the question: can machine self-awareness arise through embodied sensorimotor experience?

To address this critical question, the authors designed a study employing multimodal large language models (MM-LLMs) embedded in autonomous robotics platforms. The study's approach and main contributions are as follows:

- Evaluating whether a multimodal LLM (Gemini 2.0 Flash) can develop self-awareness from raw sensorimotor data while operating autonomously in a physical environment.
- Decomposing self-awareness into three distinct dimensions: environmental, individual, and predictive awareness.
- Utilizing a suite of sensors (encoders, IMU, LiDAR, RGB-D camera) and episodic memory for the robot to iteratively predict its own state.
- Implementing an LLM-as-Judge scoring system and employing structural equation modeling (SEM) to evaluate the emergence and hierarchy of self-awareness features.
- Conducting ablation studies to test the influence of different sensory modalities on self-awareness development.

Following the innovative methodology, the paper presents its results, outlining the effectiveness of sensorimotor and memory integration for self-awareness in embodied AI systems:

- The MM-LLM achieves robust self-awareness across several key metrics, consistently surpassing 3/5 in self-identification, dimensional reasoning, and movement prediction, though somewhat weaker in environmental awareness.
- Predictive performance rapidly improves and stabilizes with continued exploration and episodic memory storage, particularly in movement and self-identification tasks.
- SEM highlights the decisive role of memory and spatial sensing for coherent, multi-dimensional self-awareness, and marks the importance of vision for environmental context.
- Ablation reveals that removing memory severely disrupts prediction coherence, while absence of visual input causes significant misclassification (e.g., misinterpreting ground movement for flight); compensation is observed when other modalities are omitted.
- The AI system cannot pinpoint its precise robot model but reliably classifies itself as a mobile, wheeled robot.

Finally, drawing together these findings, the authors reach several important conclusions about the foundations and future potential of embodied machine self-awareness:

- Multimodal sensorimotor integration and structured episodic memory enable coherent, internally grounded self-awareness in physical robots powered by MM-LLMs.
- Memory is vital for perceiving movement continuity and maintaining temporal self-consistency, while vision principally underpins environmental awareness.
- The research demonstrates that, with adequate sensory and memory supports, current MM-LLMs can autonomously develop forms of self-awareness reminiscent of biological agents.
- These outcomes imply that present architectures may already encompass the key mechanisms needed for machine self-awareness, paving the way toward advanced artificial cognitive systems with embodied intelligence.
