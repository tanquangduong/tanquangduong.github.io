---
title: "Deploying and Serving LLM with vLLM"
subtitle: "End-to-end guide: deploy and serve LLMs at scale with vLLM for high-throughput, low-latency inference"
image: /images/llm/vllm-deploying-serving-300px.png
date: "2025-07-15"
---

**Keywords:** vLLM, LLM serving, model deployment, inference optimization, PagedAttention, OpenAI API, batching, GPU inference, production LLM

![](/images/llm/vllm-deploying-serving-300px.png){fig-align="center" width=300}

## Introduction
Serving Large Language Models (LLMs) in production requires more than just loading a model and running inference. You need **high throughput, low latency, and efficient GPU memory usage** to handle real-world traffic.

**vLLM** is an open-source library designed specifically for this purpose. It makes LLM serving:

- **Fast** (up to 24x higher throughput than naive serving)
- **Memory-efficient** (via PagedAttention)
- **Production-ready** (OpenAI-compatible API server)
- **Easy to deploy** (Docker, Kubernetes, cloud)

In this tutorial, we will walk through a **complete pipeline**:

1. Install and configure vLLM
2. Serve a model with the OpenAI-compatible API
3. Query the model from Python
4. Optimize for production deployment


## What is vLLM?
**vLLM** is a high-throughput and memory-efficient inference and serving engine for LLMs. Key features include:

- **PagedAttention**: Efficient memory management inspired by OS virtual memory, reducing GPU memory waste
- **Continuous batching**: Dynamically batches incoming requests for maximum throughput
- **OpenAI-compatible API**: Drop-in replacement for OpenAI API endpoints
- **Tensor parallelism**: Distribute models across multiple GPUs
- **Support for many models**: Llama, Mistral, Qwen, Phi, Gemma, and more


## Hardware Requirements
vLLM is designed for **GPU inference**. Minimum requirements depend on your model size:

| Model Size | Minimum GPU VRAM | Recommended GPU |
|-----------|-----------------|----------------|
| 0.5B–3B | 4 GB | RTX 3060 / T4 |
| 7B–8B | 16 GB | RTX 4090 / A10 |
| 13B | 24 GB | A10 / A100 |
| 70B | 80 GB+ | A100 / H100 (multi-GPU) |

For CPU-only machines, consider using Ollama or llama.cpp instead.


## Installation

### Install vLLM

```bash
pip install vllm
```

### Install with CUDA support (recommended)

```bash
pip install vllm[cuda]
```

### Verify installation

```python
import vllm
print(vllm.__version__)
```


## Offline Inference (Batch Processing)
Use vLLM for fast batch inference without starting a server.

### Basic Example

```python
from vllm import LLM, SamplingParams

llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct")

sampling_params = SamplingParams(
    temperature=0.7,
    max_tokens=256,
)

prompts = [
    "Explain machine learning in simple terms.",
    "What is the difference between AI and ML?",
    "Write a Python function to reverse a string.",
]

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    print(output.outputs[0].text)
    print("---")
```

### Chat-style Inference

```python
from vllm import LLM, SamplingParams

llm = LLM(model="Qwen/Qwen2.5-0.5B-Instruct")

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Explain vLLM in simple terms."},
]

sampling_params = SamplingParams(
    temperature=0.7,
    max_tokens=256,
)

outputs = llm.chat(messages=[messages], sampling_params=sampling_params)

print(outputs[0].outputs[0].text)
```


## Serving with OpenAI-Compatible API
vLLM provides an API server that is **fully compatible with the OpenAI API format**.

### Start the Server

```bash
vllm serve Qwen/Qwen2.5-0.5B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key \
    --served-model-name my-model \
    --chat-template ./chat_template.jinja \
    --gpu-memory-utilization 0.90
```

Key options explained:

