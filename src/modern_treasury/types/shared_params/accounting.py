# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["Accounting"]


class Accounting(TypedDict, total=False):
    account_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    class_id: Optional[str]
    """The ID of one of the class objects in your accounting system.

    Class objects track segments of your business independent of client or project.
    Note that these will only be accessible if your accounting system has been
    connected.
    """
