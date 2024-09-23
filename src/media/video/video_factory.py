import random

from media.audio import Audio, AudioFactory
from media.audio.generator import TextToSpeechChatTTS
from media.subtitle import Subtitle, SubtitleFactory
from media.subtitle.generator import SubtitleGeneratorWhisperModel
from media.footage import Footage, FootageFactory
from media.footage.store import LocalFootageStore
from .video_request import VideoRequest
from .video import Video
from .video_request_enums import AudioQuality, FootageTheme

class VideoFactory:

    def __init__(self) -> None:
        pass

    def make_video(self, video_request: VideoRequest) -> Video:
        """
        Parse the video request and create the necessary components for the video.
        """
        #create audio
        audio = self._create_audio(video_request=video_request)
        #create subtitles 
        if audio is not None:
            subtitles = self._create_subtitles(audio=audio, video_request=video_request)
        #get footage
        footage = self._get_footage(video_request=video_request)

        # compile the video
        


    def _create_audio(self, video_request: VideoRequest) -> Audio:
        if not video_request.include_audio:
            return None
        match video_request.audio_quality:
            case AudioQuality.LOW:
                chat_tts_audio_generator = TextToSpeechChatTTS()
                audio_factory = AudioFactory(audio_generator=chat_tts_audio_generator)
                return audio_factory.make_audio(video_request.audio_text)
            case AudioQuality.MEDIUM:
                print("AudioQuality.MEDIUM case is not yet implemented.")
                return None
            case AudioQuality.HIGH:
                print("AudioQuality.HIGH case is not yet implemented.")
                return None
        return 

    def _create_subtitles(self, audio: Audio, video_request: VideoRequest) -> Subtitle:
        if not video_request.include_subtitles:
            return None
        whisper_generator = SubtitleGeneratorWhisperModel()
        subtitle_factory = SubtitleFactory(subtitle_generator=whisper_generator)
        return subtitle_factory.make_subtitle(audio)
        
    def _get_footage(self, video_request: VideoRequest) -> Footage:
        if video_request.footage_theme == FootageTheme.RANDOM:
            footage_theme = random.choice(list(FootageTheme[1:])) #exclude the first option since it's random
        else:
            footage_theme = video_request.footage_theme
        
        # work done here to get the footage by theme from the store.
        local_footage_store = LocalFootageStore()
        return local_footage_store.get_footage(query=footage_theme)
        



