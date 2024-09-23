from configurations.constants import TMP_DIR
from . import IAudioGenerator
from media.audio.audio import Audio
from uuid import UUID

import ChatTTS
import torch
import torchaudio
import numpy as np
import os

class _AudioSaveFailed(Exception):
    pass
class _TTSInferFailed(Exception):
    pass

"""
NOTE:
Create an AudioMaker and then have that inherit some backend generator like this one.
Then the AudioMaker will have some generic interface like make_audio() that will call
the TextToSpeech class (or whatever backend you give it). 
IMPORTANT!@!!!!!! ^^^^^^^
"""

class TextToSpeechChatTTS(IAudioGenerator):
    """
    Turns text content to audio files using ChatTTS as a local model.
    """

    def __init__(self, audio_format: str="wav") -> None:
        self.audio_format=audio_format
        self.sample_rate=24000

    def generate_audio(self, text: str, uuid: UUID) -> Audio:
        chat = ChatTTS.Chat()
        chat.load(compile=True)

        try:
            audio = np.asarray(chat.infer(text), dtype=np.float32)
        except Exception as e:
            raise _TTSInferFailed("Failed to infer audio from text.") from e

        audio_tensor = torch.from_numpy(audio).squeeze().unsqueeze(0)

        try:
            audio_path = os.path.join(TMP_DIR, "misc", "audio", f"{uuid}.{self.audio_format}")
            self._save_audio(audio_path, audio_tensor)
        except Exception as e:
            raise _AudioSaveFailed("Failed to save audio to file.") from e

        audio_object: Audio = Audio(uri=audio_path)
        return audio_object
    
    def _save_audio(self, audio_path: str, audio_tensor) -> None:
        torchaudio.save(uri=audio_path, format=self.audio_format, src=audio_tensor, sample_rate=self.sample_rate)

    

