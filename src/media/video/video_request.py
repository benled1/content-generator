from uuid import UUID, uuid4
from dataclasses import dataclass 
from .video_request_enums import AudioQuality, FootageTheme

class InvalidInput(Exception):
    pass

@dataclass
class VideoRequest:
    uuid: UUID = uuid4()
    footage_theme: str = "random" 
    audio_quality: str = "low"
    audio_text: str = ""
    include_audio: bool = True
    include_subtitles: bool = True

    def __post_init__(self):
        self.validate_input()
        
    def validate_input(self):
        """
        Validate the input provided to the VideoRequest.
        """
        #basic type checking
        for (name, field_type) in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                current_type = type(self.__dict__[name])
                raise TypeError(f"The field '{name}' was assigned by '{current_type}' instead of '{field_type}'")

        #enum type checking
        if AudioQuality(self.audio_quality) not in AudioQuality:
            raise InvalidInput("Video request contains invalid audio_quality.")
        if FootageTheme(self.footage_theme) not in FootageTheme:
            raise InvalidInput("Video request contains invalid footage_theme.")
        if not isinstance(self.audio_text, (str, None)):
            raise InvalidInput("Video request contains invalid audio_text.")



# BELOW SHOWS AN EXAMPLE OF HOW TO USE A DATACLASS IN PYTHON
"""
from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class MyClass:
    name: str
    age: int
    email: str = ''
    is_active: bool = True
    extra_params: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        self.validate_inputs()

    def validate_inputs(self):
        if not isinstance(self.name, str) or len(self.name) == 0:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(self.age, int) or self.age < 0:
            raise ValueError("Age must be a non-negative integer")
        # Add more validations as needed
"""