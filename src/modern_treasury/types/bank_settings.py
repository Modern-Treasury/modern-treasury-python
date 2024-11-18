# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["BankSettings"]


class BankSettings(BaseModel):
    id: str

    backup_withholding_percentage: Optional[int] = None
    """The percentage of backup withholding to apply to the legal entity."""

    created_at: datetime

    discarded_at: Optional[datetime] = None

    enable_backup_withholding: Optional[bool] = None
    """Whether backup withholding is enabled.

    See more here -
    https://www.irs.gov/businesses/small-businesses-self-employed/backup-withholding.
    """

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    privacy_opt_out: Optional[bool] = None
    """Cross River Bank specific setting to opt out of privacy policy."""

    regulation_o: Optional[bool] = None
    """
    It covers, among other types of insider loans, extensions of credit by a member
    bank to an executive officer, director, or principal shareholder of the member
    bank; a bank holding company of which the member bank is a subsidiary; and any
    other subsidiary of that bank holding company.
    """

    updated_at: datetime
