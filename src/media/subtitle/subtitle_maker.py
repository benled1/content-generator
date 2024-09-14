from media.audio.audio import Audio
from media.subtitle.generators.i_subtitle_generator import ISubtitleGenerator
from .subtitle import Subtitle
from pathlib import Path
from faster_whisper import WhisperModel
from configurations.constants import SUBTITLE_STORAGE_URI

import math
import os
import uuid


class SubtitleMaker():

    def __init__(self, subtitle_generator: ISubtitleGenerator) -> None:
        self.subtitle_generator = subtitle_generator

    def make_subtitle(self, audio: Audio) -> Subtitle:
        srt: Subtitle = self.subtitle_generator.generate_subtitle(audio)
        return srt
