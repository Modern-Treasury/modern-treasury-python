# File generated from our OpenAPI spec by Stainless.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Ledger"]


class Ledger(BaseModel):
    created_at: str

    description: Optional[str]
    """An optional free-form description for internal use."""

    discarded_at: Optional[str]

    id: str

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: str
    """The name of the ledger."""

    object: str

    updated_at: str
