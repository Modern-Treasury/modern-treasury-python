# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ConnectionLegalEntityUpdateParams"]


class ConnectionLegalEntityUpdateParams(TypedDict, total=False):
    status: Literal["processing"]
    """The status of the connection legal entity."""
