---
title: "Run LLM Locally with Ollama"
subtitle: "From setup to deployment: run and serve local LLMs easily with Ollama"
image: /images/llm/ollama-1.png
date: "2025-05-25"
---

**Keywords:** Ollama, Local LLM, AI deployment, llama3, mistral, phi, generative AI, on-prem AI, LLM inference



## Introduction

Running Large Language Models (LLMs) locally is becoming a key trend for developers and companies who want **privacy, low latency, and cost control**.

Instead of relying on external APIs, tools like **Ollama** allow you to run powerful models directly on your machine with minimal setup.


## What is Ollama?

**Ollama** is a lightweight framework designed to simplify local LLM usage. It enables you to:

- Run LLMs locally (CPU or GPU)
- Download and manage models easily
- Serve models via a local API
- Customize models using simple configuration files

Supported models include:
- `llama3`
- `mistral`
- `phi`
- `gemma`



## Installation

### macOS / Linux

```
curl -fsSL https://ollama.com/install.sh | sh
```

### Windows

Download from:
https://ollama.com/download

### Verify Installation

```
ollama --version
```



## Run Your First Model

Ollama automatically downloads models when you run them:

```
ollama run mistral
```

Interactive prompt example:

```
>>> Explain what is an LLM
```



## Choose a Small Model (Recommended)

For local environments (CPU or small GPU), start with lightweight models:

| Model      | Size  | Notes      |
|------------|-------|------------|
| `phi`      | ~2.7B | Very fast  |
| `gemma:2b` | ~2B   | Efficient  |
| `mistral`  | ~7B   | Balanced   |

Recommended demo:

```
ollama run phi
```



## Using Ollama in Python

**Install dependency**
```
pip install requests
```

**Example code**

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi",
        "prompt": "Explain AI in simple terms",
        "stream": False
    }
)

print(response.json()["response"])
```


## Serve Models via API

Ollama automatically exposes a local API:

```
http://localhost:11434
```

### Curl example

```
curl http://localhost:11434/api/generate -d '{
  "model": "phi",
  "prompt": "Write a short poem",
  "stream": false
}'
```


## Deployment Options

### 1. Local Interactive Mode

```
ollama run phi
```

### 2. REST API

- Integrate with backend applications
- Works with Python, Node.js, etc.

### 3. Docker Deployment

```
docker run -d -p 11434:11434 ollama/ollama
```

### 4. Reverse Proxy (Nginx)

```
server {
    listen 80;
    location / {
        proxy_pass http://localhost:11434;
    }
}
```

### 5. Kubernetes (Advanced)

- Deploy Ollama in containers
- Use GPU-enabled nodes
- Add autoscaling for production



## Custom Models with Modelfile

Create your own assistant:

```
FROM mistral

SYSTEM "You are a helpful AI assistant specialized in data science."

PARAMETER temperature 0.7
```

Build and run:

```
ollama create mymodel -f Modelfile
ollama run mymodel
```



## Performance Tips

- Use GPU (NVIDIA recommended) if available
- Prefer smaller models for CPU usage
- Use quantized models (Q4, Q5)
- Reduce context size if RAM is limited



## When to Use Ollama

### ✅ Ideal for:

- Local AI assistants
- Internal enterprise tools
- RAG pipelines with private data

### ❌ Not ideal for:

- Very large models (>70B)
- Distributed large-scale inference



## Conclusion

Ollama makes running LLMs locally **simple, fast, and production-ready**.

With just a few commands, you can:

- Download and run models
- Serve them via API
- Customize behavior
- Deploy in Docker or Kubernetes

It is a powerful solution for building **private, low-cost, and efficient AI systems**.



## Next Steps

- Integrate with LangChain or LangGraph
- Build a local RAG system (FAISS, Chroma)
- Deploy behind a secure API gateway

