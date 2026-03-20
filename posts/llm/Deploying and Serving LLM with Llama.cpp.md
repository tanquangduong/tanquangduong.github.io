---
title: "Deploying and Serving LLM with Llama.cpp"
subtitle: "End-to-end guide: deploy and serve LLMs locally and at scale with llama.cpp for efficient CPU/GPU inference"
image: /images/llm/llama.cpp-300.png
date: "2025-07-16"
---

**Keywords:** llama.cpp, LLM serving, model deployment, GGUF, quantization, inference optimization, CPU inference, GPU inference, OpenAI API, production LLM

![](/images/llm/llama.cpp-300.png){fig-align="center" width=300}

## Introduction
Not every LLM deployment requires a high-end GPU cluster. Many real-world use cases — edge devices, local development, cost-sensitive production — demand **efficient inference on commodity hardware**.

**llama.cpp** is an open-source C/C++ inference engine that makes LLM deployment:

- **Hardware-flexible** (runs on CPU, GPU, Apple Silicon, and hybrid CPU+GPU)
- **Memory-efficient** (via aggressive quantization — 2-bit to 8-bit GGUF formats)
- **Production-ready** (built-in OpenAI-compatible API server)
- **Portable** (no Python runtime or CUDA toolkit required at inference time)
- **Easy to deploy** (single binary, Docker, embedded systems)

In this tutorial, we will walk through a **complete pipeline**:

1. Install and build llama.cpp
2. Obtain and quantize models in GGUF format
3. Run offline inference from the CLI
4. Serve a model with the OpenAI-compatible API server
5. Query the model from Python
6. Optimize for production deployment


## What is llama.cpp?
**llama.cpp** is a high-performance C/C++ inference engine for LLMs, originally created by Georgi Gerganov. Key features include:

- **GGUF format**: Purpose-built model format with embedded metadata, supporting a wide range of quantization levels
- **Quantization**: Reduce model size and memory usage with minimal quality loss (Q2_K through Q8_0)
- **CPU optimization**: AVX, AVX2, AVX-512, ARM NEON for fast inference without a GPU
- **GPU offloading**: Offload layers to NVIDIA (CUDA), AMD (ROCm), Apple Metal, or Vulkan GPUs
- **Built-in server**: OpenAI-compatible HTTP API with continuous batching
- **Support for many models**: Llama, Mistral, Qwen, Phi, Gemma, DeepSeek, and more


## Hardware Requirements
llama.cpp is designed to run on a **wide range of hardware**, from laptops to servers:

| Model Size | Quantization | RAM/VRAM Needed | Recommended Hardware |
|-----------|-------------|----------------|---------------------|
| 0.5B–3B | Q4_K_M | 2–3 GB | Any modern CPU / Raspberry Pi 5 |
| 7B–8B | Q4_K_M | 5–6 GB | 16 GB RAM laptop / RTX 3060 |
| 13B | Q4_K_M | 9–10 GB | 32 GB RAM / RTX 4090 |
| 70B | Q4_K_M | 40–45 GB | 64 GB RAM / A100 (multi-GPU) |

**Key advantage:** llama.cpp can run entirely on CPU, making it ideal for environments without GPUs.


## Installation

### Option A: Install via pip (Recommended)

The easiest way to install llama.cpp's Python bindings and server:

```bash
pip install llama-cpp-python
```

With GPU acceleration (CUDA):

```bash
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python
```

With Apple Metal support:

```bash
CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python
```

### Option B: Build from Source

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```

#### CPU-only build:

```bash
cmake -B build
cmake --build build --config Release
```

#### With CUDA support:

```bash
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release
```

#### With Apple Metal support:

```bash
cmake -B build -DGGML_METAL=ON
cmake --build build --config Release
```

### Verify installation

```bash
./build/bin/llama-cli --version
```


## Obtaining GGUF Models

### Download Pre-quantized Models from HuggingFace

Many models are available pre-quantized in GGUF format:

```bash
# Using huggingface-cli
pip install huggingface_hub
huggingface-cli download unsloth/Qwen3-0.6B-GGUF Q4_K_M.gguf --local-dir ./models
```

### Quantize a Model Yourself

If you have a model in HuggingFace (safetensors) format, convert and quantize it:

```bash
# Step 1: Convert to GGUF (F16)
python convert_hf_to_gguf.py ./hf_model_dir --outfile model-f16.gguf --outtype f16

