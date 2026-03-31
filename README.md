# 🤖 GenAI RAG Chatbot (Document Q&A System)

## 📌 Overview

The **GenAI RAG Chatbot** is an intelligent document question-answering system that allows users to upload PDF documents and ask contextual questions.
It uses **Retrieval-Augmented Generation (RAG)** to fetch relevant content and generate accurate answers using Large Language Models.

---

## 🚀 Features

* 📄 Upload and process PDF documents
* 🔍 Semantic search using vector embeddings
* 🧠 Context-aware question answering
* ⚡ Fast retrieval using FAISS vector database
* 💻 Interactive UI built with Streamlit

---

## 🛠️ Tech Stack

* Python
* LangChain
* FAISS (Vector Database)
* OpenAI API
* Streamlit
* PyPDF

---

## 🧩 How It Works

1. 📥 User uploads a PDF document
2. ✂️ Text is split into smaller chunks
3. 🔢 Text is converted into embeddings (vector format)
4. 🗂️ Stored in FAISS vector database
5. ❓ User asks a question
6. 🔎 Relevant chunks are retrieved
7. 🤖 LLM generates a contextual answer

---

## 📂 Project Structure

```
rag_chatbot/
│── app.py
│── loader.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/GenAI-RAG-Chatbot.git
cd GenAI-RAG-Chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Set your OpenAI API key in `app.py`:

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Demo

* Upload a PDF
* Ask questions like:

  * "What is the main topic?"
  * "Summarize this document"

---

## 💡 Future Improvements

* Support multiple file uploads
* Add chat history memory
* Use local LLM (offline mode)
* Improve UI/UX design

---

## 🎯 Use Cases

* 📚 Study materials Q&A
* 📑 Research paper analysis
* 🏢 Company document assistant
* ⚖️ Legal document understanding

---

## 👨‍💻 Author

**Abdul Rahuman S**

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

---
