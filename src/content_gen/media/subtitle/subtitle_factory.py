from content_gen.media.audio.audio import Audio
from content_gen.media.subtitle.generator import ISubtitleGenerator
from .subtitle import Subtitle
from pathlib import Path
from faster_whisper import WhisperModel
from uuid import UUID

import math
import os
import uuid


class SubtitleFactory():

    def __init__(self, subtitle_generator: ISubtitleGenerator) -> None:
        self.subtitle_generator = subtitle_generator

    def make_subtitle(self, audio: Audio, uuid: UUID) -> Subtitle:
        srt: Subtitle = self.subtitle_generator.generate_subtitle(audio, uuid)
        return srt
