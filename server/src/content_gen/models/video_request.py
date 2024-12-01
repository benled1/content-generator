from uuid import UUID, uuid4
from dataclasses import dataclass 
from pydantic import BaseModel
from ..media_generation.video.video_request_enums import AudioQuality, FootageTheme, AudioFormats

class InvalidInput(Exception):
    pass

class VideoRequest(BaseModel):
    uuid: UUID = uuid4()
    footage_theme: FootageTheme = FootageTheme.RANDOM.value
    audio_quality: AudioQuality = AudioQuality.LOW.value
    audio_text: str
    audio_format: AudioFormats = AudioFormats.WAV.value
    include_subtitles: bool = True
    subtitle_font: str = "DejaVu-Sans"

    class Config:
        use_enum_values = True
