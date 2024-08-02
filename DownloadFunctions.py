from AudioClass import Audio
from pytubefix import YouTube

def download_audio(ytaudio : Audio):
    
    yt = YouTube(ytaudio.url)

    stream = yt.streams.get_audio_only()
    download_path = fr"{ytaudio.folder_path}/audio"
    stream.download(filename=download_path, mp3=True)
    ytaudio.update_audio_path()