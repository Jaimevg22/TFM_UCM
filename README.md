# TFM_UCM

TFM_UCM is a master's final project application that allows you to download audio from YouTube videos, transcribe the audio using OpenAI's Whisper AI, and then query across multiple transcriptions using a Retrieval-Augmented Generation (RAG) system powered by Llama Index. This project integrates several advanced technologies to provide a seamless experience for managing and querying transcriptions.

## Features

- **Download Audio**: Extract audio from YouTube videos.
- **Transcribe Audio**: Convert audio to text using Whisper AI.
- **Query Transcriptions**: Perform searches and queries across multiple transcriptions using RAG with Llama Index.
- **User Interface**: Access all features through a user-friendly interface built with Streamlit.

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

3. **Run the Application**

   Start the Streamlit application from the repo's directory:

   ```bash
   streamlit run frontend.py
   ```

   This will launch the web application, allowing you to interact with the various features.

