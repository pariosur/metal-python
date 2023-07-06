from __future__ import annotations
from enum import Enum
from typing import List
from typing_extensions import TypedDict, NotRequired


class TuneLabel(Enum):
    NEGATIVE = -1
    NEUTRAL = 0
    POSITIVE = 1


class IndexPayload(TypedDict):
    id: NotRequired[str]
    imageBase64: NotRequired[str]
    imageUrl: NotRequired[str]
    text: NotRequired[str]
    embedding: NotRequired[List[float]]
    metadata: NotRequired[dict]


class BulkIndexItem(TypedDict):
    id: NotRequired[str]
    index: str
    imageBase64: NotRequired[str]
    imageUrl: NotRequired[str]
    text: NotRequired[str]
    embedding: NotRequired[List[float]]
    metadata: NotRequired[dict]


class BulkIndexPayload(TypedDict):
    data: List[BulkIndexItem]


class SearchFilter(TypedDict):
    and: NotRequired[List[SearchClause]]
    or: NotRequired[List[SearchClause]]


class SearchClause(TypedDict):
    field: str
    value: str | int | float
    operator: str


class SearchPayload(TypedDict):
    imageBase64: NotRequired[str]
    imageUrl: NotRequired[str]
    text: NotRequired[str]
    embedding: NotRequired[List[float]]
    filters: NotRequired[SearchFilter]


class TunePayload(TypedDict):
    idA: str
    idB: str
    label: TuneLabel


class MotorheadPayload(TypedDict):
    api_key: NotRequired[str]
    client_id: NotRequired[str]
    base_url: NotRequired[str]
