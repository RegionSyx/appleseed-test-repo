# This file was generated by Johny Appleseed
# Date: 2021-11-29T00:51:05.813096
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Tag:
    id: Optional[int]
    label: Optional[string]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class TagRepo:
    def __init__(self, conn):
        self.conn = conn

    def get(self, id: int) -> Tag:
        raise NotImplementedError()

    def upsert(self, *tags: list[Tags]) -> list[Tags]:
        raise NotImplementedError()

    def find(self) -> list[Tags]:
        raise NotImplementedError()

    def delete(self, id: int) -> Tag:
        raise NotImplementedError()