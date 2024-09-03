from src.audio import Audio, AudioEngine
from src.rag_querying import *

# Step 1: Create an Audio object for a specific YouTube video
AudioEngine.initialize_directories()
youtube_url = "https://www.youtube.com/watch?v=5eB7yBA0utM"  # Replace with actual YouTube video URL
audio = Audio(file_name="MongoDB", url=youtube_url)

# Step 2: Initialize the audio object (creates folder, checks existing files, etc.)
AudioEngine.initialize_audio(audio)

# Step 3: Download the audio from the YouTube video
AudioEngine.download_audio(audio)

# Step 4: Transcribe the downloaded audio
try:
    AudioEngine.transcribe_audio(audio)
except Exception as e:
    print(f"An error occurred during transcription: {e}")

# Step 5: Show the transcription
print(audio.transcription)

# Step 6: Set up vector store and query the model for question answering
directory_path = audio.transcription_path
query_engine = create_query_engine_from_directory(directory_path=directory_path)
setup_qa_model(tokenizer="tinyllama-tokenizer", model="tinyllama-model")
query = "¿Qué ha sucedido con MongoDB?"
results, _ = query_vector_store(index=query_engine, query=query)

print(results)
