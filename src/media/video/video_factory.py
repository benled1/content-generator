from .video_request import VideoRequest
from .video import Video

class VideoFactory:

    def __init__(self) -> None:
        pass

    def make_video(self, video_request: VideoRequest) -> Video:
        """
        Parse the video request and create the necessary components for the video.
        """
        pass