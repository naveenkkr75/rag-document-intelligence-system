# 📄 RAG Document Intelligence System

A Retrieval Augmented Generation (RAG) based document question-answering system that allows users to upload documents and ask questions using natural language. The application uses LangChain, Google Gemini, ChromaDB, and Streamlit to provide accurate answers based only on the uploaded documents.

## 🚀 Live Demo

(Add your Streamlit Cloud URL here after deployment)

---

## 📌 Features

- 📂 Upload PDF, TXT, and DOCX documents
- 🔍 Semantic search using vector embeddings
- 🧠 Google Gemini LLM integration for answer generation
- 🗄️ Persistent ChromaDB vector database
- ⚡ Incremental document indexing
- 🔒 Duplicate document detection using SHA-256 hashing
- 💬 Chat-style conversational interface
- 📚 Source document references for generated answers
- 🌐 Streamlit-based interactive web application

---

## 🏗️ System Architecture
                 User
              |
              |
      Streamlit Interface
              |
              |
    Upload Documents / Query
              |
    ----------------------
    |                    |
    |                    |

Document Processing User Question
| |
| |
PDF/TXT/DOCX Loader |
| |
Chunking |
| |
Embeddings |
| |
----------- |
| |
v v
ChromaDB Vector Store
|
|
Similarity Retrieval
|
|
Context + Question
|
|
Google Gemini LLM
|
|
Final Answer

---

## 🛠️ Tech Stack

### Backend
- Python
- LangChain
- Google Gemini API
- ChromaDB

### AI/ML
- HuggingFace Sentence Transformers
- Vector Embeddings
- Retrieval Augmented Generation (RAG)

### Frontend
- Streamlit

### Document Processing
- PyPDF
- Docx2txt
- LangChain Document Loaders

---

## 📂 Project Structure
rag-document-intelligence-system/

│
├── app.py # Streamlit application
├── config.py # Configuration settings
├── requirements.txt # Dependencies
│
├── utils/
│ ├── llm.py # Gemini LLM configuration
│ ├── embeddings.py # Embedding model
│ ├── vectorstore.py # ChromaDB setup
│ ├── retriever.py # Similarity search
│ ├── indexer.py # Incremental indexing pipeline
│ ├── file_tracker.py # Duplicate file detection
│ ├── splitter.py # Text chunking
│ ├── prompts.py # RAG prompts
│ └── parser.py # Gemini response parser
│
├── data/
│ └── uploads/ # Uploaded documents
│
└── metadata/
└── indexed_files.json # Stored file hashes
## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/rag-document-intelligence-system.git

cd rag-document-intelligence-system