from media.video import Video, VideoRequest, VideoFactory
from storage import VideoStore, S3StorageHandler
from fastapi import FastAPI
from pydantic import BaseModel

import uuid



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world from content-gen root"}

"""
TODO: CHANGE THE VIDEOREQUEST FROM A DATA CLASS TO PYDANTIC BASEMODEL
"""
@app.post("/api/v1/video")
async def post_video():

    pass

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