from configurations.constants import AUDIO_STORAGE_URI
import ChatTTS
import torch
import torchaudio
import numpy as np
import uuid
import os


class Audio:

    def __init__(self, uri: str) -> None:
        self.uri = uri

    