from content_gen.media.video import Video, VideoFactory
from content_gen.models import VideoRequest, VideoResponse
from content_gen.storage import VideoStore, S3StorageHandler
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import uuid

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world from content-gen root"}

@app.post("/api/v1/video")
async def create_video(video_request: VideoRequest):
    print(f"Creating a video for {video_request.__dict__}")
    video_factory = VideoFactory()
    video = video_factory.make_video(video_request=video_request)

    # store the video in cloud
    storage_handler = S3StorageHandler()
    video_store = VideoStore(storage_handler=storage_handler)
    presigned_object_uri = video_store.store_video(video.uri)
    if not presigned_object_uri:
        print("Upload failed.")
        raise HTTPException(status_code=500, detail="Video upload failed.")
    video_response = VideoResponse(uuid=video_request.uuid, presigned_video_uri=presigned_object_uri)
    return video_response    

# if __name__ == "__main__":
#     # make the video
#     video_request = VideoRequest(audio_text="this is a test video text")
#     print(f"Creating a video for {video_request.__dict__}")
#     video_factory = VideoFactory()
#     video = video_factory.make_video(video_request=video_request)

#     # store the video in cloud
#     storage_handler = S3StorageHandler()
#     video_store = VideoStore(storage_handler=storage_handler)
#     uploaded_object = video_store.store_video(video.uri)
#     if not uploaded_object:
#         print("Upload failed.")
        
