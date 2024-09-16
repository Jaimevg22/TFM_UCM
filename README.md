# TFM_UCM

TFM_UCM is a master's final project application that allows you to download audio from YouTube videos, transcribe the audio using OpenAI's Whisper AI, and then query across multiple transcriptions using a Retrieval-Augmented Generation (RAG) system powered by Llama Index. This project integrates several advanced technologies to provide a seamless experience for managing and querying transcriptions.

## Features

- **Download Audio**: Extract audio from YouTube videos.
- **Transcribe Audio**: Convert audio to text using Whisper AI.
- **Query Transcriptions**: Perform searches and queries across multiple transcriptions using RAG with Llama Index.
- **User Interface**: Access all features through a user-friendly interface built with Streamlit.

## File structure

The repository has the following file structure:
```bash
.
├── Frontend                                # Code related to the interface
│   ├── __init__.py
│   ├── ChatBotPage.py                      # ChatBot interface
│   ├── FrontendFunctions.py                # Functions for the interface
│   ├── HomePage.py                         # Home page interface
│   └── StoragePage.py                      # Downloaded and transcribed interface
├── Notebooks                               # Notebooks used for testing
│   ├── local_llama_base.ipynb
│   ├── local_llama_test_query_tool.ipynb
│   └── local_llama_tools_openai.ipynb
├── src
│   ├── __init__.py
│   ├── audio.py                            # Base classes for the backend
│   ├── rag_querying.py                     # Functions related to RAG functionality
│   └── TranscriptionFunctions.py           # Functions related to transcription functionality
├── README.md
├── config.json                             # File containing work directory path
├── frontend.py                             # Run this to launch the app
├── environment_linux.yml                   # Requirements file for Linux
└── environment.yml                         # Requirements file for Windows
```

## Installation Guide

To get started with TFM_UCM, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/TFM_UCM.git
   cd TFM_UCM
   ```

2. **Create and Activate the Conda Environment**

   Ensure you have [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed. Create the Conda environment from the provided `environment.yml` file:

   ```bash
   conda env create -f environment.yml
   ```

   Activate the environment:

   ```bash
   conda activate TFM_UCM
   ```

3. **Install Ollama**
   
   Make sure you have [Ollama](https://github.com/ollama/ollama) installed.

4. **Run the Application**

   Start Ollama with Llama3.1 from the bash or Windows Powershell.

   ```bash
   ollama run llama3.1
   ```

   Start the Streamlit application from the repo's directory:

   ```bash
   streamlit run frontend.py
   ```

   This will launch the web application, allowing you to interact with the various features.
