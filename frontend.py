import streamlit as st
from pytubefix import YouTube
from io import BytesIO
from PIL import Image
import requests
from src.audio import Audio, AudioEngine

st.title("Descarga y Transcripción de Videos de YouTube")

# Crear columnas para organizar los elementos horizontalmente
col1, col2, col3 = st.columns([1, 2, 1])

# Columna 1: Entrada de la URL del video
with col1:
    video_url = st.text_input("URL de YouTube:")

# Columna 2: Información del video (Título y Miniatura)
if video_url:
    try:
        yt = YouTube(video_url)
        
        audio = Audio(folder_name=video_url.split("=")[-1], url=video_url)
        AudioEngine.initialize_audio(audio)
        with col2:
            st.success("¡Video encontrado!")
            st.write(f"**Título:** {yt.title}")

            thumbnail_url = yt.thumbnail_url
            response = requests.get(thumbnail_url)
            img = Image.open(BytesIO(response.content))
            st.image(img, caption="Miniatura", use_column_width=True)
    
    except Exception as e:
        st.error("No se pudo obtener el video. Verifique la URL.")

# Columna 3: Botones de acción (Descargar y Transcribir)
with col3:
    if video_url:
        st.write("Acciones:")
        if st.button("Descargar"):
            st.write("Descargando video...")
            AudioEngine.download_audio(audio)
            st.success("¡Video descargado!")

        if st.button("Transcribir"):
            st.write("Transcribiendo video...")
            AudioEngine.transcribe_audio(audio)
            st.success("¡Transcripción completada!")
    else:
        st.write("Ingrese una URL válida.")
