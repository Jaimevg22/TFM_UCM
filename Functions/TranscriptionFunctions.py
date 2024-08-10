import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from AudioClass import Audio
import pickle

#Puede rentar hacer pip install flash-attn --no-build-isolation
#¿language a-priori?
#¿Mejor timestamps word o sentence?

def get_model() -> tuple: #Devuelve el modelo, el procesador, el dispositivo y el tipo de dato de torch
    
    device = "cuda:0" if torch.cuda.is_available() else "cpu" 
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = "openai/whisper-large-v3"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)
    
    processor = AutoProcessor.from_pretrained(model_id)
    
    return model, processor, device, torch_dtype

#Segun la documentación del Whisper (https://huggingface.co/openai/whisper-large-v3) existen dos formas de transcripción:

# 1. Sequential long-form 
# This algorithm uses a sliding window for buffered inference of long audio files (> 30-seconds), 
# and returns more accurate transcriptions compared to the chunked long-form algorithm.
# The sequential long-form algorithm should be used in either of the following scenarios:
# Transcription accuracy is the most important factor, and latency is less of a consideration
# You are transcribing batches of long audio files, in which case the latency of sequential is comparable to chunked, 
# while being up to 0.5% WER more accurate

# def transcribe_audio_slf(ytaudio : Audio) -> None:
    
#     if not ytaudio.downloaded:
#         raise Exception("Audio file not downloaded")
    
#     model, processor, device, torch_dtype = get_model()

#     pipe = pipeline(
#         "automatic-speech-recognition",
#         model=model,
#         tokenizer=processor.tokenizer,
#         feature_extractor=processor.feature_extractor,
#         max_new_tokens=128,
#         torch_dtype=torch_dtype,
#         device=device,
#         return_timestamps=True
#     )

#     result = pipe(ytaudio.audio_path)
    
#     ytaudio.update_transcription(result)

# 2. Chunked long-form
# large-v3 remains compatible with the Transformers chunked long-form algorithm. 
# This algorithm should be used when a single large audio file is being transcribed and the fastest possible 
# inference is required. In such circumstances, the chunked algorithm is up to 9x faster than OpenAI's 
# sequential long-form implementation (see Table 7 of the Distil-Whisper paper).
# To enable chunking, pass the chunk_length_s parameter to the pipeline. For distil-large-v3, a chunk length of 25-seconds is optimal.

def transcribe_audio(ytaudio : Audio) -> None:
    
    if not ytaudio.downloaded:
        raise Exception("Audio file not downloaded")
    
    model, processor, device, torch_dtype = get_model()

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=25,
        batch_size=16,
        torch_dtype=torch_dtype,
        device=device,
        return_timestamps=True
    )
    
    result = pipe(ytaudio.audio_path)
    
    ytaudio.update_transcription(result)
    
if __name__ == "__main__":
    # from DownloadFunctions import download_audio
    # youtube_url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
    # ytaudio = Audio(folder_name="test", url=youtube_url)
    # download_audio(ytaudio)
    # transcribe_audio_clf(ytaudio)
    
    ytaudio = Audio(folder_name="test", url="https://www.youtube.com/watch?v=jNQXAC9IVRw")
    model, processor, device, torch_dtype = get_model()
    print(ytaudio.audio_path)
    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        torch_dtype=torch_dtype,
        device=device,
        return_timestamps=True
    )

    result = pipe(r"C:\Users\Jaime\OneDrive\Escritorio\TFM_UCM\data\test\audio.mp3")