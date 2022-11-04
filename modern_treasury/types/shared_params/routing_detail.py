# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BankAddress", "RoutingDetail"]


class BankAddress(TypedDict, total=False):
    country: Required[Optional[str]]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    created_at: Required[str]

    id: Required[str]

    line1: Required[Optional[str]]

    line2: Required[Optional[str]]

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    locality: Required[Optional[str]]
    """Locality or City."""

    object: Required[str]

    postal_code: Required[Optional[str]]
    """The postal code of the address."""

    region: Required[Optional[str]]
    """Region or State."""

    updated_at: Required[str]


class RoutingDetail(TypedDict, total=False):
    bank_address: Required[Optional[BankAddress]]

    bank_name: Required[str]
    """The name of the bank."""

    created_at: Required[str]

    discarded_at: Required[Optional[str]]

    id: Required[str]

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    payment_type: Required[
        Optional[
            Literal[
                "ach",
                "au_becs",
                "bacs",
                "book",
                "card",
                "check",
                "eft",
                "global_pay",
                "interac",
                "provxchange",
                "rtp",
                "sen",
                "sepa",
                "signet",
                "wire",
            ]
        ]
    ]
    """
    If the routing detail is to be used for a specific payment type this field will
    be populated, otherwise null.
    """

    routing_number: Required[str]
    """The routing number of the bank."""

    routing_number_type: Required[
        Literal["aba", "au_bsb", "br_codigo", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "swift"]
    ]
    """One of `aba`, `swift`, `ca_cpa`, `au_bsb`, `gb_sort_code`, `in_ifsc`, `cnaps`."""

    updated_at: Required[str]
