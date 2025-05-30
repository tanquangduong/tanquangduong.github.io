---
title: "Hume: Integrating System-2 Thinking into Vision-Language-Action Robots"
subtitle: "A Dual-System Model for Expert Robot Control and Robust Recovery"
date: "2025-05-27"
---

**Authors:** H. Song et al.<br>
**Published on Arxiv:** 2025-05-27<br>
**Link:** <http://arxiv.org/abs/2505.21432v1><br>
**Institutions:** Shanghai Jiao Tong University • Shanghai AI Laboratory • Zhejiang University • AgiBot<br>
**Keywords:** Vision-Language-Action models, System-2 thinking, Dual-system robot control, Value-guided action selection, Cascaded action denoising, Offline reinforcement learning, Robotic manipulation, Generalist robots, Failure recovery, Flow matching, Diffusion policy

<img src="https://picsum.photos/800/400" alt="Random Unsplash-style image" style="border-radius:8px; margin-bottom:1em;">

<!-- Context -->

The development of generalist robots capable of matching human dexterity across diverse tasks remains a central goal in robotics. Traditionally, these efforts have focused on fast, reactive models inspired by System-1 thinking, but leveraging System-2's deliberate, value-guided reasoning—prevalent in human cognition—for robot control is still largely unexplored. Prior attempts at vision-language-action (VLA) architectures have either lacked genuine System-2 integration or failed to harmonize slow reasoning with the swift execution required in real-world robotics.

To address these gaps, the paper introduces Hume, presenting a novel approach:

- Hume implements a dual-system VLA architecture, where System 2 operates as a slow, value-guided deliberative module generating and ranking action candidates, and System 1 acts as a fast, reactive controller refining selected actions in real time.
- The architecture is trained via offline reinforcement learning on robotics demonstrations and evaluated extensively in both simulation (LIBERO, SimplerEnv) and on real robots (WidowX, Franka, AgiBot G-1), with ablation studies to isolate the effects of each system component.

Building upon this framework, the study assesses Hume's impact with extensive benchmarks:
- On the LIBERO benchmark, Hume achieves a record 98.6% success rate, outperforming leading baselines.
- In SimplerEnv, Hume delivers state-of-the-art results, showing remarkable improvements on both simulated and physical manipulation tasks, with robust recovery from failures and clear gains isolated in ablation analyses.

These compelling results culminate in several major conclusions:
- Hume's dual-system VLA design unites the strengths of System-2 deliberation and System-1 reactivity, yielding superior task performance and error recovery in robotic manipulation.
- While demonstrating significant advantages, Hume's reliance on the quality of action proposals and simplicity of value-guidance underscores opportunities for further work, including advanced deliberative strategies and real-time reinforcement learning advancements.