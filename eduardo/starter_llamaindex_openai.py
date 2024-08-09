#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:10:23 2024

@author: eduardocarreroyubero
"""

# !pip install llama-index

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_graph_from_storage

api_key = "sk-3FZTo5iM5Ch0w4yOjE8-zq4NHGmIR7MWTUCd0MIXuKT3BlbkFJ3b28Vv3B6YNmg_7BK1fkAld1Mw9cuvnis6LdzXYsMA"

llm_model = OpenAI(
    model='gpt-3.5-turbo',
    api_key=api_key,
    temperature=0.7
)

embeddings_model = OpenAIEmbedding(
    model="text-embedding-ada-002",
    api_key=api_key
)

Settings.llm = llm_model
Settings.embed_model = embeddings_model

documents = SimpleDirectoryReader("/Users/eduardocarreroyubero/Documents/GitHub/TFM_UCM/eduardo/rag_data").load_data()

# documents[0]
# len(documents)

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

question = "¿qué se va a hacer para ampliar el tratamiento EDAR de Sant Lluis?"
response = query_engine.query(question)
print(response)

response.response
response.metadata







