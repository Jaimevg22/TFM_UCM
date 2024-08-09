#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:10:23 2024

@author: eduardocarreroyubero
"""

# !pip install llama-index
# !pip install llama-index-embeddings-huggingface
# !pip install llama-index-llms-ollama

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

api_key = "PONER LA TUYA"

documents = SimpleDirectoryReader("/Users/eduardocarreroyubero/Documents/GitHub/TFM_UCM/eduardo/rag_data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
# importante: installar ollama y levantar el modelo que quieras usar por linea de comandos (https://github.com/ollama/ollama?tab=readme-ov-file)
Settings.llm = Ollama(model="llama3.1", request_timeout=360.0)

index = VectorStoreIndex.from_documents(
    documents,
)

query_engine = index.as_query_engine()
question = "¿qué se va a hacer para ampliar el tratamiento EDAR de Sant Lluis?"
response = query_engine.query(question)
print(response)
# Se realizarán obras para mejorar y ampliar las infraestructuras hidráulicas en determinados municipios de las Illes Balears, incluyendo la mejora del tratamiento EDAR de Sant Lluís.

response.response

response.metadata
# {'a24a142f-3572-45ee-a99a-652e2a843da5': {'page_label': '64',
#   'file_name': 'BOE-A-2024-1569.pdf',
#   'file_path': '/Users/eduardocarreroyubero/Documents/GitHub/TFM_UCM/eduardo/rag_data/BOE-A-2024-1569.pdf',
#   'file_type': 'application/pdf',
#   'file_size': 2846212,
#   'creation_date': '2024-08-09',
#   'last_modified_date': '2024-08-02'},
#  '812d0419-726a-46fc-98ec-993b4b52cc6f': {'page_label': '29',
#   'file_name': 'BOE-A-2024-1569.pdf',
#   'file_path': '/Users/eduardocarreroyubero/Documents/GitHub/TFM_UCM/eduardo/rag_data/BOE-A-2024-1569.pdf',
#   'file_type': 'application/pdf',
#   'file_size': 2846212,
#   'creation_date': '2024-08-09',
#   'last_modified_date': '2024-08-02'}}






