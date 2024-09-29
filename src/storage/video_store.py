from handlers import IStorageHandler



class VideoStore():

    def __init__(self, storage_handler: IStorageHandler) -> None:
        self.storage_handler = storage_handler
        pass

    def store_video(self, video_path: str) -> None:
        self.storage_handler.store_object(object_path=video_path)
        pass
