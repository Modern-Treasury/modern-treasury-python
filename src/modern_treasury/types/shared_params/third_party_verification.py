# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ThirdPartyVerification"]


class ThirdPartyVerification(TypedDict, total=False):
    outcome: Required[Literal["passed", "failed"]]
    """The outcome of the verification. One of `passed` or `failed`."""

    vendor: Required[Literal["persona", "middesk", "alloy", "sumsub", "veriff"]]
    """The vendor that performed the verification, e.g. `persona`."""

    vendor_verification_id: Required[str]
    """The identification of the third party verification in `vendor`'s system."""

    verification_category: Required[
        Literal["legal_name", "date_of_birth", "address", "government_id_number", "adverse_media"]
    ]
    """The category of verification performed."""

    verification_method: Required[str]
    """The method used to perform the verification."""

    verification_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The timestamp when the verification was performed."""

    comment: Optional[str]
    """An optional comment about the verification."""
