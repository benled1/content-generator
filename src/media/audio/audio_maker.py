from .generators.i_audio_generator import IAudioGenerator
from media.audio.audio import Audio
from typing import Union

class AudioMaker():

    def __init__(self, audio_generator: IAudioGenerator) -> None:
        self._audio_generator = audio_generator

    def make_audio(self, input_data: str) -> Audio:
        return self._audio_generator.generate_audio(input_data)

    