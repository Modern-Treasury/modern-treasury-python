# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import identification_create_params, identification_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.identification import Identification

__all__ = ["Identifications", "AsyncIdentifications"]


class Identifications(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentificationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return IdentificationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentificationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return IdentificationsWithStreamingResponse(self)

    def create(
        self,
        *,
        id_number: str,
        id_type: Literal[
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
            "generic_international",
            "gr_vat",
            "hk_brn",
            "hk_hkid",
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
            "national_id",
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
        ],
        legal_entity_id: str,
        documents: Iterable[identification_create_params.Document] | Omit = omit,
        expiration_date: Union[str, date, None] | Omit = omit,
        issuing_country: Optional[str] | Omit = omit,
        issuing_region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Identification:
        """
        Create an Identification for a Legal Entity.

        Args:
          id_number: The ID number of identification document.

          id_type: The type of ID number.

          legal_entity_id: The ID of the Legal Entity the identification belongs to.

          documents: A list of documents to attach to the identification.

          expiration_date: The date when the Identification is no longer considered valid by the issuing
              authority.

          issuing_country: The ISO 3166-1 alpha-2 country code of the country that issued the
              identification

          issuing_region: The region in which the identifcation was issued.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/identifications",
            body=maybe_transform(
                {
                    "id_number": id_number,
                    "id_type": id_type,
                    "legal_entity_id": legal_entity_id,
                    "documents": documents,
                    "expiration_date": expiration_date,
                    "issuing_country": issuing_country,
                    "issuing_region": issuing_region,
                },
                identification_create_params.IdentificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Identification,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identification:
        """
        Get an existing Identification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/identifications/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identification,
        )

    def update(
        self,
        id: str,
        *,
        expiration_date: Union[str, date, None] | Omit = omit,
        id_number: str | Omit = omit,
        id_type: Literal[
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
            "generic_international",
            "gr_vat",
            "hk_brn",
            "hk_hkid",
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
            "national_id",
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
        | Omit = omit,
        issuing_country: Optional[str] | Omit = omit,
        issuing_region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Identification:
        """
        Update an existing Identification.

        Args:
          expiration_date: The date when the Identification is no longer considered valid by the issuing
              authority.

          id_number: The ID number of identification document.

          id_type: The type of ID number.

          issuing_country: The ISO 3166-1 alpha-2 country code of the country that issued the
              identification

          issuing_region: The region in which the identifcation was issued.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/api/identifications/{id}", id=id),
            body=maybe_transform(
                {
                    "expiration_date": expiration_date,
                    "id_number": id_number,
                    "id_type": id_type,
                    "issuing_country": issuing_country,
                    "issuing_region": issuing_region,
                },
                identification_update_params.IdentificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Identification,
        )


class AsyncIdentifications(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentificationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentificationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentificationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncIdentificationsWithStreamingResponse(self)

    async def create(
        self,
        *,
        id_number: str,
        id_type: Literal[
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
            "generic_international",
            "gr_vat",
            "hk_brn",
            "hk_hkid",
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
            "national_id",
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
        ],
        legal_entity_id: str,
        documents: Iterable[identification_create_params.Document] | Omit = omit,
        expiration_date: Union[str, date, None] | Omit = omit,
        issuing_country: Optional[str] | Omit = omit,
        issuing_region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Identification:
        """
        Create an Identification for a Legal Entity.

        Args:
          id_number: The ID number of identification document.

          id_type: The type of ID number.

          legal_entity_id: The ID of the Legal Entity the identification belongs to.

          documents: A list of documents to attach to the identification.

          expiration_date: The date when the Identification is no longer considered valid by the issuing
              authority.

          issuing_country: The ISO 3166-1 alpha-2 country code of the country that issued the
              identification

          issuing_region: The region in which the identifcation was issued.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/identifications",
            body=await async_maybe_transform(
                {
                    "id_number": id_number,
                    "id_type": id_type,
                    "legal_entity_id": legal_entity_id,
                    "documents": documents,
                    "expiration_date": expiration_date,
                    "issuing_country": issuing_country,
                    "issuing_region": issuing_region,
                },
                identification_create_params.IdentificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Identification,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Identification:
        """
        Get an existing Identification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/identifications/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Identification,
        )

    async def update(
        self,
        id: str,
        *,
        expiration_date: Union[str, date, None] | Omit = omit,
        id_number: str | Omit = omit,
        id_type: Literal[
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
            "generic_international",
            "gr_vat",
            "hk_brn",
            "hk_hkid",
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
            "national_id",
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
        | Omit = omit,
        issuing_country: Optional[str] | Omit = omit,
        issuing_region: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Identification:
        """
        Update an existing Identification.

        Args:
          expiration_date: The date when the Identification is no longer considered valid by the issuing
              authority.

          id_number: The ID number of identification document.

          id_type: The type of ID number.

          issuing_country: The ISO 3166-1 alpha-2 country code of the country that issued the
              identification

          issuing_region: The region in which the identifcation was issued.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/api/identifications/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "expiration_date": expiration_date,
                    "id_number": id_number,
                    "id_type": id_type,
                    "issuing_country": issuing_country,
                    "issuing_region": issuing_region,
                },
                identification_update_params.IdentificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Identification,
        )


class IdentificationsWithRawResponse:
    def __init__(self, identifications: Identifications) -> None:
        self._identifications = identifications

        self.create = _legacy_response.to_raw_response_wrapper(
            identifications.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            identifications.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            identifications.update,
        )


class AsyncIdentificationsWithRawResponse:
    def __init__(self, identifications: AsyncIdentifications) -> None:
        self._identifications = identifications

        self.create = _legacy_response.async_to_raw_response_wrapper(
            identifications.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            identifications.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            identifications.update,
        )


class IdentificationsWithStreamingResponse:
    def __init__(self, identifications: Identifications) -> None:
        self._identifications = identifications

        self.create = to_streamed_response_wrapper(
            identifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            identifications.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            identifications.update,
        )


class AsyncIdentificationsWithStreamingResponse:
    def __init__(self, identifications: AsyncIdentifications) -> None:
        self._identifications = identifications

        self.create = async_to_streamed_response_wrapper(
            identifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            identifications.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            identifications.update,
        )