- `--served-model-name`: Sets the model name exposed in the API (clients use this name in requests instead of the full HuggingFace path)
- `--chat-template`: Path to a Jinja2 chat template file for formatting chat messages (useful for custom or fine-tuned models)
- `--gpu-memory-utilization`: Fraction of GPU memory to use (0.0–1.0, default 0.9). Increase for larger models, decrease to leave room for other processes

### Start with Custom Parameters

```bash
vllm serve Qwen/Qwen2.5-0.5B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key \
    --served-model-name my-model \
    --chat-template ./chat_template.jinja \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.90 \
    --dtype auto
```

### Verify the Server

```bash
curl http://localhost:8000/v1/models
```


## Querying the API

### Using curl

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer your-secret-key" \
    -d '{
        "model": "my-model",
        "messages": [
            {"role": "user", "content": "What is vLLM?"}
        ],
        "temperature": 0.7,
        "max_tokens": 256
    }'
```

### Using Python (requests)

```python
import requests

response = requests.post(
    "http://localhost:8000/v1/chat/completions",
    headers={"Authorization": "Bearer your-secret-key"},
    json={
        "model": "my-model",
        "messages": [
            {"role": "user", "content": "Explain PagedAttention."}
        ],
        "temperature": 0.7,
        "max_tokens": 256,
    }
)

print(response.json()["choices"][0]["message"]["content"])
```

### Using OpenAI Python Client (Recommended)

Since vLLM is OpenAI-compatible, you can use the official OpenAI client:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="your-secret-key",
)

response = client.chat.completions.create(
    model="my-model",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is continuous batching?"},
    ],
    temperature=0.7,
    max_tokens=256,
)

print(response.choices[0].message.content)
```


## Serving Custom / Fine-tuned Models
If you fine-tuned a small LLM with **Unsloth** and exported it to GGUF (e.g., `gguf_model_small`), here is how to serve it with vLLM.

vLLM **natively supports GGUF** files — no conversion required. See the [official vLLM GGUF documentation](https://docs.vllm.ai/en/stable/features/quantization/gguf/) for full details.

> **Note:** GGUF support in vLLM is experimental and under-optimized. Currently, only **single-file** GGUF models are supported. If you have a multi-file GGUF model, use [`gguf-split`](https://github.com/ggerganov/llama.cpp/pull/6135) to merge them first.

### Option A: Serve a GGUF file directly

#### Step 1: Prepare Your GGUF Model

After fine-tuning with Unsloth and exporting to GGUF, you should have a file like:

```bash
gguf_model_small/
├── added_tokens.json
├── chat_template.jinja
├── config.json
├── generation_config.json
├── merges.txt
├── model.safetensors
├── special_tokens_map.json
├── tokenizer.json
├── tokenizer_config.json
├── unsloth.BF16.gguf
├── unsloth.Q4_K_M.gguf
└── vocab.json
```

#### Step 2: Serve with vLLM

Point vLLM directly at the GGUF file. Use `--tokenizer` to specify the base model's tokenizer (recommended over the GGUF-embedded tokenizer for stability):

```bash
vllm serve ./gguf_model_small/unsloth.Q4_K_M.gguf \
    --tokenizer ./gguf_model_small \
    --served-model-name my-finetuned-model \
    --chat-template ./chat_template.jinja \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key \
    --gpu-memory-utilization 0.90 \
    --max-model-len 2048
```

You can also load GGUF models from HuggingFace using the `repo_id:quant_type` format:

```bash
vllm serve unsloth/Qwen3-0.6B-GGUF:Q4_K_M \
    --tokenizer Qwen/Qwen3-0.6B \
    --served-model-name qwen3-gguf \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key \
    --gpu-memory-utilization 0.90
```

Add `--tensor-parallel-size 2` to distribute across multiple GPUs:

```bash
vllm serve unsloth/Qwen3-0.6B-GGUF:Q4_K_M \
    --tokenizer Qwen/Qwen3-0.6B \
    --tensor-parallel-size 2 \
    --api-key your-secret-key
```

#### Step 3: Verify and Query

```bash
curl http://localhost:8000/v1/models \
    -H "Authorization: Bearer your-secret-key"
```

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="your-secret-key",
)

response = client.chat.completions.create(
    model="my-finetuned-model",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is fine-tuning?"},
    ],
    temperature=0.7,
    max_tokens=256,
)

