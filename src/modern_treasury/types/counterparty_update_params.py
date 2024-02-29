# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["CounterpartyUpdateParams"]


class CounterpartyUpdateParams(TypedDict, total=False):
    email: str
    """A new email for the counterparty."""

    legal_entity_id: Optional[str]
    """The id of the legal entity."""

    metadata: Dict[str, str]
    """Additional data in the form of key-value pairs.

    Pairs can be removed by passing an empty string or `null` as the value.
    """

    name: str
    """A new name for the counterparty. Will only update if passed."""

    send_remittance_advice: bool
    """
    If this is `true`, Modern Treasury will send an email to the counterparty
    whenever an associated payment order is sent to the bank.
    """

    taxpayer_identifier: str
    """Either a valid SSN or EIN."""
