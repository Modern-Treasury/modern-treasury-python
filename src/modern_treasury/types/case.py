# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .requested_action import RequestedAction

__all__ = ["Case"]


class Case(BaseModel):
    id: str

    created_at: datetime

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    requested_actions: List[RequestedAction]
    """The pending actions requested to resolve the case."""

    resolved_actions: List[RequestedAction]
    """The requested actions that have been resolved."""

    status: Literal["open", "resolved"]
    """The status of the case."""

    subject_id: str
    """The ID of the object the case is about."""

    subject_type: str
    """The type of the object the case is about."""

    updated_at: datetime
