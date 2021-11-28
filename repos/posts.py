from dataclasses import dataclass


@dataclass
class Post:
    id: int
    title: string
    body: string


class PostRepo:
    def __init__(self, conn):
        self.conn = conn

    def get(self, id: int) -> Post:
        raise NotImplementedError()

    def upsert(self, *posts : list[Posts]) -> list[Posts]:
        raise NotImplementedError()

    def find(self) -> list[Posts]:
        raise NotImplementedError()

    def delete(self, id: int) -> Post:
        raise NotImplementedError()