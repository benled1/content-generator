import random
import os
import moviepy.editor as mpe

from moviepy.video.tools.subtitles import SubtitlesClip
from media.audio import Audio, AudioFactory
from media.audio.generator import TextToSpeechChatTTS
from media.subtitle import Subtitle, SubtitleFactory
from media.subtitle.generator import SubtitleGeneratorWhisperModel
from media.footage import Footage, FootageFactory
from media.footage.store import LocalFootageStore
from .video_request import VideoRequest
from .video import Video
from .video_request_enums import AudioQuality, FootageTheme
from configurations.constants import TMP_DIR

class VideoFactory:

    def __init__(self) -> None:
        pass

    def make_video(self, video_request: VideoRequest) -> Video:
        """
        Parse the video request and create the necessary components for the video.
        """
        print(f"Starting video compilation video request = {video_request}")
        #create audio
        audio = self._create_audio(video_request=video_request)
        #create subtitles 
        subtitles = self._create_subtitles(audio=audio, video_request=video_request)
        #get footage
        footage = self._get_footage(video_request=video_request)

        # compile the video
        mpe_audio = mpe.AudioFileClip(audio.uri) # get the audio file clip
        mpe_footage = mpe.VideoFileClip(footage.uri) # get the video file clip

        # cut the footage 
        footage_start_time = random.randint(0, ((int)(mpe_footage.duration - mpe_audio.duration) + 1))
        footage_end_time = footage_start_time + mpe_audio.duration + 1
        mpe_footage = mpe_footage.subclip(footage_start_time, footage_end_time)

        # add the audio
        mpe_footage = mpe_footage.set_audio(mpe_audio)

        # generate the subtitles clip and compile the video
        text_generator = lambda txt: mpe.TextClip(txt, font=video_request.subtitle_font, fontsize=50, color="white", stroke_color="black", stroke_width=2,  size=mpe_footage.size)
        if subtitles is None:
            mpe_subtitles = None
            mpe_composite_clip = mpe_footage
        else:
            mpe_subtitles = SubtitlesClip(subtitles.uri, text_generator)
            mpe_composite_clip = mpe.CompositeVideoClip([mpe_footage, mpe_subtitles.set_position(("center", "bottom"))])

        # write out the final video
        output_video_path = os.path.join(TMP_DIR, "completed_videos", f"{video_request.uuid}.mp4")
        mpe_composite_clip.write_videofile(output_video_path)
        return Video(output_video_path)


    def _create_audio(self, video_request: VideoRequest) -> Audio:
        match AudioQuality(video_request.audio_quality):
            case AudioQuality.LOW:
                chat_tts_audio_generator = TextToSpeechChatTTS(video_request.audio_format)
                audio_factory = AudioFactory(audio_generator=chat_tts_audio_generator)
                return audio_factory.make_audio(input_data=video_request.audio_text, uuid=video_request.uuid)
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
        return subtitle_factory.make_subtitle(audio, video_request.uuid)
        
    def _get_footage(self, video_request: VideoRequest) -> Footage:
        if video_request.footage_theme == FootageTheme.RANDOM:
            footage_theme = random.choice(list(FootageTheme[1:])) #exclude the first option since it's random
        else:
            footage_theme = video_request.footage_theme
        
        # work done here to get the footage by theme from the store.
        local_footage_store = LocalFootageStore()
        footage_factory = FootageFactory(footage_store=local_footage_store)
        return footage_factory.make_footage(theme=footage_theme, uuid=video_request.uuid)
        



