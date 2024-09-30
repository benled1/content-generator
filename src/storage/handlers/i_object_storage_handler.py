from abc import ABC, abstractmethod


class IObjectStorageHandler(ABC):

    @abstractmethod
    def store_object(self, object_name: str, file_path: str, bucket: str):
        pass