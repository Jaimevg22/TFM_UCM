import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import pickle

def get_model() -> tuple:
    """Devuelve el modelo, el procesador, el dispositivo y el tipo de dato de torch"""
    
    device = "cuda:0" if torch.cuda.is_available() else "cpu" 
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = "openai/whisper-large-v3"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)
    
    processor = AutoProcessor.from_pretrained(model_id)
    
    return model, processor, device, torch_dtype
