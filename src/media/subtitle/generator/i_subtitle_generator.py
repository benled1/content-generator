from abc import ABC, abstractmethod
from media.audio.audio import Audio


"""
IMPORTANT NOTE: remove the typing stuff from audio. This is overcomplicating things this early on and should just take a string input for now. 
"""

class ISubtitleGenerator(ABC):
    @abstractmethod
    def generate_subtitle(self, ref_audio: Audio):
        """
        Generate a subtitle object.
        This method will be implemented in subclasses
        """
        pass