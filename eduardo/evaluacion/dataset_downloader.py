#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:19:30 2024

@author: eduardocarreroyubero
"""


from llama_index.core.llama_dataset import download_llama_dataset

from llama_index.core.llama_pack import download_llama_pack
from llama_index.core import VectorStoreIndex

# download and install dependencies for benchmark dataset
rag_dataset, documents = download_llama_dataset(
    "PaulGrahamEssayDataset", "./data"
)

# download and install dependencies
rag_dataset, documents = download_llama_dataset(
    "PaulGrahamEssayDataset", "./test_rag_data/paul_graham"
)

rag_dataset, documents = download_llama_dataset(
    "PatronusAIFinanceBenchDataset", "./rag_data/FinanceBench"
)

rag_dataset, documents = download_llama_dataset(
    "BlockchainSolanaDataset", "./rag_data/Blockchain"
)

rag_dataset, documents = download_llama_dataset(
    "HistoryOfAlexnetDataset", "./rag_data/Alexnet"
)

rag_dataset, documents = download_llama_dataset(
    "CovidQaDataset", "./rag_data/Covid"
)

rag_dataset, documents = download_llama_dataset(
    "Llama2PaperDataset", "./rag_data/Llama2Paper"
)

# rag_dataset, documents = download_llama_dataset(
#     "MiniMtBenchSingleGradingDataset", "./rag_data/MtBench"
# )

# rag_dataset, documents = download_llama_dataset(
#     "MtBenchHumanJudgementDataset", "./rag_data/HumanJudgement"
# )