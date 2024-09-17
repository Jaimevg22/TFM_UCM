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
├── data                                    # Data storage for transcriptions and other files
│   └── documents                           # Directory for document data
├── Frontend                                # Code related to the user interface
│   ├── __init__.py
│   ├── ChatBotPage.py                      # ChatBot interface
│   ├── FrontendFunctions.py                # Functions for the interface
│   ├── HomePage.py                         # Home page interface
│   └── StoragePage.py                      # Interface for viewing stored transcriptions
├── notebooks                               # Jupyter notebooks for testing and evaluation
│   ├── eval_batch_multiple_evaluations.ipynb
│   ├── eval_retriever.ipynb
│   ├── local_llama_base.ipynb
│   ├── local_llama_tools_openai.ipynb
│   └── evaluation                          # Additional evaluation notebooks for various models
│       ├── eval-plantilla-modelo-embeddings.ipynb # Template to evaluate embeddings model
│       ├── eval-plantilla-modelo-llm-v2.ipynb     # Template to evaluate llm model
│       ├── eval-all_mpnet_base_v2.ipynb
│       ├── eval-gte_qwen2_1_5b_instruct.ipynb
│       ├── eval-internlm2_chat.ipynb
│       ├── eval-internlm2.ipynb
│       ├── eval-llama3_1.ipynb
│       ├── eval-llama3_1_sauerkraut.ipynb
│       ├── eval-multi_qa_mpnet_base_dot_v1.ipynb
│       ├── eval-phi3_14b.ipynb
│       ├── eval-phi3_3b.ipynb
│       ├── eval-phi3_5_mini.ipynb
│       ├── eval-plantilla-modelo-llm-v1.ipynb
│       └── eval-stella_en_1_5B_v5.ipynb
├─── src                                     # Backend and processing logic
│   └── __init__.py
│   ├── audio.py                            # Audio handling logic
│   ├── dataset_downloader.py               # Dataset downloading utilities
│   ├── rag_querying.py                     # Functions related to RAG and Llama Index querying
│   ├── TranscriptionFunctions.py           # Functions for transcription using Whisper AI
├── environment_linux.yml                   # Conda environment for Linux systems
├── environment.yml                         # Conda environment for Windows/Mac
├── README.md                               # Project documentation (this file)
└── frontend.py                             # Main entry point for running the app with Streamlit
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

   Install [Ollama](https://github.com/ollama/ollama), which is necessary to run Llama models locally.

   After installation, run the Llama model by typing the following command in your shell:

   ```bash
   ollama run llama3.1
   ```

4. **Install FFmpeg**

   Install [FFmpeg](https://ffmpeg.org/download.html) for your operating system, which is required for audio extraction.

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
