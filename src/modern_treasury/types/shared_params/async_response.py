# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AsyncResponse"]


class AsyncResponse(TypedDict, total=False):
    id: Required[str]

    object: Required[str]
