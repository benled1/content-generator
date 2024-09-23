from abc import ABC, abstractmethod
from media.audio.audio import Audio
from uuid import UUID


"""
IMPORTANT NOTE: remove the typing stuff from audio. This is overcomplicating things this early on and should just take a string input for now. 
"""

class ISubtitleGenerator(ABC):
    @abstractmethod
    def generate_subtitle(self, ref_audio: Audio, uuid: UUID):
        """
        Generate a subtitle object.
        This method will be implemented in subclasses
        """
        pass