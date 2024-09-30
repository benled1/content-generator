from media.video import Video, VideoRequest, VideoFactory
from storage import VideoStore, S3StorageHandler

import uuid

"""
TODO:
- create the s3 storage handler and store a video that was made in s3
- create a fastapi endpoint and expose the endpoint via a server

EXTRA TODO:
- change the audio and subtitles and footage 
"""


if __name__ == "__main__":

    video_request = VideoRequest(audio_text="This is created through the video compilation step!")
    video_factory = VideoFactory()
    video = video_factory.make_video(video_request=video_request)
    storage_handler = S3StorageHandler()
    video_store = VideoStore(storage_handler=storage_handler)
    res = video_store.store_video(video.uri)
    if res:
        print("video storage is complete")
    else:
        print("video storage failed")