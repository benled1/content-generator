from .generators.i_audio_generator import IAudioGenerator
from media.utils.typing import AudioGeneratorInput, is_audio_generator_input
from media.audio.audio import Audio
from typing import Union

class AudioMaker():

    def __init__(self, audio_generator: IAudioGenerator) -> None:
        self._audio_generator = audio_generator

    def make_audio(self, input_data: AudioGeneratorInput) -> Audio:
        if not is_audio_generator_input(input_data):
            raise TypeError(f"make_audio received an invalid type {type(input_data)}")
        return self._audio_generator.generate_audio(input_data)

    