# Step 2: Quantize to Q4_K_M
./build/bin/llama-quantize model-f16.gguf model-Q4_K_M.gguf Q4_K_M
```

### Common Quantization Levels

| Quantization | Bits | Size (7B) | Quality | Speed |
|-------------|------|----------|---------|-------|
| Q2_K | 2 | ~2.7 GB | Low | Fastest |
| Q4_K_M | 4 | ~4.1 GB | Good | Fast |
| Q5_K_M | 5 | ~4.8 GB | Very Good | Medium |
| Q6_K | 6 | ~5.5 GB | Excellent | Medium |
| Q8_0 | 8 | ~7.2 GB | Near-FP16 | Slower |
| F16 | 16 | ~13.5 GB | Lossless | Slowest |

**Recommendation:** `Q4_K_M` offers the best balance of quality, size, and speed for most use cases.


## Offline Inference (CLI)
Use llama.cpp for fast inference directly from the command line.

### Basic Text Generation

```bash
./build/bin/llama-cli \
    -m ./models/Q4_K_M.gguf \
    -p "Explain machine learning in simple terms." \
    -n 256 \
    --temp 0.7
```

### Interactive Chat Mode

```bash
./build/bin/llama-cli \
    -m ./models/Q4_K_M.gguf \
    --chat-template chatml \
    -cnv \
    --temp 0.7
```

### With GPU Offloading

Offload layers to GPU for faster inference (use `-ngl` to specify number of layers):

```bash
./build/bin/llama-cli \
    -m ./models/Q4_K_M.gguf \
    -p "What is the difference between AI and ML?" \
    -n 256 \
    -ngl 99 \
    --temp 0.7
```

`-ngl 99` offloads all layers to GPU. Use a lower number for partial offloading when VRAM is limited.

### Batch Inference with Python

```python
from llama_cpp import Llama

llm = Llama(
    model_path="./models/Q4_K_M.gguf",
    n_ctx=4096,
    n_gpu_layers=-1,  # -1 = offload all layers to GPU
)

prompts = [
    "Explain machine learning in simple terms.",
    "What is the difference between AI and ML?",
    "Write a Python function to reverse a string.",
]

for prompt in prompts:
    output = llm(
        prompt,
        max_tokens=256,
        temperature=0.7,
    )
    print(output["choices"][0]["text"])
    print("---")
```

### Chat-style Inference with Python

```python
from llama_cpp import Llama

llm = Llama(
    model_path="./models/Q4_K_M.gguf",
    n_ctx=4096,
    n_gpu_layers=-1,
    chat_format="chatml",
)

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "Explain llama.cpp in simple terms."},
]

output = llm.create_chat_completion(
    messages=messages,
    max_tokens=256,
    temperature=0.7,
)

print(output["choices"][0]["message"]["content"])
```


## Serving with OpenAI-Compatible API
llama.cpp includes a built-in HTTP server that is **fully compatible with the OpenAI API format**.

### Start the Server (C++ binary)

```bash
./build/bin/llama-server \
    -m ./models/Q4_K_M.gguf \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key \
    --chat-template chatml \
    -ngl 99 \
    -c 4096 \
    --slots 4
```

Key options explained:

- `-m`: Path to the GGUF model file
- `-ngl 99`: Number of layers to offload to GPU (99 = all layers)
- `-c 4096`: Context length (max tokens for input + output)
- `--slots 4`: Number of concurrent request slots (controls parallelism)
- `--chat-template`: Chat template format (chatml, llama2, mistral, etc.)
- `--api-key`: API key for authentication

### Start the Server (Python)

```bash
python -m llama_cpp.server \
    --model ./models/Q4_K_M.gguf \
    --host 0.0.0.0 \
    --port 8000 \
    --n_gpu_layers -1 \
    --chat_format chatml \
    --n_ctx 4096
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
        "model": "default",
        "messages": [
            {"role": "user", "content": "What is llama.cpp?"}
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
        "model": "default",
        "messages": [
            {"role": "user", "content": "Explain GGUF quantization."}
        ],
        "temperature": 0.7,
        "max_tokens": 256,
    }
)

print(response.json()["choices"][0]["message"]["content"])
```

### Using OpenAI Python Client (Recommended)

Since llama.cpp server is OpenAI-compatible, you can use the official OpenAI client:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="your-secret-key",
)

response = client.chat.completions.create(
    model="default",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is quantization in LLMs?"},
    ],
    temperature=0.7,
    max_tokens=256,
)

print(response.choices[0].message.content)
```


## Serving Custom / Fine-tuned Models
If you fine-tuned a small LLM with **Unsloth** and exported it to GGUF (e.g., `gguf_model_small`), here is how to serve it with llama.cpp.

### Option A: Serve a GGUF File Directly

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

#### Step 2: Serve with llama.cpp

```bash
./build/bin/llama-server \
    -m ./gguf_model_small/unsloth.Q4_K_M.gguf \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key \
    --chat-template chatml \
    -ngl 99 \
    -c 2048 \
    --slots 4
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
    model="default",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is fine-tuning?"},
    ],
    temperature=0.7,
    max_tokens=256,
)

print(response.choices[0].message.content)
```

