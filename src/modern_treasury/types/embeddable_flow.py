# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.transaction_direction import TransactionDirection

__all__ = ["EmbeddableFlow", "Options", "OptionsUnionMember0", "OptionsUnionMember1", "OptionsUnionMember2"]


class OptionsUnionMember0(BaseModel):
    legal_entity_id: str

    type: Literal["individual"]


class OptionsUnionMember1(BaseModel):
    counterparty_id: Optional[str] = None

    external_account_id: Optional[str] = None

    payment_types: List[str]

    receiving_countries: List[str]


class OptionsUnionMember2(BaseModel):
    amount: int

    counterparty_id: Optional[str] = None

    currency: str

    direction: TransactionDirection

    due_date: Optional[date] = None

    effective_date_selection_enabled: bool

    existing_external_accounts_filter: Optional[Literal["verified"]] = None

    external_account_collection: Literal["enabled", "disabled"]

    originating_account_id: str

    payment_order_id: Optional[str] = None

    receiving_account_id: Optional[str] = None

    selected_effective_date: Optional[date] = None


Options: TypeAlias = Union[OptionsUnionMember0, OptionsUnionMember1, OptionsUnionMember2]


class EmbeddableFlow(BaseModel):
    id: str

    client_token: str

    created_at: datetime

    expires_at: datetime

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    options: Options

    status: Literal["cancelled", "completed", "expired", "pending"]
    """The current status of the underlying flow."""

    template: Literal["legal_entity_onboarding", "account_collection", "payment"]

    updated_at: datetime
