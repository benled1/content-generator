from .generator import IAudioGenerator
from media.audio.audio import Audio
from typing import Union
from uuid import UUID

class AudioFactory():

    def __init__(self, audio_generator: IAudioGenerator) -> None:
        self._audio_generator = audio_generator

    def make_audio(self, input_data: str, uuid: UUID) -> Audio:
        return self._audio_generator.generate_audio(input_data)

    