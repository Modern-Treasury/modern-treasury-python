# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LegalEntityComplianceDetail"]


class LegalEntityComplianceDetail(TypedDict, total=False):
    id: Required[str]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    discarded_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]

    issuer: Required[str]
    """The issuer of the compliance token."""

    live_mode: Required[bool]
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: Required[str]

    token_expires_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]
    """The timestamp when the compliance token expires."""

    token_issued_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]
    """The timestamp when the compliance token was issued."""

    token_url: Required[Optional[str]]
    """The URL to the compliance token. (ex. provider portal URL)"""

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    validated: Required[bool]
    """Whether entity corresponding to the compliance token has been validated."""

    validated_at: Required[Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]]
    """The timestamp when the entity was validated."""
