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
    """
    Represents an audio file along with its associated metadata and paths.

    Attributes:
        file_name (str): The name of the audio file.
        url (str): The URL from which the audio is sourced.
        folder_path (str): The directory path where audio files and transcriptions are stored.
        audio_path (str): The full file path to the downloaded audio file.
        downloaded (bool): A flag indicating whether the audio file has been downloaded.
        transcription_path (str): The full file path to the transcribed text file.
        transcription (str): The transcription of the audio file.
        transcribed (bool): A flag indicating whether the audio file has been transcribed.
    """
    file_name: str
    url: str
    folder_path: str = field(init=False)
    audio_path: str = field(default="")
    downloaded: bool = field(default=False)
    transcription_path: str = field(default="")
    transcription: str = field(default="")
    transcribed: bool = field(default=False)

    def __post_init__(self):
        """
        Initializes the folder path for storing audio and transcription files.
        """
        self.folder_path = rf"{WORK_DIR}/data"  # Initialize folder_path based on file_name


class AudioEngine:
    """
    A utility class for managing audio files, including downloading, transcribing,
    and handling file paths and storage.

    Methods:
        initialize_directories() -> None:
            Creates the directories where audio files, URLs, and transcriptions are stored.
        
        transcribe_audio(audio: Audio) -> None:
            Transcribes the given audio file and saves the transcription to the appropriate directory.
        
        initialize_audio(audio: Audio) -> None:
            Initializes the audio file by checking its download and transcription status, 
            and setting the appropriate paths.
        
        update_audio_path(audio: Audio) -> None:
            Updates the path to the audio file after it has been downloaded.
        
        update_transcription(audio: Audio, transcription: str) -> None:
            Updates the transcription content and saves it to the appropriate directory.
        
        download_audio(audio: Audio) -> None:
            Downloads the audio file from the given URL and saves it locally.
    """


    @staticmethod
    def initialize_directories() -> None:
        """
        Creates the directories where audio files, URLs, and transcriptions are stored.
        If the directories do not exist, they are created.
        """
        if not os.path.exists(rf"{WORK_DIR}/data"):
            os.makedirs(rf"{WORK_DIR}/data")  # Create the folder if it doesn't exist
        if not os.path.exists(rf"{WORK_DIR}/data/documents"):
            os.makedirs(rf"{WORK_DIR}/data/documents")


    @staticmethod
    def transcribe_audio(audio : Audio) -> None:
        """
        Transcribes the given audio file and saves the transcription to the appropriate directory.

        Args:
            audio (Audio): The audio object containing the file to be transcribed.

        Raises:
            Exception: If the audio file has not been downloaded.
        """
        if not audio.transcribed:
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
        """
        Initializes the audio file by checking its download and transcription status,
        and setting the appropriate paths.

        Args:
            audio (Audio): The audio object to initialize.

        Raises:
            Exception: If a folder with the same name exists but with a different URL.
        """
        if not os.path.exists(f"{audio.folder_path}/{audio.file_name}.txt"):
            # Create the file that saves the URL
            with open(f"{audio.folder_path}/{audio.file_name}.txt", "w") as url_file:
                url_file.write(audio.url)
        else:
            # Read the saved URL
            file_url = open(f"{audio.folder_path}/{audio.file_name}.txt", "r").read()
            
            # If the saved URL is different from the current URL
            if file_url != audio.url:
                raise Exception("File already exists with different URL")
            audio.url = file_url
            
            # Update audio path if the file exists
            if os.path.exists(f"{audio.folder_path}/{audio.file_name}.m4a"):
                AudioEngine.update_audio_path(audio)
                
            # Update transcription if the file exists
            if os.path.exists(f"{audio.folder_path}/documents/{audio.file_name}.txt"):
                AudioEngine.update_transcription(audio, pickle.load(open(f"{audio.folder_path}/documents/{audio.file_name}.txt", "rb")))


    @staticmethod
    def update_audio_path(audio: Audio) -> None:
        """
        Updates the path to the audio file after it has been downloaded.

        Args:
            audio (Audio): The audio object whose path is to be updated.
        """
        audio.audio_path = f"{audio.folder_path}/{audio.file_name}.m4a"
        audio.downloaded = True


    @staticmethod
    def update_transcription(audio: Audio, transcription) -> None:
        """
        Updates the transcription content and saves it to the appropriate directory.

        Args:
            audio (Audio): The audio object to update.
            transcription (str): The transcription text to be saved.
        """
        audio.transcription = transcription
        audio.transcription_path = f"{audio.folder_path}/documents/{audio.file_name}.txt"

        # Write the transcription to a .txt file
        with open(audio.transcription_path, "w") as transcription_file:
            transcription_file.write(transcription)
        
        audio.transcribed = True
        print(f"Transcription written to {audio.transcription_path}")


    @staticmethod
    def download_audio(audio : Audio) -> None:
        """
        Downloads the audio file from the given URL and saves it locally.

        Args:
            audio (Audio): The audio object representing the file to download.
        """
        yt = YouTube(audio.url)
        stream = yt.streams.get_audio_only(subtype='mp4')
        download_path = fr"{audio.folder_path}/{audio.file_name}.m4a"
        stream.download(filename=download_path)
        AudioEngine.update_audio_path(audio)
