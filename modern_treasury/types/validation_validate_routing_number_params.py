# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ValidationValidateRoutingNumberParams"]


class ValidationValidateRoutingNumberParams(TypedDict, total=False):
    routing_number: Required[str]
    """The routing number that is being validated."""

    routing_number_type: Required[
        Literal["aba", "au_bsb", "br_codigo", "ca_cpa", "cnaps", "gb_sort_code", "in_ifsc", "my_branch_code", "swift"]
    ]
    """
    One of `aba`, `au_bsb`, `br_codigo`, `ca_cpa`, `cnaps`, `gb_sort_code`,
    `in_ifsc`, `my_branch_code`, or `swift`. In sandbox mode we currently only
    support `aba` and `swift` with routing numbers '123456789' and 'GRINUST0XXX'
    respectively.
    """
