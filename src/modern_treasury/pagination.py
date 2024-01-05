# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import override

from httpx import Response

from ._utils import is_mapping, maybe_coerce_integer
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPage", "AsyncPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")


class SyncPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    per_page: Optional[int] = None
    after_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        after_cursor = self.after_cursor
        if not after_cursor:
            return None

        return PageInfo(params={"after_cursor": after_cursor})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                "per_page": maybe_coerce_integer(response.headers.get("X-Per-Page")),
                "after_cursor": response.headers.get("X-After-Cursor"),
            },
        )


class AsyncPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    per_page: Optional[int] = None
    after_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        after_cursor = self.after_cursor
        if not after_cursor:
            return None

        return PageInfo(params={"after_cursor": after_cursor})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
                "per_page": maybe_coerce_integer(response.headers.get("X-Per-Page")),
                "after_cursor": response.headers.get("X-After-Cursor"),
            },
        )
