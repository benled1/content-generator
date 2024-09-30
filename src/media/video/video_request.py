from uuid import UUID, uuid4
from dataclasses import dataclass 
from .video_request_enums import AudioQuality, FootageTheme, AudioFormats

class InvalidInput(Exception):
    pass

@dataclass
class VideoRequest:
    uuid: UUID = uuid4()
    footage_theme: str = "random" 
    audio_quality: str = "low"
    audio_text: str = ""
    audio_format: str = "wav"
    include_subtitles: bool = True
    subtitle_font: str = "DejaVu-Sans"

    def __post_init__(self):
        self.validate_input()
        
    def validate_input(self):
        """
        Validate the input provided to the VideoRequest.
        """
        # basic type checking
        for (name, field_type) in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                current_type = type(self.__dict__[name])
                raise TypeError(f"The field '{name}' was assigned by '{current_type}' instead of '{field_type}'")

        # enum type checking
        if AudioQuality(self.audio_quality) not in AudioQuality:
            raise InvalidInput("Video request contains invalid audio_quality.")
        if FootageTheme(self.footage_theme) not in FootageTheme:
            raise InvalidInput("Video request contains invalid footage_theme.")
        if AudioFormats(self.audio_format) not in AudioFormats:
            raise InvalidInput("Video request contains invalid audio_format.")
        if not isinstance(self.audio_text, (str, None)):
            raise InvalidInput("Video request contains invalid audio_text.")
