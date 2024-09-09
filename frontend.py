import streamlit as st
from pytubefix import YouTube
from io import BytesIO
from PIL import Image
import requests
from src.audio import Audio, AudioEngine
import traceback
import os
from Frontend.HomePage import home_page
from Frontend.ChatBotPage import chat_bot
from Frontend.StoragePage import storage_page
from Frontend.FrontendFunctions import update_data, get_id_from_video_url

st.set_page_config(
    page_title="Frontend TFM",  # Cambia el título de la página
    layout="wide",  # Cambia el diseño a "wide" para ocupar todo el ancho
    page_icon=":material/home:"  # Cambia el ícono de la pestaña
)

home_tab, control_tab, chat_tab = st.tabs(["Descarga y Transcripción", "Videos Descargados", "Chat Bot"])

with home_tab:
    home_page()

with control_tab:
    storage_page()

with chat_tab:
    chat_bot()