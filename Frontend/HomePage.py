import streamlit as st
from src.audio import Audio, AudioEngine
from io import BytesIO
from PIL import Image
import requests
from pytubefix import YouTube
import traceback
from Frontend.FrontendFunctions import update_data, get_id_from_video_url, comprobar_estado_clase

def home_page():

    with st.container(border=True):
            video_url = st.text_input("URL de YouTube:")
            if video_url:
                try:
                    update_data()
                    yt = YouTube(video_url)
                    downloaded, transcribed = comprobar_estado_clase(video_url)
                except:
                    st.error("No se pudo encontrar el video. Verifique la URL.")
            st.divider()
            
            col2, col3 = st.columns([1.4, 1])      
            if video_url and yt:
                try:
                    yt = YouTube(video_url)
                    
                    audio = Audio(file_name=video_url.split("=")[-1], url=video_url)
                    AudioEngine.initialize_audio(audio)
                    
                    with col2:
                        st.write(f"**Título:** {yt.title}")

                        thumbnail_url = yt.thumbnail_url
                        response = requests.get(thumbnail_url)
                        img = Image.open(BytesIO(response.content))
                        with st.container(border=True):
                            st.image(img, caption="Miniatura", use_column_width=True)
                except FileNotFoundError:
                    print("¡Debes cambiar el archivo config para que el path sea correcto!")
                except Exception as e:
                    traceback.print_exc()
                    st.error("No se pudo obtener el video. Verifique la URL.")

            # Columna 3: Botones de acción (Descargar y Transcribir)
            with col3:
                if video_url:
                    st.write("Acciones:")
            
                    with st.container(border=True):
                        if st.button("Descargar", use_container_width=True):
                            with st.spinner("Descargando video..."):
                                AudioEngine.download_audio(audio)
                                st.success("¡Video descargado!")
                        if downloaded:
                            st.success("¡Video ya descargado!")
                    st.markdown("<br>", unsafe_allow_html=True)
                    with st.container(border=True):
                        if st.button("Transcribir", use_container_width=True):
                            with st.spinner("Transcribiendo audio..."):
                                try:
                                    AudioEngine.transcribe_audio(audio)
                                    st.success("¡Transcripción completada!")
                                except Exception as e:
                                    st.error(traceback.format_exc())
                        if transcribed:
                            st.success("¡Transcripción completada!")