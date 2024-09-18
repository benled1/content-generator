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
- create a integration test for audio, footage, and subtitle. Basically for each test, run to make sure the files are good.
- create unit tests for each of the packages mentioned above
- during the two above, tweak code as needed if it feels off while using it.


EXTRA TODO:
- put the uuid of the file as a property in the file class for ex. Audio.uuid should be a property. This way the subtitle doesn't have to retrieve the uuid from the file name.
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
    

    

    






