import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor
from llama_index import download_loader
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# Step 1: Load documents from the directory
def load_documents_from_directory(directory_path):
    # Using SimpleDirectoryReader to read all text files in the directory
    reader = SimpleDirectoryReader(directory_path)
    documents = reader.load_data()
    return documents

# Step 2: Create the vector store index using Llama Index
def create_vector_store(documents):
    index = GPTVectorStoreIndex.from_documents(documents)
    return index

# Step 3: Load a model and tokenizer from Hugging Face for question answering
def load_qa_model(model_name="deepset/roberta-base-squad2"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
    return qa_pipeline

# Step 4: Query the vector store for relevant documents
def query_vector_store(index, query):
    response = index.query(query)
    return response

# Step 5: Extract specific information using the Hugging Face QA model
def extract_information(qa_pipeline, query, documents):
    answers = []
    for doc in documents:
        context = doc.text
        answer = qa_pipeline(question=query, context=context)
        answers.append(answer['answer'])
    return answers

# Main Function
def main(directory_path, query):
    # Load documents from directory
    documents = load_documents_from_directory(directory_path)
    
    # Create vector store index
    index = create_vector_store(documents)
    
    # Load the Hugging Face model and tokenizer for QA
    qa_pipeline = load_qa_model()
    
    # Query the vector store
    relevant_docs = query_vector_store(index, query)
    
    # Extract specific information from relevant documents
    extracted_info = extract_information(qa_pipeline, query, relevant_docs)
    
    print("Extracted Information:")
    for idx, info in enumerate(extracted_info):
        print(f"Answer {idx+1}: {info}")

    return extracted_info

# Example usage
if __name__ == "__main__":
    directory_path = "path/to/your/documents"
    query = "Your question here"
    main(directory_path, query)
