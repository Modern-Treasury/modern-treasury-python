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
            "generic",
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
            "at_atin",
            "at_vat",
            "au_abn",
            "au_tfn",
            "be_ent",
            "be_nrn",
            "br_cnpj",
            "br_cpf",
            "ca_bn",
            "ca_sin",
            "ch_ahv",
            "ch_uid",
            "cl_run",
            "cl_rut",
            "co_cedulas",
            "co_nit",
            "cy_tin",
            "cz_ico",
            "cz_rc",
            "de_stid",
            "de_stnr",
            "de_vat",
            "dk_cpr",
            "dk_cvr",
            "drivers_license",
            "ee_ik",
            "ee_rk",
            "es_nie",
            "es_nif",
            "fi_hetu",
            "fi_ytj",
            "fr_nif",
            "fr_siren",
            "fr_vat",
            "gb_nino",
            "gb_utr",
            "gb_vat",
            "gr_vat",
            "hn_id",
            "hn_rtn",
            "hr_oib",
            "hu_adj",
            "hu_anum",
            "ie_pps",
            "ie_trn",
            "in_lei",
            "is_knt",
            "it_cf",
            "it_piva",
            "jp_hb",
            "jp_mn",
            "kr_brn",
            "kr_crn",
            "kr_rrn",
            "li_peid",
            "lt_ak",
            "lt_jak",
            "lu_mtc",
            "lu_vat",
            "lv_pk",
            "lv_rn",
            "mt_tin",
            "mt_vat",
            "mx_curp",
            "mx_ine",
            "mx_rfc",
            "nl_bsn",
            "nl_btw",
            "nl_rsin",
            "no_fdn",
            "no_mva",
            "no_orgnr",
            "nz_ird",
            "passport",
            "pl_nip",
            "pl_pesel",
            "pt_nif",
            "ro_cnp",
            "ro_cui",
            "sa_tin",
            "sa_vat",
            "se_orgnr",
            "se_pnmr",
            "sg_fin",
            "sg_nric",
            "sg_uen",
            "si_dav",
            "si_tin",
            "sk_ico",
            "sk_rc",
            "us_ein",
            "us_itin",
            "us_ssn",
            "uy_rut",
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
