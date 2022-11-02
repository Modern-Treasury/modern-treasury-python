# File generated from our OpenAPI spec by Stainless.

from typing import List, Type, Generic, Mapping, TypeVar, Optional
from typing_extensions import TypedDict

from httpx import Response

from ._types import ModelT
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["PageParams", "SyncPage", "AsyncPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


class PageParams(TypedDict, total=False):
    after_cursor: Optional[str]

    per_page: int


class SyncPage(BaseSyncPage[ModelT], BasePage[ModelT, PageParams], Generic[ModelT]):
    items: List[ModelT]
    per_page: Optional[int]
    after_cursor: Optional[str]

    def _get_page_items(self) -> List[ModelT]:
        return self.items

    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.after_cursor
        if not cursor:
            return None

        return PageInfo(params={"after_cursor": cursor})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:
        return cls.construct(
            **{
                **(data if isinstance(data, Mapping) else {"items": data}),
                "per_page": response.headers.get("X-Per-Page"),
                "after_cursor": response.headers.get("X-After-Cursor"),
            }
        )


class AsyncPage(BaseAsyncPage[ModelT], BasePage[ModelT, PageParams], Generic[ModelT]):
    items: List[ModelT]
    per_page: Optional[int]
    after_cursor: Optional[str]

    def _get_page_items(self) -> List[ModelT]:
        return self.items

    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.after_cursor
        if not cursor:
            return None

        return PageInfo(params={"after_cursor": cursor})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:
        return cls.construct(
            **{
                **(data if isinstance(data, Mapping) else {"items": data}),
                "per_page": response.headers.get("X-Per-Page"),
                "after_cursor": response.headers.get("X-After-Cursor"),
            }
        )
