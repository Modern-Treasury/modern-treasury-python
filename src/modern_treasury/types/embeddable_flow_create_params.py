# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "EmbeddableFlowCreateParams",
    "Options",
    "OptionsAccountCollectionFlowCreateRequest",
    "OptionsPaymentFlowCreateRequest",
    "OptionsType",
]


class EmbeddableFlowCreateParams(TypedDict, total=False):
    options: Required[Options]
    """The parameters for the selected template's flow."""

    template: Required[Literal["legal_entity_onboarding", "account_collection", "payment"]]


class OptionsAccountCollectionFlowCreateRequest(TypedDict, total=False):
    counterparty_id: Required[str]
    """Required."""

    payment_types: Required[SequenceNotStr[str]]

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


class OptionsPaymentFlowCreateRequest(TypedDict, total=False):
    amount: Required[int]
    """Required.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000. Can be any integer up to 36 digits.
    """

    counterparty_id: Required[str]
    """Required.

    The ID of a counterparty associated with the payment. As part of the payment
    workflow an external account will be associated with this model.
    """

    currency: Required[str]
    """Required. The currency of the payment."""

    direction: Required[Literal["credit", "debit"]]
    """Required.

    Describes the direction money is flowing in the transaction. Can only be
    `debit`. A `debit` pulls money from someone else's account to your own.
    """

    originating_account_id: Required[str]
    """Required. The ID of one of your organization's internal accounts."""

    due_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Optional.

    Can only be passed in when `effective_date_selection_enabled` is `true`. When
    set, the due date is shown to your end-user in the pre-built UI as they are
    selecting a payment `effective_date`.
    """


class OptionsType(TypedDict, total=False):
    type: Required[Literal["individual"]]


Options: TypeAlias = Union[OptionsAccountCollectionFlowCreateRequest, OptionsPaymentFlowCreateRequest, OptionsType]
