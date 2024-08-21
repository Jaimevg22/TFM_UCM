from audio import Audio, AudioEngine
from rag_querying import *

# Step 1: Create an Audio object for a specific YouTube video
youtube_url = "https://www.youtube.com/watch?v=fBKJEj-b86o"  # Replace with actual YouTube video URL
audio = Audio(folder_name="example_folder", url=youtube_url)

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
directory_path = "path/to/your/documents"
query = "Your question here"
results = main(directory_path, query)

# Step 7: Save model answer for later analysis
with open(f"WORK_DIR/responses/{query[:20]}.txt", "w") as response_file:
    for item in results:
        response_file.write(f"{item}\n")
