import streamlit as st
from Frontend.FrontendFunctions import update_data, get_url_from_title
from pytubefix import YouTube
from src.audio import Audio, AudioEngine

def storage_page():
    clases_creadas, clases_descargadas, clases_transcritas = update_data()
    print("DEBUG  Clases creadas:", clases_creadas)
    print("DEBUG  Clases descargadas:", clases_descargadas)
    print("DEBUG  Clases transcritas:", clases_transcritas)
    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        st.markdown("<h3 style='text-align: center;'>Clases creadas:</h3>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h3 style='text-align: center;'>Descargadas:</h3>", unsafe_allow_html=True)

    with col3:
        st.markdown("<h3 style='text-align: center;'>Transcritas:</h3>", unsafe_allow_html=True)

    st.divider()
    for clase_title in clases_creadas:
        clase_url = get_url_from_title(clase_title)
        with st.container(border=True):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**Título:** {clase_title} [**URL**: {clase_url}]")

            with col2:
                if clase_title in clases_descargadas:
                    st.success("", icon="✅")
                else:
                    col1, col2 = st.columns([3, 1], vertical_alignment="center")
                    with col1:
                        st.error("", icon="🚨")
                    with col2:
                        btn = st.button(":material/arrow_downward:", key=f"download_{clase_title}", use_container_width=True)
                        if btn:
                            
                            AudioEngine.download_audio(Audio(file_name=YouTube(clase_url).title, url=clase_url))
                            clases_descargadas.append(clase_title)
                            st.rerun()
                    
            with col3:
                if clase_title in clases_transcritas:
                    st.success("", icon="✅")
                else:
                    st.error("", icon="🚨")
