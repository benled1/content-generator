from abc import ABC, abstractmethod
from content_gen.media.audio.audio import Audio
from uuid import UUID


class ISubtitleGenerator(ABC):
    @abstractmethod
    def generate_subtitle(self, ref_audio: Audio, uuid: UUID):
        """
        Generate a subtitle object.
        This method will be implemented in subclasses
        """
        pass