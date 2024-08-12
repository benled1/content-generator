import ChatTTS
import torch
import torchaudio
import numpy as np

class TTSGenerator:
    
    def __init__(self, audio_store_uri: str) -> None:
        self.audio_store_uri = audio_store_uri

    def generate_audio_file(self, text_input: str) -> str:
        """
        Take in a text block and convert it to an audio file. Return the path to the audio file.
        """
        chat = ChatTTS.Chat()
        chat.load(compile=True)

        wav = np.asarray(chat.infer(text_input), dtype=np.float32)
        print(wav)
        wav_tensor = torch.from_numpy(wav).squeeze().unsqueeze(0)
        print(wav_tensor)
        torchaudio.save(uri=f"{self.audio_store_uri}/test_audio.wav", format="wav", src=wav_tensor, sample_rate=24000)
        