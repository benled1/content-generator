from media.audio.audio_maker import AudioMaker
from media.audio.generators.text_to_speech_chat_tts import TextToSpeechChatTTS
from media.audio.generators.i_audio_generator import IAudioGenerator
from media.audio.audio import Audio
from media.subtitle.generators.i_subtitle_generator import ISubtitleGenerator
from media.subtitle.generators.subtitle_generator_whisper_model import SubtitleGeneratorWhisperModel
from media.subtitle.subtitle_maker import SubtitleMaker
from media.subtitle.subtitle import Subtitle
import uuid

"""
TODO:
- create a footage generator/maker class that will retrieve or gen footage in some way. abstract this out in the same way it was done for both subtitles and audio
- abstract away the method of uploading from the generator class. Generator should make and return the object with a reference to a local tmp file. Uploader/StorageManager should store the file
    in a more official place like s3 or a none tmp file like (local_media_store)
"""


if __name__ == "__main__":
    
    chat_tts_audio_generator: IAudioGenerator = TextToSpeechChatTTS()
    audio_maker: AudioMaker  = AudioMaker(audio_generator=chat_tts_audio_generator)
    audio: Audio = audio_maker.make_audio("This is made with a audio generator and maker.")
    whisper_model_srt_generator : ISubtitleGenerator = SubtitleGeneratorWhisperModel()
    subtitle_maker: SubtitleMaker = SubtitleMaker(whisper_model_srt_generator)
    subtitle: Subtitle = subtitle_maker.make_subtitle(audio)
    

    






