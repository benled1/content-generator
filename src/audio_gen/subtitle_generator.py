import math
import os
import uuid
from faster_whisper import WhisperModel


class SubtitleGenerator():

    def __init__(self) -> None:
        pass

    def transcribe_audio(self, audio_filepath) -> None:
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

        output_file = f"{uuid.uuid4()}.{language}.srt"
        store_path = "./local_media_store/tmp_files"
        full_output_path = os.path.join(store_path, output_file)
        with open(full_output_path, "w") as f:
            f.write(text)

    def format_time(self, seconds):
        hours = math.floor(seconds / 3600)
        seconds %= 3600
        minutes = math.floor(seconds / 60)
        seconds %= 60
        milliseconds = round((seconds - math.floor(seconds)) * 1000)
        seconds = math.floor(seconds)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"
        return formatted_time