from .footage import Footage
from .store import IFootageStore

class FootageFactory:

    def __init__(self, footage_store: IFootageStore) -> None:
        self.footage_store = footage_store
        pass

    def make_footage(self, query: str) -> Footage:
        """
        Retrieve footage.
        """
        return self.footage_store.get_footage(query)