# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from .._types import SequenceNotStr

from typing import List

__all__ = ["AccountCollectionFlowCreateParams"]

class AccountCollectionFlowCreateParams(TypedDict, total=False):
    counterparty_id: Required[str]
    """Required."""

    payment_types: Required[SequenceNotStr[str]]

    receiving_countries: List[Literal["USA", "AUS", "BEL", "CAN", "CHL", "CHN", "COL", "FRA", "DEU", "HKG", "IND", "IRL", "ITA", "MEX", "NLD", "PER", "ESP", "GBR"]]