---
title: "Fine-tuning an LLM with Unsloth and Serving with Ollama"
subtitle: "End-to-end guide: fine-tune a small model on Hugging Face with Unsloth and deploy locally with Ollama"
image: /images/llm/unsloth x ollama-300px.png
date: "2025-06-20"
---

**Keywords:** Unsloth, Ollama, fine-tuning, Hugging Face, Qwen, Alpaca dataset, LoRA, GGUF, local LLM, AI deployment

![](/images/llm/unsloth x ollama-300px.png){fig-align="center" width=300}

## Introduction
Fine-tuning your own Large Language Model (LLM) is no longer limited to large GPU clusters. With modern tools like **Unsloth** and **Ollama**, you can fine-tune a **small model on a small dataset** and run it locally on your machine.

This approach is ideal if you want:

- **Full control over your model**
- **Privacy (no external API calls)**
- **Low-cost experimentation**
- **Custom domain adaptation**

In this tutorial, we will walk through a **complete pipeline**:

1. Load a small LLM from Hugging Face  
2. Fine-tune it with Unsloth  
3. Export it to GGUF  
4. Serve it locally with Ollama  



## What is Unsloth?
**Unsloth** is an optimized framework for fine-tuning LLMs efficiently. It enables:

- Fast training (2x–5x speed improvements)
- Reduced VRAM usage (4-bit quantization)
- Easy LoRA fine-tuning
- Direct export to GGUF

## What is Ollama?
**Ollama** is a lightweight framework designed to simplify local LLM usage. It enables you to:

* Run LLMs locally (CPU or GPU).
* Download and manage open-source models (including custom configurations and models pulled from Hugging Face).
* Serve models via a built-in local HTTP API server.
* Customize models using simple configuration files.

Read this article for more details: [Run LLM Locally with Ollama](https://tanquangduong.github.io/posts/llm/Run%20LLM%20locally%20with%20Ollama.html) 


## Fine-tune LLM with Unsloth
### Model & Dataset Selection

*Model*

`unsloth/Qwen2.5-0.5B-Instruct`

*Dataset*

`yahma/alpaca-cleaned` (subset of 200 samples)



### Environment Setup

```python
!pip install -q unsloth
!pip install -q transformers datasets trl accelerate peft bitsandbytes sentencepiece
```



### Load Model

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/Qwen2.5-0.5B-Instruct",
    max_seq_length=1024,
    load_in_4bit=True,
)
```



### Add LoRA Adapters

```python
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=[
        "q_proj","k_proj","v_proj","o_proj",
        "gate_proj","up_proj","down_proj",
    ],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
)
```



### Load Dataset

```python
from datasets import load_dataset
dataset = load_dataset("yahma/alpaca-cleaned", split="train[:200]")
```



### Format Dataset

```python
def format_example(example):
    user_text = example["instruction"]
    if example["input"]:
        user_text += "\n\nInput:\n" + example["input"]

    messages = [
        {"role": "user", "content": user_text},
        {"role": "assistant", "content": example["output"]},
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
    )
    return {"text": text}

dataset = dataset.map(format_example)
```

### Fine-tuning

```python
from trl import SFTTrainer, SFTConfig

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    args=SFTConfig(
        dataset_text_field="text",
        per_device_train_batch_size=2,
        max_steps=60,
        learning_rate=2e-4,
        output_dir="outputs",
    ),
)

trainer.train()
```

### Test Model

```python
from unsloth import FastLanguageModel
FastLanguageModel.for_inference(model)

inputs = tokenizer("Explain fine-tuning simply", return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=100)

print(tokenizer.decode(outputs[0]))
```

### Save Model

```python
model.save_pretrained("lora_model")
tokenizer.save_pretrained("lora_model")
```

### Export GGUF

```python
model.save_pretrained_gguf(
    "gguf_model",
    tokenizer,
    quantization_method="q4_k_m",
)
```

### Download Model from Colab
```python
!zip -r model.zip gguf_model
```

## Run your fine-tuned model with Ollama
### Install Ollama
Download from:
[https://ollama.com](https://ollama.com)

Or via terminal:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```


### Create an Ollama Model

Folder structure:
```bash
my-model/
├── Modelfile
├── model.gguf
```



### Create Modelfile

```txt
FROM ./model.gguf

SYSTEM You are a helpful AI assistant.

PARAMETER temperature 0.7
PARAMETER num_ctx 2048
```



### Run Model

```bash
ollama create my-model -f Modelfile
ollama run my-model
```



### API Usage

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "my-model",
        "prompt": "Explain LoRA",
        "stream": False
    }
)

print(response.json()["response"])
```


## Deployment Tips

- Use quantized models (Q4/Q5) to reduce RAM usage
- Prefer GPU acceleration if available
- Keep dataset clean → quality > quantity
- Start small, then scale



## Conclusion
With Unsloth + Hugging Face + Ollama, you now have a complete local LLM pipeline:


- Fine-tune efficiently with minimal hardware
- Customize models for your use case
- Deploy locally with zero latency
- Maintain full control and privacy

This workflow is perfect for:

- Prototyping AI products
- Internal enterprise tools
- Personal AI assistants



## Next Steps
- Train on your own domain dataset (RAG + fine-tuning)
- Add tools with LangGraph agents
- Deploy behind an API gateway (FastAPI, Nginx)
- Scale with Docker + GPU servers
