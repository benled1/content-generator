from config.constants import AUDIO_STORAGE_URI
import ChatTTS
import torch
import torchaudio
import numpy as np

class AudioSaveFailed(Exception):
    pass

class _TTSBuilder:

    def __init__(self) -> None:
        pass

    def text_to_audio(self, content: str, audio_path: str) -> str:

        chat = ChatTTS.Chat()
        chat.load(compile=True)
        audio = np.asarray(chat.infer(content), dtype=np.float32)
        audio_tensor = torch.from_numpy(audio).squeeze().unsqueeze(0)

        try:
            torchaudio.save(uri=AUDIO_STORAGE_URI, format="wav", src=audio_tensor, sample_rate=24000)
        except Exception as e:
            raise AudioSaveFailed(e)
        return AUDIO_STORAGE_URI


