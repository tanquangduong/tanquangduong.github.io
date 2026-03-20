---
title: "Run LLM Locally with Ollama"
subtitle: "From setup to deployment: run and serve local LLMs easily with Ollama"
image: /images/llm/ollama-300px.png
date: "2025-05-25"
---

**Keywords:** Ollama, Local LLM, AI deployment, llama3, mistral, phi, generative AI, on-prem AI, LLM inference

![](/images/llm/ollama-300px.png){fig-align="center" width=300}

## Introduction
Running Large Language Models (LLMs) locally is becoming a key trend for developers and companies who want **privacy, low latency, and cost control**. 

Instead of relying on external APIs and paying for hosted services, tools like **Ollama** allow you to run powerful models directly on your own computer with minimal setup. This free open-source tool ensures complete privacy, security, and zero-latency responses.

## What is Ollama?
**Ollama** is a lightweight framework designed to simplify local LLM usage. It enables you to:

* Run LLMs locally (CPU or GPU).
* Download and manage open-source models (including custom configurations and models pulled from Hugging Face).
* Serve models via a built-in local HTTP API server.
* Customize models using simple configuration files.

Supported models include hundreds of options available in the Ollama library, such as **Llama 3.1, Llama 2, Mistral, Phi, and Gemma**, as well as multimodal models that accept photos, video, and voice.

## Hardware Considerations
Since you are running these models locally, you must download the entire model to your machine. **You need to ensure you have enough disk space and RAM to load and run them**. 

For example, the massive Llama 3.1 405B model requires hundreds of gigabytes of space and RAM, which is difficult for standard machines to handle. For local environments, it is highly recommended to start with lightweight or older models (like Llama 2, Phi, Gemma 2b, or Mistral) that most computers can comfortably run.

## Installation & Verification
Installing Ollama is incredibly straightforward:

1. Go to the official website at [https://ollama.com](https://ollama.com) and click on download.
2. Select your operating system (**Windows, macOS, or Linux**) and install the application.
3. Run the desktop application; nothing will appear on your screen immediately because this simply starts a backend server running the Ollama service.

**Verify Installation:**

Open your terminal or command prompt and type:

`ollama`

`ollama --version`

If you receive an output of available commands, you have installed Ollama correctly.

## Run Your First Model
Ollama automatically downloads models the first time you run them. To start a model, simply type `ollama run` followed by the model's identifier.

For example, to run Mistral or Llama 2:

`ollama run llama2`

`ollama run mistral`

If the model isn't on your system, Ollama will pull the manifest and download it. If it is already installed, it will instantly bring up an interactive prompt where you can start chatting with the model.

**Basic Terminal Commands:**

* **Exit the chat prompt:** Type `/bye`.
* **List installed models:** Type `ollama list`.
* **Remove a model:** Type `ollama rm <model_name>`.

## Serve Models via API
Ollama automatically exposes a local HTTP API, meaning you can trigger models from curl, Postman, Python code, or custom software applications.

* If the Ollama desktop application is running, the API is automatically open in the background on **port 11434**.
* If you need to manually invoke the server from your terminal, run the command: 

    `ollama serve` 

This will run the HTTP API in your terminal instance, allowing you to view all incoming requests.

## Using Ollama in Python
You have complete control over how you interact with Ollama in code.

**Method 1: Using the `requests` library manually**

You can send POST requests directly to the local server API endpoint (`http://localhost:11434/api/chat`). You can even enable streaming mode to grab responses in real-time as the model types them out.

*Example code*

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

**Method 2: Using the official `ollama` package (Recommended)**

For a much simpler integration, use the official Python or JavaScript packages.
`pip install ollama`

*Example code:*
```python
import ollama
response = ollama.generate(model='mistral', prompt='Explain Python.')
print(response['response'])
```

## Custom Models with Modelfile
You can easily create your own customized assistants by writing a Modelfile (a simple file with no extension).

Example: Creating a Pirate Assistant

Create a file named `Modelfile` in your directory with the following syntax:

```txt
FROM llama3.2
SYSTEM "You are a pirate. Speak like a pirate and answer all questions in pirate style."
```
Open your terminal in that directory and build the model by assigning it a name and pointing to the file (-f):

`ollama create pirate-bot -f ./Modelfile`

Run your custom model:

`ollama run pirate-bot`

Now, if you say "hello", the model will respond like a pirate, for example:

```txt
"Ahoy matey! What brings ye to these waters?"
```

## Deployment Options & Performance Tips
- Use GPU (NVIDIA recommended) if available to drastically speed up processing.
- Docker / Kubernetes: You can containerize Ollama and deploy it on GPU-enabled nodes for scalable production.
- Reduce context size or use quantized models (Q4, Q5) if your machine's RAM is limited.

## Conclusion
Ollama makes running LLMs locally simple, fast, and production-ready. With just a few commands, you can download models, chat with them instantly without latency, customize their behaviors with Modelfiles, and seamlessly integrate them into your code via a local HTTP API. It is a powerful solution for building private, low-cost, and efficient AI systems.

## Next Steps
- Integrate with LangChain or LangGraph.
- Build a local RAG system (FAISS, Chroma) with your private data.
- Deploy behind a secure API gateway.
