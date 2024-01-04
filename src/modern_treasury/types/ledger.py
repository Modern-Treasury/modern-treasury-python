# File generated from our OpenAPI spec by Stainless.

import builtins
from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Ledger"]


class Ledger(BaseModel):
    id: str

    created_at: datetime

    description: Optional[str] = None
    """An optional free-form description for internal use."""

    discarded_at: Optional[datetime] = None

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

    updated_at: datetime

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object:
            ...
