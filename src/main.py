from media.audio.audio_maker import AudioMaker
from media.audio.generators.text_to_speech_chat_tts import TextToSpeechChatTTS
from media.audio.generators.i_audio_generator import IAudioGenerator
from media.audio.audio import Audio
import uuid


if __name__ == "__main__":
    
    chat_tts_audio_generator: IAudioGenerator = TextToSpeechChatTTS()
    audio_maker: AudioMaker  = AudioMaker(audio_generator=chat_tts_audio_generator)
    audio: Audio = audio_maker.make_audio("This is made with a audio generator and maker.")
    

    






