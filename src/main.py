from media.audio.audio_maker import AudioMaker
from media.audio.generators.text_to_speech_chat_tts import TextToSpeechChatTTS
from media.audio.generators.i_audio_generator import IAudioGenerator
from media.audio.audio import Audio
from media.subtitle.generators.i_subtitle_generator import ISubtitleGenerator
from media.subtitle.generators.subtitle_generator_whisper_model import SubtitleGeneratorWhisperModel
from media.subtitle.subtitle_maker import SubtitleMaker
from media.subtitle.subtitle import Subtitle
import uuid


if __name__ == "__main__":
    
    chat_tts_audio_generator: IAudioGenerator = TextToSpeechChatTTS()
    audio_maker: AudioMaker  = AudioMaker(audio_generator=chat_tts_audio_generator)
    audio: Audio = audio_maker.make_audio("This is made with a audio generator and maker.")
    whisper_model_srt_generator : ISubtitleGenerator = SubtitleGeneratorWhisperModel()
    subtitle_maker: SubtitleMaker = SubtitleMaker(whisper_model_srt_generator)
    subtitle: Subtitle = subtitle_maker.make_subtitle(audio)
    

    






