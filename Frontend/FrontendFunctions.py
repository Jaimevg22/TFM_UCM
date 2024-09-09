import os
from typing import Tuple

def update_data():
    carpeta_data = r"data"
    carpeta_documentos = r"data/documentos"
    os.makedirs(carpeta_data, exist_ok=True)
    os.makedirs(carpeta_documentos, exist_ok=True)
    clases_creadas = [archivo.split(".")[0] for archivo in os.listdir(carpeta_data) if archivo.endswith(".txt")]
    clases_descargadas = [archivo.split(".")[0] for archivo in os.listdir(carpeta_data) if archivo.endswith(".m4a")]
    clases_transcritas = [archivo.split(".")[0] for archivo in os.listdir(carpeta_documentos) if archivo.endswith(".txt")]

    return clases_creadas, clases_descargadas, clases_transcritas

def get_id_from_video_url(video_url : str) -> str:
    return video_url.split("=")[-1]

def get_video_url_from_id(id_video : str) -> str:
    return f"https://www.youtube.com/watch?v={id_video}"

def comprobar_estado_clase(video_url : str) -> Tuple[bool, bool]:
    id_video = get_id_from_video_url(video_url)

    _, clases_descargadas, clases_transcritas = update_data()

    downloaded = id_video + ".m4a" in clases_descargadas
    transcribed = id_video + ".txt" in clases_transcritas
    
    return downloaded, transcribed





