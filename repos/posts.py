from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    id: Optional[int]
    title: Optional[string]
    body: Optional[string]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


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