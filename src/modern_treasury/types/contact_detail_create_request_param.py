# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ContactDetailCreateRequestParam"]


class ContactDetailCreateRequestParam(TypedDict, total=False):
    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number", "website"]
