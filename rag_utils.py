'''
This module contains utility functions for retrieving context from
Azure Search based on user queries.
'''
import os
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv()
# Initialize Azure Search client
search_client = SearchClient(
    endpoint=os.getenv("SEARCH_ENDPOINT"),
    index_name=os.getenv("SEARCH_INDEX"),
    credential=AzureKeyCredential(os.getenv("SEARCH_KEY"))
)


def retrieve_context(query):
    '''
    Function to retrieve context from Azure Search based on user query

    Args:
        query (str): The user's question or query

    Returns:
        str: Retrieved context from Azure Search
    '''
    results = search_client.search(
        search_text=query,
        search_fields=["content"],
        top=5
    )
    context = ""
    for result in results:
        context += result.get("content", "") + "\n"
    return context.strip()
