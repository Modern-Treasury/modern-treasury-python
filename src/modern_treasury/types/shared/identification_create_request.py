# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IdentificationCreateRequest"]


class IdentificationCreateRequest(BaseModel):
    id_number: str
    """The ID number of identification document."""

    id_type: Literal[
        "ar_cuil",
        "ar_cuit",
        "br_cnpj",
        "br_cpf",
        "cl_run",
        "cl_rut",
        "co_cedulas",
        "co_nit",
        "drivers_license",
        "hn_id",
        "hn_rtn",
        "in_lei",
        "kr_brn",
        "kr_crn",
        "kr_rrn",
        "passport",
        "sa_tin",
        "sa_vat",
        "us_ein",
        "us_itin",
        "us_ssn",
        "vn_tin",
    ]
    """The type of ID number."""

    expiration_date: Optional[date] = None
    """
    The date when the Identification is no longer considered valid by the issuing
    authority.
    """

    issuing_country: Optional[str] = None
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """

    issuing_region: Optional[str] = None
    """The region in which the identifcation was issued."""
