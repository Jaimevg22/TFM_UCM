# TFM_UCM

TFM_UCM is a master's final project application that allows you to download audio from YouTube videos, transcribe the audio using OpenAI's Whisper AI, and then query across multiple transcriptions using a Retrieval-Augmented Generation (RAG) system powered by Llama Index. This project integrates several advanced technologies to provide a seamless experience for managing and querying transcriptions.

## Features

- **Download Audio**: Extract audio from YouTube videos.
- **Transcribe Audio**: Convert audio to text using Whisper AI.
- **Query Transcriptions**: Perform searches and queries across multiple transcriptions using RAG with Llama Index.
- **User Interface**: Access all features through a user-friendly interface built with Streamlit.

## File Structure

The repository has the following file structure:

```bash
.
├── Frontend                                # Code related to the user interface
│   ├── __init__.py
│   ├── ChatBotPage.py                      # ChatBot interface
│   ├── FrontendFunctions.py                # Functions for the interface
│   ├── HomePage.py                         # Home page interface
│   ├── StoragePage.py                      # Interface for viewing stored transcriptions
│   └── TestPage.py                         # Test page interface
├── notebooks                               # Jupyter notebooks for testing and evaluation
│   ├── eval_batch_multiple_evaluations.ipynb
│   ├── eval_retriever.ipynb
│   ├── local_llama_base.ipynb
│   ├── local_llama_test_query_tool.ipynb
│   ├── local_llama_tools_openai.ipynb
│   ├── starter_llamaindex_local.py
│   └── starter_llamaindex_openai.py
├── src                                     # Backend and processing logic
│   ├── __init__.py
│   ├── audio.py                            # Audio handling logic
│   ├── dataset_downloader.py               # Dataset downloading utilities
│   ├── DownloadFunctions.py                # Functions to download audio from YouTube
│   ├── rag_querying.py                     # Functions related to RAG and Llama Index querying
│   └── TranscriptionFunctions.py           # Functions for transcription using Whisper AI
├── frontend.py                             # Main entry point for running the app with Streamlit
├── environment.yml                         # Requirements file for Windows/Mac
├── environment_linux.yml                   # Requirements file for Linux
└── README.md                               # Project documentation (this file)
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

   For Linux systems, use the `environment_linux.yml` file instead:

   ```bash
   conda env create -f environment_linux.yml
   ```

   After creating the environment, activate it:

   ```bash
   conda activate TFM_UCM
   ```

3. **Install Ollama**

   Install [Ollama](https://github.com/ollama/ollama), this is necessary to run Llama models locally.

   Next, run the chosen Llama model locally. To do this type the following command in the PowerShell:

   ```bash
   ollama run llama3.1
   ```

4. **Install FFmpeg**

   Install [FFmpeg](https://ffmpeg.org/download.html) for your operating system.

5. **Run the Application**

   Start the Streamlit application from the root directory:

   ```bash
   streamlit run frontend.py
   ```

   This will launch the web application, allowing you to interact with the YouTube audio downloader, transcription tool, and RAG-based query system.

## Usage

1. **Download Audio**: Input the URL of the YouTube video to download the audio.
2. **Transcribe Audio**: The app will transcribe the audio using Whisper AI.
3. **Query Transcriptions**: Use the RAG-based search functionality to query across the transcriptions.
