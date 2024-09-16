from abc import ABC, abstractmethod


class IAudioGenerator(ABC):

    @abstractmethod
    def generate_audio(self):
        """
        Generate an audio object.
        This method will be implemented in subclasses
        """
        pass