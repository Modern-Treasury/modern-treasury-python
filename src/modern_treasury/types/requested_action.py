# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RequestedAction"]


class RequestedAction(BaseModel):
    id: str

    category: Literal[
        "onboarding_articles_of_incorporation_failure",
        "onboarding_business_registry_verification_failure",
        "onboarding_database_failure",
        "onboarding_proof_of_address_failure",
        "onboarding_ssn_check_failure",
        "onboarding_tin_check_failure",
    ]
    """The category of the requested action."""

    created_at: datetime

    field: Optional[Literal["articles_of_incorporation", "ein_letter", "legal_entity_details", "proof_of_address"]] = (
        None
    )
    """The field that needs to be corrected or provided, if any."""

    instructions: Optional[str] = None
    """Instructions on how to resolve the requested action."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    reasons: List[str]
    """The reasons the action was requested."""

    updated_at: datetime
