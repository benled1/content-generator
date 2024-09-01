from configurations.constants import AUDIO_STORAGE_URI
import ChatTTS
import torch
import torchaudio
import numpy as np
import uuid
import os

class _AudioSaveFailed(Exception):
    pass
class _TTSInferFailed(Exception):
    pass

class TextToSpeech:
    """
    Turns text content to audio files.
    """

    def __init__(self, audio_format:str="wav") -> None:
        self.audio_format=audio_format
        self.sample_rate=24000

    def text_to_audio(self, content: str) -> str:
        chat = ChatTTS.Chat()
        chat.load(compile=True)

        try:
            audio = np.asarray(chat.infer(content), dtype=np.float32)
        except Exception as e:
            raise _TTSInferFailed("Failed to infer audio from text.") from e

        audio_tensor = torch.from_numpy(audio).squeeze().unsqueeze(0)

        try:
            audio_path = os.path.join(AUDIO_STORAGE_URI, f"{uuid.uuid4()}.{self.audio_format}")
            torchaudio.save(uri=audio_path, format=self.audio_format, src=audio_tensor, sample_rate=self.sample_rate)
        except Exception as e:
            raise _AudioSaveFailed("Failed to save audio to file.") from e
        return audio_path
    

