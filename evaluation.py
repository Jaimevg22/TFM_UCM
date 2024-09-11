import streamlit as st
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core.evaluation import (
    FaithfulnessEvaluator,
    RelevancyEvaluator,
    CorrectnessEvaluator,
    GuidelineEvaluator,
    SemanticSimilarityEvaluator,
    DatasetGenerator
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.evaluation import BatchEvalRunner
from src.audio import WORK_DIR

# Configuración de la API Key
os.environ["OPENAI_API_KEY"] = "TU KEY"

EVALUATORS = {
    "Faithfulness": FaithfulnessEvaluator,
    "Relevancy": RelevancyEvaluator,
    "Correctness": CorrectnessEvaluator,
    "Guideline": GuidelineEvaluator,
    "Semantic": SemanticSimilarityEvaluator
}

def list_files(directory):
    """Lista los archivos en el directorio especificado."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def load_documents(files):
    """Carga documentos desde una lista de archivos."""
    documents = []
    for file in files:
        path = os.path.join(f"{WORK_DIR}/data/documents", file)
        documents.extend(SimpleDirectoryReader(input_dir=os.path.dirname(path)).load_data())
    return documents

def create_vector_index(documents, model_name):
    """Crea un índice vectorial para los documentos con el modelo especificado."""
    llm = OpenAI(temperature=0.3, model=model_name)
    splitter = SentenceSplitter(chunk_size=512)
    return VectorStoreIndex.from_documents(documents, transformations=[splitter])

def generate_dataset(documents, model_name, num_queries):
    """Genera un dataset de preguntas a partir de los documentos."""
    llm = OpenAI(temperature=0.3, model=model_name)
    dataset_generator = DatasetGenerator.from_documents(documents, llm=llm)
    return dataset_generator.generate_dataset_from_nodes(num=num_queries)

def evaluate_model(index, queries, references, evaluators):
    """Ejecuta la evaluación usando el índice vectorial y los evaluadores seleccionados."""
    runner = BatchEvalRunner(evaluators, workers=8)
    eval_results = runner.aevaluate_queries(index.as_query_engine(), queries=queries, reference=references)
    return eval_results

def main():
    st.title("Evaluación de Modelos con Streamlit")

    # Selección de documentos
    st.sidebar.header("Seleccionar Documentos")
    document_files = list_files(f"{WORK_DIR}/data/documents")
    selected_files = st.sidebar.multiselect("Seleccionar Documentos para el Dataset", document_files)
    
    # Selección del modelo del índice vectorial
    vector_model_name = st.sidebar.selectbox("Seleccionar Modelo para Índice Vectorial", ["gpt-3.5-turbo", "gpt-4"])

    # Selección del modelo de referencia
    reference_model_name = st.sidebar.selectbox("Seleccionar Modelo de Referencia", ["gpt-3.5-turbo", "gpt-4"])

    # Creación del índice vectorial
    if st.sidebar.button("Crear Índice Vectorial"):
        documents = load_documents(selected_files)
        vector_index = create_vector_index(documents, vector_model_name)
        st.sidebar.write("Índice Vectorial creado.")

    # Configuración de evaluadores
    st.sidebar.header("Configuración de Evaluadores")
    selected_evaluators = st.sidebar.multiselect(
        "Seleccionar Evaluadores",
        options=[name for name in EVALUATORS.keys()],
        default=["Faithfulness", "Relevancy"]
    )

    # Generación del dataset de evaluación
    num_queries = st.sidebar.slider("Número de Queries", min_value=1, max_value=100, value=5)
    if st.sidebar.button("Generar Dataset"):
        documents = load_documents(selected_files)
        queries = generate_dataset(documents, reference_model_name, num_queries)
        references = [None] * len(queries)  # No tenemos referencias en este caso
        st.sidebar.write(f"Dataset generado con {len(queries)} queries.")

        # Evaluación del modelo
        if st.sidebar.button("Evaluar Modelo"):
            evaluator_objects = {name: EVALUATORS[name](llm=OpenAI(model=vector_model_name)) for name in selected_evaluators}
            eval_results = evaluate_model(vector_index, queries, references, evaluator_objects)
            st.write("Resultados de la Evaluación:")
            for key, result in eval_results.items():
                st.write(f"**{key}**")
                for res in result:
                    st.write(f"- {res.response} (Score: {res.score})")

if __name__ == "__main__":
    main()