print(response.choices[0].message.content)
```

### Option B: Serve in Hugging Face format (safetensors)

If you prefer **maximum compatibility** (e.g., with LoRA adapters or features not yet supported with GGUF), export in HF format instead:

```python
# During fine-tuning with Unsloth, save in HF format
model.save_pretrained_merged("hf_model_small", tokenizer)
```

Then serve:

```bash
vllm serve ./hf_model_small \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key \
    --served-model-name my-finetuned-model \
    --chat-template ./chat_template.jinja \
    --gpu-memory-utilization 0.90 \
    --dtype auto \
    --max-model-len 2048
```

### Serve a LoRA Adapter (Without Merging)

If you prefer to keep LoRA weights separate, vLLM supports serving LoRA adapters on top of a base model:

```bash
vllm serve Qwen/Qwen2.5-0.5B-Instruct \
    --enable-lora \
    --lora-modules my-lora=./lora_model \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key
```

Then query with the LoRA model name:

```python
response = client.chat.completions.create(
    model="my-lora",
    messages=[{"role": "user", "content": "Hello!"}],
)
```


## Docker Deployment
Deploy vLLM in a container for production environments.

### Dockerfile

```dockerfile
FROM vllm/vllm-openai:latest

ENV MODEL_NAME=Qwen/Qwen2.5-0.5B-Instruct

CMD ["--model", "${MODEL_NAME}", "--host", "0.0.0.0", "--port", "8000"]
```

### Run with Docker

```bash
docker run --gpus all \
    -p 8000:8000 \
    vllm/vllm-openai:latest \
    --model Qwen/Qwen2.5-0.5B-Instruct \
    --host 0.0.0.0 \
    --port 8000
```


## Performance Optimization Tips

- **GPU memory utilization**: Set `--gpu-memory-utilization 0.90` to maximize GPU usage (range: 0.0–1.0)
- **Served model name**: Use `--served-model-name` for cleaner API model names instead of long HuggingFace paths
- **Chat template**: Use `--chat-template` to apply a custom Jinja2 chat template for fine-tuned models
- **Quantization**: Use AWQ or GPTQ quantized models to reduce VRAM
- **Tensor parallelism**: Use `--tensor-parallel-size N` for multi-GPU setups
- **Max model length**: Reduce `--max-model-len` if you don't need long contexts
- **Continuous batching**: Enabled by default, handles concurrent requests efficiently
- **Streaming**: Use `stream=True` for real-time token generation


## vLLM vs Other Serving Solutions

| Feature | vLLM | Ollama | TGI | llama.cpp |
|--------|------|--------|-----|-----------|
| Throughput | Very High | Medium | High | Low-Medium |
| GPU Required | Yes | Optional | Yes | Optional |
| OpenAI API | Yes | Partial | Yes | Partial |
| Multi-GPU | Yes | No | Yes | No |
| Ease of Use | Medium | Easy | Medium | Medium |
| Best For | Production | Local Dev | Production | Edge/CPU |


## Conclusion
vLLM is the go-to solution for **high-performance LLM serving in production**:

- Serves models with an OpenAI-compatible API
- Handles high-concurrency with continuous batching
- Optimizes GPU memory with PagedAttention
- Supports custom and fine-tuned models
- Deploys easily with Docker and Kubernetes

This workflow is perfect for:

- Production AI APIs
- Enterprise LLM platforms
- High-traffic chatbot backends
- Multi-model serving infrastructure


## Next Steps
- Combine with a RAG pipeline (LangChain + vLLM)
- Add load balancing with Nginx or Traefik
- Deploy on Kubernetes with GPU node pools
- Monitor with Prometheus + Grafana
- Serve multiple models with model routing
