'''
This script is responsible for uploading PDF documents from the "data" folder
to Azure Search.
It extracts text from each PDF file and uploads it as a document to the specified
Azure Search index.
'''
import os
from pypdf import PdfReader
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()

search_client = SearchClient(
    endpoint=os.getenv("SEARCH_ENDPOINT"),
    index_name=os.getenv("SEARCH_INDEX"),
    credential=AzureKeyCredential(os.getenv("SEARCH_KEY"))
)


def extract_text(pdf_path):
    '''
    Function to extract text from a PDF file
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF file
    '''
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def upload_documents():
    '''
    Function to upload documents from the "data" folder to Azure Search
    '''
    docs = []
    folder = "data"
    os.makedirs(folder, exist_ok=True)

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            text = extract_text(os.path.join(folder, file))
            base_name = os.path.splitext(file)[0]  # Remove file extension for document ID
            docs.append({
                "id": base_name,  # Safe key for Azure Search
                "content": text
            })

    if docs:
        search_client.upload_documents(docs)

if __name__ == "__main__":
    upload_documents()
