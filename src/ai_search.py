# ai_search.py

from typing import List
from azure.search.documents import SearchClient
from azure.search.documents.models import (
    VectorizedQuery,
    QueryType,
    QueryCaptionType,
    QueryAnswerType,
)
from azure_config import AzureConfig 
from azure.identity import DefaultAzureCredential
from azure.core.credentials import AzureKeyCredential

import os, uuid
# set environment variables before importing any other code
from dotenv import load_dotenv
load_dotenv()

# Initialize AzureConfig
azure_config = AzureConfig()

def retrieve_documentation(
    question: str,
    index_name: str,
    embedding: List[float],
    search_endpoint: str
) -> str:
    search_client = SearchClient(
        endpoint=azure_config.search_endpoint,
        index_name=index_name,
        credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
    )

    print(f"Search Question: {question}")
    print(f"Searchclient: {search_client}")

    vector_query = VectorizedQuery(
        vector=embedding, k_nearest_neighbors=3, fields="contentVector"
    )

    #print(f"Vector query: {vector_query}")

    try:

        results = search_client.search(
            search_text=question,
            vector_queries=[vector_query],
            query_type=QueryType.SEMANTIC,
            semantic_configuration_name="default",
            query_caption=QueryCaptionType.EXTRACTIVE,
            query_answer=QueryAnswerType.EXTRACTIVE,
            top=3
        )

        docs = [
            {
                "id": doc["id"],
                "title": doc["title"],
                "content": doc["content"],
                "url": doc["url"],
            }
            for doc in results
        ]

        print(f"Retrieved Docs: {docs}")

        return docs
    except Exception as e:
        print(f"An error occurred during search: {e}")
        return []




