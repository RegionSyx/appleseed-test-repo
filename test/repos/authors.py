# This file was generated by Johny Appleseed
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Author:
    name: Optional[string]
    None: Optional[]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class AuthorRepo:
    def __init__(self, conn):
        self.conn = conn

    def get(self, id: int) -> Author:
        raise NotImplementedError()

    def upsert(self, *authors: list[Authors]) -> list[Authors]:
        raise NotImplementedError()

    def find(self) -> list[Authors]:
        raise NotImplementedError()

    def delete(self, id: int) -> Author:
        raise NotImplementedError()