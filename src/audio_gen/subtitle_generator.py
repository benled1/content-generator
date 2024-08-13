import math
import os
import uuid
from faster_whisper import WhisperModel


class _SubtitleGenerator():

    def __init__(self, store_uri) -> None:
        self.store_uri = store_uri

    def text_to_srt(self, audio_filepath: str, audio_uuid: str) -> str:
        model = WhisperModel("small")
        segments, info = model.transcribe(audio_filepath, word_timestamps=True)

        language = info.language
        segments = list(segments)

        text = ""
        index = 0

        for segment in segments:
            for word in segment.words:
                word_start = self.format_time(word.start)
                word_end = self.format_time(word.end)
                text += f"{str(index+1)} \n"
                text += f"{word_start} --> {word_end} \n"
                new_word = word.word.replace(" ", "")
                text += f"{new_word} \n"
                text += "\n"
                index += 1

        output_file = f"{audio_uuid}.{language}.srt"
        full_output_path = os.path.join(self.store_uri, output_file)
        with open(full_output_path, "w") as f:
            f.write(text)

        return full_output_path

    def format_time(self, seconds: int):
        hours = math.floor(seconds / 3600)
        seconds %= 3600
        minutes = math.floor(seconds / 60)
        seconds %= 60
        milliseconds = round((seconds - math.floor(seconds)) * 1000)
        seconds = math.floor(seconds)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"
        return formatted_time