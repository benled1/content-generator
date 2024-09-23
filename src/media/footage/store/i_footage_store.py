from abc import ABC, abstractmethod
from media.footage import Footage


class IFootageStore:

    @abstractmethod
    def get_footage(self, query: str) -> Footage:
        """
        Get footage from the store where it is. Store it locally in the 
        tmp folder under the same uuid as the other components being used in this 
        video creation. 
        """

        pass