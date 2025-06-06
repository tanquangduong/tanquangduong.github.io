---
title: "OntoRAG: Automating Ontology Derivation for Enhanced Question-Answering"
subtitle: "From Unstructured Electrical Relay Documents to Structured Ontologies"
date: "2025-05-31"
---

**Authors:** Y. Tiwari et al.<br>
**Published on Arxiv:** 2025-05-31<br>
**Link:** http://arxiv.org/abs/2506.00664v1<br>
**Institutions:** ABB Ability Innovation Center, Bangalore, India • ABB Ability Innovation Center, Hyderabad, India • Indian Institute of Technology, Kharagpur, India<br>
**Keywords:** LLM, Ontology Learning, Retrieval-Augmented Generation, Knowledge Graph, GraphRAG, Leiden algorithm, Semantic Web, Question Answering, PDF Parsing, Information Extraction<br>

<img src="https://picsum.photos/id/714/300/200" 
alt="Random Unsplash-style image" 
style="display: block; margin-left: auto; margin-right: auto; border-radius:8px; margin-bottom:1em; box-shadow: 0 4px 16px rgba(0,0,0,0.15);">

<!-- Context -->

Ontologies are crucial for structuring knowledge bases to improve the performance of question-answering (QA) systems using Large Language Models. However, the manual creation of ontologies is a significant bottleneck, especially in large or rapidly evolving technical domains.

To address these challenges, the authors introduce their solution and methodology as follows:

- OntoRAG is an automated pipeline designed to extract ontologies from unstructured data, specifically electrical relay documents in PDF format.
- The pipeline encompasses components such as web scraping, advanced PDF parsing, hybrid and semantic chunking, information extraction—including Named Entity Recognition and atomic fact detection—knowledge graph construction, and automated ontology generation.
- Community detection via the Leiden algorithm and LLM-assisted property synthesis (utilizing Gemini 2.5 Flash) ensure semantic coherence and ontological integrity.
- The method enables multi-hop reasoning and structured retrieval capabilities with the created ontology.
- Experiments compare OntoRAG against baseline vector-based Retrieval-Augmented Generation (semantic search) and GraphRAG, employing a proprietary dataset with 1 million tokens from technical documentation on electrical relays.
- Evaluation involves both qualitative and claim-based quantitative metrics: comprehensiveness, diversity, empowerment, and directness.

Following the description of OntoRAG's methodology, the results further underscore its efficacy:

- OntoRAG delivers comprehensiveness win rates of 88% over semantic search and 65% over the best GraphRAG configuration, along with diversity win rates of 86% and 62%, respectively.
- Claim-based analysis reveals OntoRAG generates more unique claims and greater diversity (35.2 claims, 14.1 clusters) compared to GraphRAG (34.8 claims, 13.8 clusters) and semantic search (26.5 claims, 8.0 clusters).
- It consistently surpasses GraphRAG at all ontology granularities regarding comprehensiveness and diversity.
- Empowerment scores are similar between OntoRAG and GraphRAG, with semantic search being strongest in directness.
- The computational cost for creating ontologies is higher for OntoRAG (300 minutes for 1M tokens) than for GraphRAG (281 minutes), presenting scalability challenges.

To complete the discussion, the authors offer their main conclusions:

- OntoRAG enables major advances in fully automated ontology creation from unstructured sources, notably enhancing question-answering performance in terms of comprehensiveness and diversity.
- By removing the dependency on manual curation and maintaining ontological integrity, it promotes effective knowledge organization in complex technical fields.
- Current limitations relate to computational intensity and the use of domain-specific prompts, which affect scalability and applicability to new fields.
- Future research will aim to optimize computational efficiency, scale up to larger datasets, and generalize the framework to other domains using adaptive prompts.
