from media.audio import TextToSpeechChatTTS, AudioFactory, Audio
from media.audio.generator import IAudioGenerator
from media.subtitle import SubtitleGeneratorWhisperModel, SubtitleFactory, Subtitle
from media.subtitle.generator import ISubtitleGenerator
from media.footage import LocalFootageStore, FootageFactory, Footage
from media.footage.store import IFootageStore

import uuid

"""
TODO:
- create a video_factory that will take video_request objects as input and make video objects as output.


EXTRA TODO:
- change the audio and subtitles and footage 
"""


if __name__ == "__main__":
    
    chat_tts_audio_generator: IAudioGenerator = TextToSpeechChatTTS()
    whisper_model_srt_generator : ISubtitleGenerator = SubtitleGeneratorWhisperModel()
    local_footage_store: IFootageStore = LocalFootageStore()

    audio_factory: AudioFactory  = AudioFactory(audio_generator=chat_tts_audio_generator)
    subtitle_factory: SubtitleFactory = SubtitleFactory(subtitle_generator=whisper_model_srt_generator)
    footage_factory: FootageFactory = FootageFactory(footage_store=local_footage_store)


    audio: Audio = audio_factory.make_audio("Poopoo peepee poopy pee")
    print(audio)
    subtitle: Subtitle = subtitle_factory.make_subtitle(audio)
    footage: Footage = footage_factory.make_footage("minecraft")
    print(footage)
    

    

    






