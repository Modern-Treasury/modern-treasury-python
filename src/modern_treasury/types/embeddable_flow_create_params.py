# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .payment_flow_create_request_param import PaymentFlowCreateRequestParam
from .account_collection_flow_create_request_param import AccountCollectionFlowCreateRequestParam

__all__ = ["EmbeddableFlowCreateParams", "Options", "OptionsType"]


class EmbeddableFlowCreateParams(TypedDict, total=False):
    options: Required[Options]
    """The parameters for the selected template's flow."""

    template: Required[Literal["legal_entity_onboarding", "account_collection", "payment"]]


class OptionsType(TypedDict, total=False):
    type: Required[Literal["individual"]]


Options: TypeAlias = Union[AccountCollectionFlowCreateRequestParam, PaymentFlowCreateRequestParam, OptionsType]
