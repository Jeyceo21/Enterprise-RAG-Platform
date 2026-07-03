<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,50:203A43,100:2C5364&height=260&section=header&text=Enterprise%20RAG%20Platform&fontSize=45&fontColor=ffffff&animation=fadeIn&fontAlignY=40"/>
</p>

<h1 align="center">
🧠 Enterprise RAG Platform
</h1>

<h3 align="center">
Enterprise-grade Retrieval-Augmented Generation (RAG) Platform for Semantic Search and AI-Powered Question Answering
</h3>

<p align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/FAISS-00599C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Sentence_Transformers-5C2D91?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge"/>
<img src="https://img.shields.io/badge/LLM-RAG-blueviolet?style=for-the-badge"/>

</p>

---

# 📖 Overview

Enterprise RAG Platform is a production-inspired Retrieval-Augmented Generation (RAG) system that enables intelligent document search and context-aware question answering using modern Large Language Models (LLMs).

Instead of relying on traditional keyword-based retrieval, the platform leverages semantic embeddings to understand the meaning behind user queries. Relevant document chunks are efficiently retrieved through FAISS vector search and passed to an LLM running locally via Ollama, enabling accurate, context-aware responses.

The project demonstrates a modular AI architecture suitable for enterprise knowledge bases, internal documentation systems, research repositories, and AI-powered assistants.

---

# 🎯 Why This Project?

Organizations manage thousands of pages of documentation, policies, technical manuals, and research papers. Traditional keyword search often fails to retrieve the most relevant information because it cannot understand semantic meaning.

This platform addresses that challenge by combining:

- Semantic document retrieval
- Dense vector search
- Retrieval-Augmented Generation (RAG)
- Large Language Models
- Modular REST APIs

The result is an AI-powered knowledge assistant capable of providing accurate answers grounded in enterprise documents.

---

# ✨ Key Features

- 🔍 Semantic Document Search
- 📄 PDF & Text Document Ingestion
- 🧠 Sentence Transformer Embeddings
- ⚡ FAISS Vector Database
- 🤖 Ollama LLM Integration
- 🚀 FastAPI REST Backend
- 💻 Streamlit User Interface
- 📚 Modular RAG Pipeline
- 🔄 Scalable Architecture
- 🔌 Easy Integration with Custom Knowledge Bases

---

# 📑 Table of Contents

- Overview
- Why This Project?
- Key Features
- AI Pipeline
- Architecture
- Screenshots
- Tech Stack
- Folder Structure
- Installation
- Usage
- API Documentation
- Performance
- Security
- Roadmap
- Contributors
- License

---

# 🧠 AI Pipeline

The application follows a Retrieval-Augmented Generation workflow:

1. User submits a query.
2. Documents are converted into semantic embeddings.
3. FAISS retrieves the most relevant document chunks.
4. Retrieved context is combined with the user query.
5. Ollama-powered LLM generates a context-aware response.
6. The response is displayed through the Streamlit interface.
