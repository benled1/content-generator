import shutil
import os

from uuid import UUID

from content_gen.media.footage import Footage
from .i_footage_store import IFootageStore
from content_gen.configurations.constants import FOOTAGE_STORE_URI, TMP_DIR


class LocalFootageStore(IFootageStore):

    def __init__(self) -> None:
        pass

    def get_footage(self, theme: str, uuid: UUID) -> Footage:
        src = os.path.join(FOOTAGE_STORE_URI, "test-minecraft.mp4")
        dst = os.path.join(FOOTAGE_STORE_URI, f"{uuid}.mp4")
        shutil.copy(src, dst)
        return Footage(dst)