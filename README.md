# 🧠 Local AI Agent Lab

This repository marks the beginning of a personal project aimed at **building a fully functional artificial intelligence agent using local LLM models**, without relying on any subscription-based or pay-per-use services.

## 🎯 Objective

To explore and develop an architecture capable of running language models **autonomously and locally**, allowing queries or interactions through an API (FastAPI) without needing to connect to commercial services like OpenAI, Anthropic, or similar platforms.

The focus is entirely on **zero subscription cost**, using only infrastructure under our control (e.g., local servers, Docker containers, VPS, etc.).

## 🧩 Technologies to be used

- **FastAPI**: to expose the model as a web service (REST API).
- **Transformers / Hugging Face**: to work with open-source LLMs.
- **Local models**: GPT2, GPT4All, Mistral, LLaMA.cpp, etc.
- **Docker**: for containerization and easy deployment.
- **(Optional)** LangChain, Ollama, LlamaIndex, or other complementary agent tools.

## 💡 Why this project?

Because access to language models shouldn’t be exclusively tied to commercial platforms. This project aims to:

- Have **full control over models and data**.
- **Avoid recurring costs** from token-based APIs or monthly plans.
- Learn how to self-host, serve, and scale LLMs.
- Create a foundation for future intelligent assistants, chatbots, autonomous agents, or integrations.

## 🚧 Project status

🟡 In early development. Currently testing first prototypes using FastAPI and local GPT2.

Next steps:
- [ ] Load models from disk and avoid runtime downloads
- [ ] Expose working `/chat` endpoint
- [ ] Dockerize the API
- [ ] Test with more powerful local models

## 📁 Expected project structure

