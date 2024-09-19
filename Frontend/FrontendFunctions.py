import os
from typing import Tuple
from src.audio import WORK_DIR
from pytubefix import YouTube

carpeta_data = f"{WORK_DIR}data"
carpeta_documentos = f"{WORK_DIR}data/documents"

def update_data():
    os.makedirs(carpeta_data, exist_ok=True)
    os.makedirs(carpeta_documentos, exist_ok=True)
    clases_creadas = [archivo.split(".")[0] for archivo in os.listdir(carpeta_data) if archivo.endswith(".txt")]
    clases_descargadas = [archivo.split(".")[0] for archivo in os.listdir(carpeta_data) if archivo.endswith(".m4a")]
    clases_transcritas = [archivo.split(".")[0] for archivo in os.listdir(carpeta_documentos) if archivo.endswith(".txt")]

    return clases_creadas, clases_descargadas, clases_transcritas

def get_url_from_title(title: str) -> str:
    return open(f"{carpeta_data}/{title}.txt").read()

def comprobar_estado_clase(video_url : str) -> Tuple[bool, bool]:
    title_video = YouTube(video_url).title

    _, clases_descargadas, clases_transcritas = update_data()

    downloaded = title_video + ".m4a" in clases_descargadas
    transcribed = title_video + ".txt" in clases_transcritas
    
    return downloaded, transcribed
