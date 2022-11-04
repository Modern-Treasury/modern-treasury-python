# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["Connection"]


class Connection(BaseModel):
    created_at: str

    discarded_at: Optional[str]

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    updated_at: str

    vendor_customer_id: Optional[str]
    """An identifier given to this connection by the bank."""

    vendor_id: str
    """Unique identifier for the bank or vendor."""

    vendor_name: str
    """A human-friendly name for the bank or vendor."""
