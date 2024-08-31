import os
import json
import pickle
from pytubefix import YouTube
from dataclasses import dataclass, field
from transformers import pipeline
from src.TranscriptionFunctions import get_model 

with open("config.json") as config_file:
    config = json.load(config_file)
    
WORK_DIR = config["work_dir"]



@dataclass
class Audio:
    folder_name: str
    url: str
    folder_path: str = field(init=False)
    audio_path: str = field(default="")
    downloaded: bool = field(default=False)
    transcription_path: str = field(default="")
    transcription: str = field(default="")

    def __post_init__(self):
        self.folder_path = rf"{WORK_DIR}/data"  # Initialize folder_path based on folder_name


class AudioEngine:
    @staticmethod
    def transcribe_audio(audio : Audio) -> None:
        
        if not audio.downloaded:
            raise Exception("Audio file not downloaded")
        
        model, processor, device, torch_dtype = get_model()

        pipe = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            max_new_tokens=128,
            chunk_length_s=25,
            batch_size=16,
            torch_dtype=torch_dtype,
            device=device,
            return_timestamps=False
        )
        
        result = pipe(audio.audio_path)["text"]
        AudioEngine.update_transcription(audio, result)

    @staticmethod
    def initialize_audio(audio: Audio) -> None:
        print(audio.folder_path)
        # Check if the folder exists
        if not os.path.exists(audio.folder_path):
            os.makedirs(audio.folder_path)  # Create the folder if it doesn't exist
            
            # Create the file that saves the URL
            with open(f"{audio.folder_path}/{audio.folder_name}.txt", "w") as url_file:
                url_file.write(audio.url)

            if not os.path.exists(f"{audio.folder_path}/documents"):
                os.makedirs(f"{audio.folder_path}/documents")
        else:
            # Read the saved URL
            folder_url = open(f"{audio.folder_path}/{audio.folder_name}.txt", "r").read()
            
            # If the saved URL is different from the current URL
            if folder_url != audio.url:
                raise Exception("Folder already exists with different URL")
            
            # Update audio path if the file exists
            if os.path.exists(f"{audio.folder_path}/{audio.folder_name}.m4a"):
                AudioEngine.update_audio_path(audio)
                
            # Update transcription if the file exists
            if os.path.exists(f"{audio.folder_path}/documents/{audio.folder_name}.txt"):
                AudioEngine.update_transcription(audio, pickle.load(open(f"{audio.folder_path}/documents/{audio.folder_name}.txt", "rb")))

    @staticmethod
    def update_audio_path(audio: Audio) -> None:
        audio.audio_path = f"{audio.folder_path}/{audio.folder_name}.m4a"
        audio.downloaded = True

    @staticmethod
    def update_transcription(audio: Audio, transcription) -> None:
        audio.transcription = transcription
        audio.transcription_path = f"{audio.folder_path}/documents/{audio.folder_name}.txt"

        # Write the transcription to a .txt file
        with open(audio.transcription_path, "w") as transcription_file:
            transcription_file.write(transcription)
        
        print(f"Transcription written to {audio.transcription_path}")

    @staticmethod
    def download_audio(audio : Audio) -> None:
        yt = YouTube(audio.url)
        stream = yt.streams.get_audio_only(subtype='mp4')
        download_path = fr"{audio.folder_path}/{audio.folder_name}.m4a"
        stream.download(filename=download_path)
        AudioEngine.update_audio_path(audio)
