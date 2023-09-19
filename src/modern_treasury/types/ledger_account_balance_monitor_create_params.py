# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["LedgerAccountBalanceMonitorCreateParams", "AlertCondition"]


class LedgerAccountBalanceMonitorCreateParams(TypedDict, total=False):
    alert_condition: Required[AlertCondition]
    """Describes the condition that must be satisfied for the monitor to be triggered."""

    ledger_account_id: Required[str]
    """The ledger account associated with this balance monitor."""

    description: str
    """An optional, free-form description for internal use."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class AlertCondition(TypedDict, total=False):
    field: Required[str]
    """
    One of `available_balance_amount`, `pending_balance_amount`,
    `posted_balance_amount`, `ledger_account_lock_version`.
    """

    operator: Required[str]
    """A logical operator to compare the `field` against the `value`.

    One of `less_than`, `less_than_or_equals`, `equals`, `greater_than_or_equals`,
    `greater_than`.
    """

    value: Required[int]
    """
    The monitor's `current_ledger_account_balance_state.triggered` will be `true`
    when comparing the `field` to this integer value using the `operator` is
    logically true.
    """
