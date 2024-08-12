from faster_whisper import WhisperModel


class SubtitleGenerator():

    def __init__(self) -> None:
        pass

    def transcribe_audio(self, audio_filepath, output_filepath) -> None:
        model = WhisperModel("small")
        segments, info = model.transcribe(audio_filepath, word_timestamps=True)

        language = info.language
        segments = list(segments)

        