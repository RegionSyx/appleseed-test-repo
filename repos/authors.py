from dataclasses import dataclass

@dataclass
class Author:
    id: int
    name: string


class AuthorRepo:

    def __init__(self, conn):
        self.conn = conn

    def get(self, id : int) -> Author:
        raise NotImplemented()

    def upsert(self, *authors : list[Authors]) -> list[Authors]:
        raise NotImplemented()

    def find(self) -> list[Authors]:
        raise NotImplemented()