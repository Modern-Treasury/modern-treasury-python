# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmbeddableFlowUpdateParams"]


class EmbeddableFlowUpdateParams(TypedDict, total=False):
    status: Required[Literal["cancelled"]]
    """The updated status of the flow.

    Can only be used to mark the flow as `cancelled`.
    """
