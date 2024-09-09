import streamlit as st
from Frontend.FrontendFunctions import update_data, get_video_url_from_id
from pytubefix import YouTube
from src.audio import Audio, AudioEngine

def storage_page():
    clases_creadas, clases_descargadas, clases_transcritas = update_data()
    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        st.markdown("<h3 style='text-align: center;'>Clases creadas:</h3>", unsafe_allow_html=True)

    with col2:
        st.markdown("<h3 style='text-align: center;'>Descargadas:</h3>", unsafe_allow_html=True)

    with col3:
        st.markdown("<h3 style='text-align: center;'>Transcritas:</h3>", unsafe_allow_html=True)

    st.divider()
    for clase_id in clases_creadas:
        with st.container(border=True):
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**Título:** {YouTube(get_video_url_from_id(clase_id)).title} [**Id**: {clase_id}]")

            with col2:
                if clase_id in clases_descargadas:
                    st.success("", icon="✅")
                else:
                    col1, col2 = st.columns([3, 1], vertical_alignment="center")
                    with col1:
                        st.error("", icon="🚨")
                    with col2:
                        btn = st.button(":material/arrow_downward:", key=f"download_{clase_id}", use_container_width=True)
                        if btn:
                            
                            AudioEngine.download_audio(Audio(file_name=clase_id, url=get_video_url_from_id(clase_id)))
                            clases_descargadas.append(clase_id)
                            st.rerun()
                    
            with col3:
                if clase_id in clases_transcritas:
                    st.success("", icon="✅")
                else:
                    st.error("", icon="🚨")
