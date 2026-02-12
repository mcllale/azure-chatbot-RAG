# 🎓 Student Helpdesk AI (Azure RAG Chatbot)

## 📌 Overview
Koketso Llale AI Resume is a Retrieval-Augmented Generation (RAG) chatbot built using **Azure OpenAI** and **Azure AI Search**.  
It provides accurate, document-based answers to related to my Curriculum Vitae. User can search for my academics, work experience, skills, and/or projects.

The purpose of this project is to demonstrates **enterprise-grade Generative AI architecture on Azure**.

---

## 🧠 Architecture
- Azure OpenAI (LLM)
- Azure AI Search (Document Retrieval)
- Azure Storage (CV in PDF)
- Streamlit UI
- Azure App Service (Deployment)

---

## ✨ Features
- Chat-based AI assistant
- Retrieval-Augmented Generation (RAG)
- Document-aware responses
- Streamlit dashboard UI
- Secure configuration using environment variables
- Cloud deployment on Azure

---

## 🏗️ System Architecture
User
│
▼
Streamlit UI
│
▼
Azure AI Search ──► Relevant Documents
│
▼
Azure OpenAI (GPT)
│
▼
AI Response

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9+
- Azure OpenAI resource
- Azure AI Search index

### Installation
```bash
git clone https://github.com/mcllale/azure_chatbot.git
cd azure_chatbot
pip install -r requirements.txt

---

# Architecture Diagram (Portfolio Version)

+-------------+
| User |
+-------------+
|
v
+-------------------+
| Streamlit UI |
| (App Service) |
+-------------------+
|
v
+-------------------+
| Azure AI Search |
| (Document Index) |
+-------------------+
|
v
+-------------------+
| Azure OpenAI GPT |
| (RAG Response) |
+-------------------+
|
v
+-------------+
| AI Answer |
+-------------+

