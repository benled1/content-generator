import ChatTTS
import torch
import torchaudio
import numpy as np

class _TTSGenerator:
    
    def __init__(self, store_uri: str) -> None:
        self.store_uri = store_uri 

    def text_to_wav(self, text_input: str, audio_uuid: str) -> str:
        """
        Take in a text block and convert it to an audio file. Return the path to the audio file.
        """
        chat = ChatTTS.Chat()
        chat.load(compile=True)
        wav = np.asarray(chat.infer(text_input), dtype=np.float32)
        wav_tensor = torch.from_numpy(wav).squeeze().unsqueeze(0)

        full_wav_path = f"{self.store_uri}/{audio_uuid}.wav"
        torchaudio.save(uri=full_wav_path, format="wav", src=wav_tensor, sample_rate=24000)
        return full_wav_path
        