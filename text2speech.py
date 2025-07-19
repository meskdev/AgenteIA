from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch

modelo = pipeline("text-to-speech", "microsoft/speecht5_tts", device="cuda")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

speaker_embedding = torch.tensor(embeddings_dataset[0]["xvector"]).unsqueeze(0)
# # You can replace this embedding with your own as well.

prompt = "Python is the best programming language. If you disagree, you're wrong"

speech = modelo(prompt, forward_params={"speaker_embeddings": speaker_embedding})

sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])
