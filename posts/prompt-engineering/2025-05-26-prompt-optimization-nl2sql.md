---
title: "Effectiveness of Prompt Optimization in NL2SQL Systems"
subtitle: "A Multi-Objective Approach to Improving Accuracy and Efficiency"
date: "2025-05-26"
---

**Authors: ** S. Gurajada et al.<br>
**Published on Arxiv: ** 2025-05-26<br>
**Link: ** <http://arxiv.org/abs/2505.20591v1><br>
**Institutions:** Megagon Labs • Adobe<br>
**Keywords:** NL2SQL, large language models, prompt optimization, in-context learning, multi-objective optimization, schema pruning, SQL generation, BIRD dataset, GPT-4o, query latency<br>

<!-- Change the folliwng id_value randomly between 1 and 1000 to get different random images. -->
<img src="https://picsum.photos/id/802/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

Natural Language to SQL (NL2SQL) systems have leveraged large language models (LLMs) to enable translation of natural language queries into SQL statements for domain-specific databases. Traditionally, in-context learning (ICL) methods guide LLMs using carefully selected schema, cell values, and exemplars—typically chosen through retrieval-based techniques that add inference-time overhead. Prior work has focused on SQL generation quality, often overlooking efficiency and suitability for production deployment.

To address these efficiency challenges, the authors introduce their proposed solution:


- They propose a prompt optimization framework for NL2SQL that statically selects a representative set of exemplars and instructions, jointly optimizing for both accuracy and efficiency using multi-objective techniques.

- The introduced Iterative Prompt Optimization (IPO) is a bi-agent LLM system (Proposer, SQL Generator) that iteratively refines instructions and exemplars based on performance feedback, promoting schema pruning and concise prompts.

- Benchmarking is performed using the new BIRD-MULTI dataset, which extends BIRD with query execution latency annotations, supporting optimization for both SQL accuracy and execution efficiency.


Following this approach, the authors evaluate and present their main experimental results:


- IPO, using GPT-4o, consistently outperforms baselines such as Random Exemplar Selection (RES), Optimized Random Exemplar Selection (ORES), and MIPROv2 on the BIRD dataset, particularly excelling with complex queries.

- Through iterative schema pruning, IPO generates the shortest prompts (around 6.5k tokens) while maintaining comparable optimization times to other methods.

- Using a multi-objective optimization strategy, IPO increases SQL execution efficiency: optimizing for both accuracy and latency results in reduced maximum and average query latencies, while maintaining execution accuracy (58.98% with latency optimization vs 59.24% for accuracy-only on BIRD dev).


Finally, the paper draws several key conclusions from the findings:


- Joint selection of instructions and exemplars through prompt optimization leads to improvements in both accuracy and efficiency for NL2SQL systems.

- Iterative prompt optimization not only boosts SQL generation performance but also facilitates concise prompt creation via schema pruning without sacrificing accuracy.

- Multi-objective optimization is vital for deploying NL2SQL systems in real-world settings, as it enables generation of efficient, accurate queries; the BIRD-MULTI benchmark is a meaningful contribution supporting this advancement.
