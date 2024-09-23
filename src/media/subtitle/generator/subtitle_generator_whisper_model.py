from .i_subtitle_generator import ISubtitleGenerator
from media.audio.audio import Audio
from media.audio.audio import Audio
from media.subtitle.subtitle import Subtitle
from uuid import UUID
from pathlib import Path
from faster_whisper import WhisperModel
from configurations.constants import TMP_DIR

import math
import os
import uuid

class AudioTranscriptionFailed(Exception):
    pass

class SubtitleGeneratorWhisperModel(ISubtitleGenerator):

    def __init__(self, model_size: str="small", output_type: str="srt") -> None:
        self.model_size = model_size
        pass

    def generate_subtitle(self, ref_audio: Audio, uuid: UUID):
        model = WhisperModel(self.model_size)
        try:
            segments, info = model.transcribe(ref_audio.uri, word_timestamps=True)
        except Exception as e:
            raise AudioTranscriptionFailed("Failed to transcribe audio.") from e

        language = info.language
        segments = list(segments)
        
        text = ""
        index = 0
        for segment in segments:
            for word in segment.words:
                word_start = self._format_srt_time(word.start)
                word_end = self._format_srt_time(word.end)
                text += f"{str(index+1)} \n"
                text += f"{word_start} --> {word_end} \n"
                new_word = word.word.replace(" ", "")
                text += f"{new_word} \n"
                text += "\n"
                index += 1

        output_file = f"{uuid}.{language}.srt"
        full_subtitle_path = self._save_subtitle(text, output_file)
        
        return Subtitle(full_subtitle_path)

    def _save_subtitle(self, text: str, subtitle_file: str) -> str:
        full_output_path = os.path.join(TMP_DIR, 'misc', 'subtitle', subtitle_file)
        with open(full_output_path, "w") as f:
            f.write(text)
        return full_output_path
    
    def _format_srt_time(self, seconds: int):
        hours = math.floor(seconds / 3600)
        seconds %= 3600
        minutes = math.floor(seconds / 60)
        seconds %= 60
        milliseconds = round((seconds - math.floor(seconds)) * 1000)
        seconds = math.floor(seconds)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"
        return formatted_time
    