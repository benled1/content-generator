import uuid
from .subtitle_generator import _SubtitleGenerator
from .tts_generator import _TTSGenerator

class AudioGenerator():

    def __init__(self) -> None:
        self.subtitle_generator = _SubtitleGenerator("./local_media_store/subtitles")
        self.tts_generator = _TTSGenerator("./local_media_store/audio")

    def generate_audio(self, text_input):
        audio_uuid = uuid.uuid4()
        wav_file = self.tts_generator.text_to_wav(text_input=text_input, audio_uuid=audio_uuid)
        srt_file = self.subtitle_generator.text_to_srt(audio_filepath=wav_file, audio_uuid=audio_uuid)
        return wav_file, srt_file 
