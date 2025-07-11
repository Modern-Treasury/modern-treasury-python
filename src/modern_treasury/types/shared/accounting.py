# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Accounting"]


class Accounting(BaseModel):
    account_id: Optional[str] = None
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    class_id: Optional[str] = None
    """The ID of one of the class objects in your accounting system.

    Class objects track segments of your business independent of client or project.
    Note that these will only be accessible if your accounting system has been
    connected.
    """
