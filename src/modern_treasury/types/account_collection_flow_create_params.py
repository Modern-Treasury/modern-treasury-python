# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountCollectionFlowCreateParams"]


class AccountCollectionFlowCreateParams(TypedDict, total=False):
    counterparty_id: Required[str]
    """Required."""

    payment_types: Required[List[str]]

    receiving_countries: List[
        Literal[
            "USA",
            "AUS",
            "BEL",
            "CAN",
            "CHL",
            "CHN",
            "COL",
            "FRA",
            "DEU",
            "HKG",
            "IND",
            "IRL",
            "ITA",
            "MEX",
            "NLD",
            "PER",
            "ESP",
            "GBR",
        ]
    ]
