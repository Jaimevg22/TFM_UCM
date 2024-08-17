from audio import Audio, AudioEngine

# Step 1: Create an Audio object for a specific YouTube video
youtube_url = "https://www.youtube.com/watch?v=example_video_id"  # Replace with actual YouTube video URL
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

# Step 5: 