### Option B: Convert from HuggingFace Format

If your model is in HuggingFace safetensors format, convert it first:

```bash
# Convert to GGUF
python convert_hf_to_gguf.py ./hf_model_small --outfile my-model-f16.gguf --outtype f16

# Quantize
./build/bin/llama-quantize my-model-f16.gguf my-model-Q4_K_M.gguf Q4_K_M

# Serve
./build/bin/llama-server \
    -m my-model-Q4_K_M.gguf \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key \
    --chat-template chatml \
    -ngl 99 \
    -c 2048
```

### Serve with LoRA Adapters

llama.cpp supports applying LoRA adapters at inference time without merging:

```bash
./build/bin/llama-server \
    -m ./models/base-model-Q4_K_M.gguf \
    --lora ./lora-adapter.gguf \
    --host 0.0.0.0 \
    --port 8000 \
    --api-key your-secret-key \
    -ngl 99
```

Then query normally:

```python
response = client.chat.completions.create(
    model="default",
    messages=[{"role": "user", "content": "Hello!"}],
)
```


## Docker Deployment
Deploy llama.cpp in a container for production environments.

### Run with Docker (CPU)

```bash
docker run -p 8000:8000 \
    -v ./models:/models \
    ghcr.io/ggerganov/llama.cpp:server \
    -m /models/Q4_K_M.gguf \
    --host 0.0.0.0 \
    --port 8000 \
    -c 4096
```

### Run with Docker (CUDA GPU)

```bash
docker run --gpus all -p 8000:8000 \
    -v ./models:/models \
    ghcr.io/ggerganov/llama.cpp:server-cuda \
    -m /models/Q4_K_M.gguf \
    --host 0.0.0.0 \
    --port 8000 \
    -ngl 99 \
    -c 4096
```

### Docker Compose

```yaml
version: '3.8'
services:
  llama-server:
    image: ghcr.io/ggerganov/llama.cpp:server-cuda
    ports:
      - "8000:8000"
    volumes:
      - ./models:/models
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
    command: >
      -m /models/Q4_K_M.gguf
      --host 0.0.0.0
      --port 8000
      -ngl 99
      -c 4096
      --slots 4
```


## Performance Optimization Tips

- **GPU offloading**: Use `-ngl 99` to offload all model layers to GPU; use a lower value for partial offloading when VRAM is limited
- **Context length**: Set `-c` to the minimum context length you need — larger context uses more memory
- **Concurrent slots**: Use `--slots N` to control how many requests can be processed in parallel
- **Quantization choice**: `Q4_K_M` is the sweet spot for most use cases; use `Q5_K_M` or `Q6_K` if quality matters more than speed
- **Memory mapping**: llama.cpp uses mmap by default, allowing models to be loaded without duplicating in RAM
- **Batch size**: Use `-b` to tune the prompt processing batch size (default 2048); larger values can speed up prompt processing
- **Flash attention**: Use `--flash-attn` to enable Flash Attention for faster inference (if supported)
- **Streaming**: Use `stream=True` for real-time token generation


## llama.cpp vs Other Serving Solutions

| Feature | llama.cpp | vLLM | Ollama | TGI |
|--------|----------|------|--------|-----|
| CPU Inference | Excellent | No | Good | No |
| GPU Inference | Good | Excellent | Good | Excellent |
| Throughput | Low-Medium | Very High | Medium | High |
| GPU Required | No | Yes | No | Yes |
| OpenAI API | Yes | Yes | Partial | Yes |
| Multi-GPU | Limited | Yes | No | Yes |
| Quantization | Extensive (GGUF) | AWQ/GPTQ | GGUF | AWQ/GPTQ |
| Ease of Use | Medium | Medium | Easy | Medium |
| Best For | Edge/CPU/Local | Production GPU | Local Dev | Production GPU |


## Conclusion
llama.cpp is the go-to solution for **flexible, hardware-efficient LLM deployment**:

- Runs on CPU, GPU, Apple Silicon, and hybrid configurations
- Supports extensive quantization for reduced memory and faster inference
- Provides an OpenAI-compatible API server for seamless integration
- Handles custom and fine-tuned models in GGUF format
- Deploys easily with Docker or as a single binary

This workflow is perfect for:

- Local development and prototyping
- Edge and embedded AI deployments
- Cost-sensitive production environments
- CPU-only server deployments
- Laptop and desktop AI applications


## Next Steps
- Combine with a RAG pipeline (LangChain + llama.cpp)
- Add load balancing with Nginx or Traefik
- Deploy on Kubernetes with mixed CPU/GPU node pools
- Monitor with Prometheus + Grafana (llama.cpp exposes `/metrics`)
- Explore speculative decoding for faster inference
- Use grammar-constrained generation for structured output (JSON mode)
