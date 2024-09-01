import uuid
from utils.audio.text_to_speech import TextToSpeech
from utils.audio.subtitle_tools import SubtitleTools

if __name__ == "__main__":
    audio_uuid = uuid.uuid4()
    text_content = "This is sample text content."
    tts = TextToSpeech()
    subtitle_tools = SubtitleTools()
    audio_path = tts.text_to_audio(text_content)
    subtitle_tools.text_to_srt(audio_path)

    






