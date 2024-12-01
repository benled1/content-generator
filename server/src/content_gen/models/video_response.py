from uuid import UUID, uuid4
from pydantic import BaseModel



class VideoResponse(BaseModel):
    uuid: UUID 
    presigned_video_uri: str
