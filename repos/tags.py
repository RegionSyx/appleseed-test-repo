from dataclasses import dataclass


@dataclass
class Tag:
    id: int
    label: string


class TagRepo:

    def __init__(self, conn):
        self.conn = conn

    def get(self, id : int) -> Tag:
        raise NotImplementedError()

    def upsert(self, *tags : list[Tags]) -> list[Tags]:
        raise NotImplementedError()

    def find(self) -> list[Tags]:
        raise NotImplementedError()

    def delete(self, id : int) -> Tag:
        raise NotImplementedError()