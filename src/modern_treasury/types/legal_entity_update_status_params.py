# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["LegalEntityUpdateStatusParams"]


class LegalEntityUpdateStatusParams(TypedDict, total=False):
    status: Required[Literal["active", "suspended", "denied"]]
    """The target status for the legal entity.

    One of `active`, `suspended`, or `denied`. Valid transitions depend on the
    current status.
    """
