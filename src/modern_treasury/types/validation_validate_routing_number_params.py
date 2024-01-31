# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ValidationValidateRoutingNumberParams"]


class ValidationValidateRoutingNumberParams(TypedDict, total=False):
    routing_number: Required[str]
    """The routing number that is being validated."""

    routing_number_type: Required[
        Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "dk_interbank_clearing_code",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "hu_interbank_clearing_code",
            "id_sknbi_code",
            "in_ifsc",
            "jp_zengin_code",
            "mx_bank_identifier",
            "my_branch_code",
            "nz_national_clearing_code",
            "pl_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ]
    ]
    """The type of routing number.

    See https://docs.moderntreasury.com/platform/reference/routing-detail-object for
    more details. In sandbox mode we currently only support `aba` and `swift` with
    routing numbers '123456789' and 'GRINUST0XXX' respectively.
    """
