# 🎓 Koketso Llale AI chatbot (Azure RAG Chatbot)

## 📌 Overview
Koketso Llale AI Resume is a Retrieval-Augmented Generation (RAG) chatbot built using **Azure OpenAI** and **Azure AI Search**.  
It provides accurate, document-based answers to related to my Curriculum Vitae. User can search for my academics, work experience, skills, and/or projects.

The purpose of this project is to demonstrates **enterprise-grade Generative AI architecture on Azure**, therefore it is not deployed.

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
- 
### Streamlit User Interface
![alt text](https://github.com/mcllale/azure-chatbot-RAG/images/capture.png "Streamlit User Interface")
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

### How to run
This project is for practical use of RAG. You will need Azure account, on Azure portal:   
- Create Azure OpenAI and Azure AI Serach services (Region must be the same for both services)
- Get both endpoints(URLs) and keys for both services
- Copy and paste them in .env accordingly
  
```bash
git clone https://github.com/mcllale/azure-chatbot-RAG.git
cd azure-chatbot-RAG
pip install -r requirements.txt
python upload_documents.py
streamlit run app.py

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


