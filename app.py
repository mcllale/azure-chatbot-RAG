# Import necessary libraries
import os
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
from rag_utils import retrieve_context

# Load environment variables from .env file
load_dotenv()

# Page header configuration
st.set_page_config(
    page_title="Koketso Llale AI Resume",
    page_icon="🎓",
    layout="centered"
)
st.title("🎓 Koketso Llale AI Resume")
st.caption("Powered by Azure OpenAI + Azure AI Search (RAG)")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-01"
)
# Get user input for the question
user_question = st.text_input("Ask a question about Koketso? education, work experience, or skills")

if st.button("Ask AI") and user_question:
    with st.spinner("Searching documents and generating answer..."):
        context = retrieve_context(user_question)
        if isinstance(context, list):
            context = "\n".join(context)

        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant to answer strictly using the provided context."
                },
                {
                    "role": "user",
                    "content": f"""
You are an AI assistant answering questions about Koketso Llale's resume.
Use ONLY the information provided in the context below.
If the answer is not in the content, say: "I don't have that information in the resume."

Context:
{context}

Question:
{user_question}
"""
                }
            ]
        )

        answer = response.choices[0].message.content
        st.success("Answer")
        st.write(answer)
