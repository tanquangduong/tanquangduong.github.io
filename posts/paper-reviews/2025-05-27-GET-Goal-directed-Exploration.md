---
title: "GET: Goal-directed Exploration and Targeting for Large-Scale Unknown Environments"
subtitle: "Integrating LLM-based Semantic Reasoning and Memory for Autonomous Robot Search"
date: "2025-05-27"
---

**Authors: ** L. Zheng et al.<br>
**Published on Arxiv: ** 2025-05-27<br>
**Link: ** <http://arxiv.org/abs/2505.20828v1><br>
**Institutions:** Sun Yat-Sen University, School of Computer Science and Engineering • Sun Yat-Sen University, School of Systems Science and Engineering • Sun Yat-Sen University, School of Artificial Intelligence<br>
**Keywords:** Large Language Models, LLM reasoning, Embodied AI, Object search, Goal-directed exploration, Diagram of Unified Thought (DoUT), Gaussian Mixture Model, Semantic octomap, Probabilistic memory, Autonomous robotics, Real-world experiments, Trajectory optimization, Spatial reasoning<br>

<img src="https://picsum.photos/seed/751469/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

Searching for objects in vast, unstructured environments poses significant challenges for autonomous robots, especially under dynamic or outdoor conditions. Traditional approaches, often based on heuristics or hand-crafted routines, typically fail to generalize, while modern deep learning and reinforcement learning algorithms demand enormous data and may still lack robust transferability. Large Language Models (LLMs) introduce semantic reasoning, yet they struggle with spatial reasoning and effective use of memory in physically grounded settings.

To bridge these gaps, the article presents a novel framework, GET, which proposes the following key approaches and contributions:

- GET (Goal-directed Exploration and Targeting) synergizes LLM-based reasoning with experience-guided spatial exploration to enhance object search in unknown large-scale environments.
- Incorporates DoUT (Diagram of Unified Thought), a unique reasoning module that employs a role-based feedback loop for real-time, task-adaptive decisions by integrating both external memory and task-specific requirements.
- Models past search experiences via a Gaussian Mixture Model, forming probabilistic maps that update priors about object locations, optimizing efficiency for repeated and novel searches.
- Demonstrates the framework in real-world settings using a two-wheeled robot, with systematic comparisons against heuristic, baseline, and LLM-only strategies using recognized benchmarks such as path length, search time, and success rate.

Building on this integrated approach, the results highlight the significant performance gains achieved by GET:

- GET surpasses heuristic and LLM-only baselines, demonstrating marked improvements in search efficiency and robustness.
- In initial searches, GET reduces both path length and search time by substantial margins—up to 58.7% reduction against FAEL, TARE, EFP, and Sem baselines across all evaluated scenes.
- In repeated or dynamically changing tasks, the system leverages probabilistic memory to further minimize search time and path, providing consistently better performance with less variability.
- The DoUT module enables more rapid and accurate convergence of LLM-based reasoning, outperforming previous architectures (such as DoT) as indicated by higher cosine similarity scores among various LLMs (GPT-4o, GPT-4o-mini, LearnLM 1.5, Moonshot AI).

Drawing on these comprehensive results, the study concludes with the following takeaways:

- GET enables robust, scalable, and highly efficient autonomous object search in unfamiliar environments through structured LLM-based reasoning and adaptive, experience-driven memory integration.
- The DoUT framework offers a versatile, real-time decision-making foundation for embodied AI, supporting rapid adaptation to new tasks and scenarios.
- State-of-the-art outcomes on real robot benchmarks demonstrate the high generalizability of the approach, opening new possibilities for research in LLM-embodied integration and data-efficient robotic control.
