import os
import json
import pickle

with open("config.json") as config_file:
    config = json.load(config_file)
    
WORK_DIR = config["work_dir"]

class Audio:
    def __init__(self, folder_name : str, url : str) -> None: 
        self.url = url 
        self.folder_path = rf"{WORK_DIR}/data/{folder_name}" #Carpeta donde se guardará la información del video
        self.audio_path = "" #Ruta del archivo de audio
        self.downloaded = False #Indica si el archivo de audio ha sido descargado
        self.transcription_path = "" #Ruta del archivo de transcripción
        self.transcription = None  #Transcripción del audio
        
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path) #Si no existe la carpeta la creamos
            
            with open(f"{self.folder_path}/url.txt", "w") as url_file: #Creamos el archivo que guarda la URL
                url_file.write(self.url)
        else:
            folder_url = open(f"{self.folder_path}/url.txt", "r").read() #Leemos la URL guardada
            
            if folder_url != self.url: #Si la URL guardada es diferente a la URL actual
                raise Exception("Folder already exists with different URL")
            
            if os.path.exists(f"{self.folder_path}/audio.m4a"):
                self.update_audio_path()
                
            if os.path.exists(f"{self.folder_path}/transcription.pkl"):
                self.update_transcription(pickle.load(open(f"{self.folder_path}/transcription.pkl", "rb")))
    
    def update_audio_path(self) -> None:
        self.audio_path = fr"{self.folder_path}/audio.m4a" #Actualizamos la ruta del archivo de audio
        self.downloaded = True #Indicamos que el archivo de audio ha sido descargado
        
    def update_transcription(self, result) -> None:
        trancription_file_path = fr"{self.folder_path}/transcription.pkl" #Ruta del archivo de transcripción
        
        pickle.dump(result, open(trancription_file_path, "wb")) #Guardamos la transcripción en un archivo
        
        self.transcription_path = trancription_file_path #Actualizamos la ruta del archivo de transcripción
        self.transcription = result #Guardamos el objeto transcripción en el objeto

def create_audio_from_folder(name : str) -> Audio:
    url = open(f"{WORK_DIR}/data/{name}/url.txt", "r").read() #Leemos la URL guardada
    audio = Audio(name, url) #Creamos un objeto Audio

    return audio
            