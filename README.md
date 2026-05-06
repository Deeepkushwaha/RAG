# AI Chatbot using RAG, LangChain & Semantic Search

## 📌 Project Overview
This project is an AI-powered chatbot built using **RAG (Retrieval-Augmented Generation)** architecture.  
The application allows users to upload **PDF** and **TXT** documents and ask questions based on the uploaded content.

The chatbot uses:
- **LangChain** for orchestration
- **Google Gemini API** for LLM responses and embeddings
- **FAISS** for semantic vector search
- **Streamlit** for the user interface

The system retrieves relevant document chunks using semantic similarity search and generates accurate context-based answers.

---

## 🚀 Features

- Upload PDF and TXT documents
- Semantic Search using vector embeddings
- RAG-based contextual question answering
- Gemini LLM integration
- FAISS vector database
- Interactive Streamlit UI
- Top-k document retrieval
- Context-aware AI responses
- Error handling for invalid or empty files

---

## 📂 Project Workflow

1. Upload PDF/TXT file
2. Load document content
3. Split document into chunks
4. Generate embeddings using Gemini
5. Store embeddings in FAISS vector database
6. Perform semantic similarity search
7. Retrieve relevant chunks
8. Generate AI response using Gemini LLM
9. Display answer in Streamlit UI

---

## 🧠 Architecture

```text
User Query
     ↓
Semantic Search (FAISS)
     ↓
Relevant Chunks Retrieval
     ↓
Gemini LLM
     ↓
Context-Based Response
```

---

## 📦 Installation

### Clone Repository

```bash
git clone <your-github-repo-link>
cd <project-folder>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variable Setup

Create a `.env` file and add your Gemini API key:

```env
gemini_key=YOUR_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📸 Supported File Types

- PDF
- TXT

---

## 💡 Key Functionalities

- Document ingestion and processing
- Semantic vector search
- Context-aware AI answering
- Prompt engineering
- Retrieval-Augmented Generation (RAG)
- Vector embedding generation

---

## 📈 Future Improvements

- Multi-document support
- Chat history memory
- Database integration
- OCR support for scanned PDFs
- Deployment on cloud platforms
- Authentication system

---

## 🎯 Resume Highlights

- Developed a RAG-based AI chatbot using LangChain and Gemini API.
- Implemented semantic search using FAISS vector database.
- Built an end-to-end document question-answering system.
- Integrated LLM-based contextual response generation.
- Created an interactive Streamlit web application.

---

## 👨‍💻 Author

**Deepak Kumar**  
MCA Student | Generative AI Enthusiast | Python Developer
