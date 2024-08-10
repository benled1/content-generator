import ChatTTS
import torch
import torchaudio

class TTSGenerator:

    def __init__(self) -> None:
        pass

    def generate_audio_file(self, text_input: str) -> str:
        """
        Take in a text block and convert it to an audio file. Return the path to the audio file.
        """
        chat = ChatTTS.Chat()
        chat.load(compile=False)

        text = [text_input]

        wavs = chat.infer(text)
        print(wavs)
        wav_tensor = torch.from_numpy(wavs)
        print(wav_tensor)
        unsqueezed_wave_tensor = wav_tensor.unsqueeze(0)
        print(unsqueezed_wave_tensor)
        # torchaudio.save(f"test_audio.wav",)
        
        

        pass
        