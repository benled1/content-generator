from abc import ABC, abstractmethod


class IFootageStore:

    @abstractmethod
    def get_footage(self, query: str):
        """
        Get footage from a query 
        """
        pass