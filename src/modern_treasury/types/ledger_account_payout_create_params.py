# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["LedgerAccountPayoutCreateParams"]


class LedgerAccountPayoutCreateParams(TypedDict, total=False):
    funding_ledger_account_id: Required[str]
    """
    The id of the funding ledger account that sends to or receives funds from the
    payout ledger account.
    """

    payout_ledger_account_id: Required[str]
    """
    The id of the payout ledger account whose ledger entries are queried against,
    and its balance is reduced as a result.
    """

    description: Optional[str]
    """The description of the ledger account payout."""

    effective_at_upper_bound: Optional[str]
    """
    The exclusive upper bound of the effective_at timestamp of the ledger entries to
    be included in the ledger account payout. The default value is the created_at
    timestamp of the ledger account payout.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    skip_payout_ledger_transaction: Optional[bool]
    """It is set to `false` by default.

    It should be set to `true` when migrating existing payouts.
    """

    status: Optional[Literal["pending", "posted"]]
    """The status of the ledger account payout.

    It is set to `pending` by default. To post a ledger account payout at creation,
    use `posted`.
    """
