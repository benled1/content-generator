from .handlers import IObjectStorageHandler
from content_gen.configurations.constants import VIDEO_BUCKET_NAME

import os

class VideoStore():

    def __init__(self, storage_handler: IObjectStorageHandler) -> None:
        self.storage_handler = storage_handler

    def store_video(self, video_file_path: str) -> bool:
        res: bool = self.storage_handler.store_object(object_name=f"videos/{os.path.basename(video_file_path)}", file_path=video_file_path, bucket=VIDEO_BUCKET_NAME)
        return res
            


