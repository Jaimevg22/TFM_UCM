from AudioClass import Audio
from pytubefix import YouTube

def download_audio(ytaudio : Audio):
    
    yt = YouTube(ytaudio.url)

    stream = yt.streams.get_audio_only(subtype='mp4')
    download_path = fr"{ytaudio.folder_path}/audio.m4a"
    stream.download(filename=download_path)
    ytaudio.update_audio_path()
    
if __name__ == "__main__":
    ytaudio = Audio(folder_name="test", url="https://www.youtube.com/watch?v=Y8x3cY8xN1c")
    download_audio(ytaudio=ytaudio)