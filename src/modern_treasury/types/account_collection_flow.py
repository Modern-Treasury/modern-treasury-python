# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountCollectionFlow"]


class AccountCollectionFlow(BaseModel):
    counterparty_id: str
    """The ID of a counterparty.

    An external account created with this flow will be associated with this
    counterparty.
    """

    payment_types: List[Literal["ach", "wire"]]

    id: Optional[str]

    client_token: Optional[str]
    """The client token of the account collection flow.

    This token can be used to embed account collection in your client-side
    application.
    """

    created_at: Optional[datetime]

    external_account_id: Optional[str]
    """If present, the ID of the external account created using this flow."""

    live_mode: Optional[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Optional[str]

    status: Optional[Literal["cancelled", "completed", "expired", "pending"]]
    """The current status of the account collection flow.

    One of `pending`, `completed`, `expired`, or `cancelled`.
    """

    updated_at: Optional[datetime]
