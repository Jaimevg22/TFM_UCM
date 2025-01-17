import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.llms.huggingface import HuggingFaceLLM
import torch
import openai

# Si se desea utilizar el modelo de embeddings mencionado en la sección 
# 4.7.2 se necesita una API key de OpenAI, para ponerla utilizar 
# la siguiente linea
# os.environ["OPENAI_API_KEY"] = "your_api_key"
# Ahora diríjase a la línea 67 y coméntela. Settings.embel_model = .......


if torch.cuda.is_available():
    device = torch.device("cuda")
    print("GPU is available")
else:
    device = torch.device("cpu")
    print("GPU is not available, using CPU")

device = torch.device("cuda")

def create_query_engine_from_directory(directory_path: str) -> VectorStoreIndex:
    """
    Returns a query engine attached to a vector store

    Args:
        directory_path (str): Path to the directory with the documents.
    """
    if os.listdir(directory_path):
        reader = SimpleDirectoryReader(directory_path)
        documents = reader.load_data()
        index = VectorStoreIndex.from_documents(documents)
        query_engine = index.as_query_engine()
        print(f"[+] Loaded {len(documents)} docs from {directory_path}")
        return query_engine


def setup_qa_model(embedding_model: str="", 
                   ollama_model: str="", 
                   tokenizer: str="", 
                   model: str="", 
                   context_window: int=2048, 
                   max_new_tokens: int=256, 
                   temperature: float=0.1,
                   tokenizer_kwargs: dict={"max_length": 512},
                   model_kwargs: dict={"torch_dtype": torch.float16},
                   ollama_opt: bool=False) -> None:
    """
    Sets up the models used for question answering in llama- index Settings.

    Args:
        embedding_model (str): Embedding model from HuggingFace.
        ollama_model (str): Model passed to Ollama.
        tokenizer (str): Tokenizer name for HuggingFaceLLM.
        model (str): Model used for HuggingFaceLLM.
        context_window (int): The maximum number of tokens available for input.
        max_new_tokens (int): The maximum number of tokens to generate.
        temperature (float): Model variability.
        tokenizer_kwargs (dict): kwargs for the HuggingFace tokenizer.
        model_kwargs (dict): kwargs for the HuggingFaceLLM model.
        ollama_opt (bool): True for embedding + ollama; False for HuggingFaceLLM.
    """
    if ollama_opt:
        Settings.embed_model = HuggingFaceEmbedding(model_name=embedding_model)
        # Importante: installar ollama y levantar el modelo que quieras usar por linea de comandos (https://github.com/ollama/ollama?tab=readme-ov-file)
        Settings.llm = Ollama(model=ollama_model, request_timeout=360.0, device_map=device)
    else:
        Settings.llm = HuggingFaceLLM(
            context_window=context_window,
            max_new_tokens=max_new_tokens,
            generate_kwargs={"temperature": temperature, "do_sample": False},
            tokenizer_name=tokenizer,
            model_name=model,
            tokenizer_kwargs=tokenizer_kwargs,
            model_kwargs=model_kwargs
        )

def query_vector_store(index, query):
    """
    Queries the vector store.
    """
    prompt =f'''Tienes acceso a transcripciones de videos de youtube.
            Se te hará una pregunta y debes responder basándote exclusivamente en la información proporcionada en las transcripciones. Si no puedes responder la pregunta utilizando estos datos, indica que la información no está disponible.

            Responde de manera educada, estructurada y concisa cuando corresponda. Si la pregunta requiere una respuesta breve, sé claro y directo. Asegúrate de:

            No inventar información adicional ni suponer nada que no esté claramente expresado en las transcripciones.
            Responder solo utilizando la información proporcionada, sin hacer inferencias más allá del contenido.
            Estructurar la respuesta de manera clara y fácil de entender.
            Mantener un tono respetuoso y profesional en todo momento.
            
            PREGUNTA:
            {query}
            '''
    response = index.query(prompt)
    return response.response, response.metadata
