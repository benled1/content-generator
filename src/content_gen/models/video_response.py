from uuid import UUID, uuid4
from pydantic import BaseModel



class VideoResponse(BaseModel):
    uuid: UUID 
    video_uri: str