# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContactDetail"]


class ContactDetail(TypedDict, total=False):
    id: Required[str]

    contact_identifier: Required[str]

    contact_identifier_type: Required[Literal["email", "phone_number", "website"]]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    discarded_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
