from llama_index.core.llama_dataset import download_llama_dataset

from llama_index.core.llama_pack import download_llama_pack
from llama_index.core import VectorStoreIndex

# download and install dependencies
rag_dataset, documents = download_llama_dataset(
    "PaulGrahamEssayDataset", "./eval_data/rag_data/paul_graham"
)

rag_dataset, documents = download_llama_dataset(
    "BlockchainSolanaDataset", "./eval_data/rag_data/Blockchain"
)

rag_dataset, documents = download_llama_dataset(
    "HistoryOfAlexnetDataset", "./eval_data/rag_data/Alexnet"
)

rag_dataset, documents = download_llama_dataset(
    "CovidQaDataset", "./eval_data/rag_data/Covid"
)

rag_dataset, documents = download_llama_dataset(
    "Llama2PaperDataset", "./eval_data/rag_data/Llama2Paper"
)

# rag_dataset, documents = download_llama_dataset(
#     "PatronusAIFinanceBenchDataset", "./eval_data/rag_data/FinanceBench"
# )

# rag_dataset, documents = download_llama_dataset(
#     "MiniMtBenchSingleGradingDataset", "./eval_data/rag_data/MtBench"
# )

# rag_dataset, documents = download_llama_dataset(
#     "MtBenchHumanJudgementDataset", "./eval_data/rag_data/HumanJudgement"
# )
