from media.footage import Footage
from .i_footage_store import IFootageStore
from configurations.constants import FOOTAGE_STORAGE_URI


class LocalFootageStore(IFootageStore):

    def __init__(self) -> None:
        pass

    def get_footage(self, query: str) -> Footage:
        return Footage(FOOTAGE_STORAGE_URI)