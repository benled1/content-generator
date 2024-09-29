from abc import ABC, abstractmethod


class IStorageHandler(ABC):

    @abstractmethod
    def store_object(self, object_path: str):
        pass