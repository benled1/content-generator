from abc import ABC, abstractmethod
from media.footage import Footage

class IFootageGenerator(ABC):

    @abstractmethod
    def generate_footage(self) -> Footage:
        """
        Get or generate footage and return it. 
        """
        pass


