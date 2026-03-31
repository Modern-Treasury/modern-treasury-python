# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IdentificationCreateRequest", "Documents", "Document"]


class Document(TypedDict, total=False):
    document_type: Required[
        Literal[
            "articles_of_incorporation",
            "certificate_of_good_standing",
            "ein_letter",
            "identification_back",
            "identification_front",
            "proof_of_address",
        ]
    ]
    """A category given to the document, can be `null`."""

    file_data: Required[str]
    """Base64-encoded file content for the document."""

    filename: str
    """The original filename of the document."""


Documents = Document
"""This type is deprecated and will be removed in a future release.

Please use Document instead.
"""


class IdentificationCreateRequest(TypedDict, total=False):
    id_number: Required[str]
    """The ID number of identification document."""

    id_type: Required[
        Literal[
            "ar_cuil",
            "ar_cuit",
            "br_cnpj",
            "br_cpf",
            "ca_sin",
            "cl_run",
            "cl_rut",
            "co_cedulas",
            "co_nit",
            "drivers_license",
            "hn_id",
            "hn_rtn",
            "ie_pps",
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
    ]
    """The type of ID number."""

    documents: Iterable[Document]
    """A list of documents to attach to the identification."""

    expiration_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """
    The date when the Identification is no longer considered valid by the issuing
    authority.
    """

    issuing_country: Optional[str]
    """
    The ISO 3166-1 alpha-2 country code of the country that issued the
    identification
    """

    issuing_region: Optional[str]
    """The region in which the identifcation was issued."""
