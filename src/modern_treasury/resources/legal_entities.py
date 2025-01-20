# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    legal_entity_list_params,
    legal_entity_create_params,
    legal_entity_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.legal_entity import LegalEntity
from ..types.bank_settings_param import BankSettingsParam
from ..types.wealth_and_employment_details_param import WealthAndEmploymentDetailsParam

__all__ = ["LegalEntities", "AsyncLegalEntities"]


class LegalEntities(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LegalEntitiesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return LegalEntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LegalEntitiesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return LegalEntitiesWithStreamingResponse(self)

    def create(
        self,
        *,
        legal_entity_type: Literal["business", "individual"],
        addresses: Iterable[legal_entity_create_params.Address] | NotGiven = NOT_GIVEN,
        bank_settings: Optional[BankSettingsParam] | NotGiven = NOT_GIVEN,
        business_name: Optional[str] | NotGiven = NOT_GIVEN,
        citizenship_country: Optional[str] | NotGiven = NOT_GIVEN,
        date_formed: Union[str, date, None] | NotGiven = NOT_GIVEN,
        date_of_birth: Union[str, date, None] | NotGiven = NOT_GIVEN,
        doing_business_as_names: List[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        identifications: Iterable[legal_entity_create_params.Identification] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        legal_entity_associations: Optional[Iterable[legal_entity_create_params.LegalEntityAssociation]]
        | NotGiven = NOT_GIVEN,
        legal_structure: Optional[
            Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        middle_name: Optional[str] | NotGiven = NOT_GIVEN,
        phone_numbers: Iterable[legal_entity_create_params.PhoneNumber] | NotGiven = NOT_GIVEN,
        politically_exposed_person: Optional[bool] | NotGiven = NOT_GIVEN,
        preferred_name: Optional[str] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        risk_rating: Optional[Literal["low", "medium", "high"]] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        wealth_and_employment_details: Optional[WealthAndEmploymentDetailsParam] | NotGiven = NOT_GIVEN,
        website: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LegalEntity:
        """
        create legal_entity

        Args:
          legal_entity_type: The type of legal entity.

          addresses: A list of addresses for the entity.

          business_name: The business's legal business name.

          citizenship_country: The country of citizenship for an individual.

          date_formed: A business's formation date (YYYY-MM-DD).

          date_of_birth: An individual's date of birth (YYYY-MM-DD).

          email: The entity's primary email.

          first_name: An individual's first name.

          identifications: A list of identifications for the legal entity.

          last_name: An individual's last name.

          legal_entity_associations: The legal entity associations and its child legal entities.

          legal_structure: The business's legal structure.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          middle_name: An individual's middle name.

          politically_exposed_person: Whether the individual is a politically exposed person.

          preferred_name: An individual's preferred name.

          prefix: An individual's prefix.

          risk_rating: The risk rating of the legal entity. One of low, medium, high.

          suffix: An individual's suffix.

          website: The entity's primary website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/legal_entities",
            body=maybe_transform(
                {
                    "legal_entity_type": legal_entity_type,
                    "addresses": addresses,
                    "bank_settings": bank_settings,
                    "business_name": business_name,
                    "citizenship_country": citizenship_country,
                    "date_formed": date_formed,
                    "date_of_birth": date_of_birth,
                    "doing_business_as_names": doing_business_as_names,
                    "email": email,
                    "first_name": first_name,
                    "identifications": identifications,
                    "last_name": last_name,
                    "legal_entity_associations": legal_entity_associations,
                    "legal_structure": legal_structure,
                    "metadata": metadata,
                    "middle_name": middle_name,
                    "phone_numbers": phone_numbers,
                    "politically_exposed_person": politically_exposed_person,
                    "preferred_name": preferred_name,
                    "prefix": prefix,
                    "risk_rating": risk_rating,
                    "suffix": suffix,
                    "wealth_and_employment_details": wealth_and_employment_details,
                    "website": website,
                },
                legal_entity_create_params.LegalEntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LegalEntity,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LegalEntity:
        """
        Get details on a single legal entity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/legal_entities/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LegalEntity,
        )

    def update(
        self,
        id: str,
        *,
        addresses: Iterable[legal_entity_update_params.Address] | NotGiven = NOT_GIVEN,
        bank_settings: Optional[BankSettingsParam] | NotGiven = NOT_GIVEN,
        business_name: Optional[str] | NotGiven = NOT_GIVEN,
        citizenship_country: Optional[str] | NotGiven = NOT_GIVEN,
        date_formed: Union[str, date, None] | NotGiven = NOT_GIVEN,
        date_of_birth: Union[str, date, None] | NotGiven = NOT_GIVEN,
        doing_business_as_names: List[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        identifications: Iterable[legal_entity_update_params.Identification] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        legal_structure: Optional[
            Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        middle_name: Optional[str] | NotGiven = NOT_GIVEN,
        phone_numbers: Iterable[legal_entity_update_params.PhoneNumber] | NotGiven = NOT_GIVEN,
        politically_exposed_person: Optional[bool] | NotGiven = NOT_GIVEN,
        preferred_name: Optional[str] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        risk_rating: Optional[Literal["low", "medium", "high"]] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        wealth_and_employment_details: Optional[WealthAndEmploymentDetailsParam] | NotGiven = NOT_GIVEN,
        website: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LegalEntity:
        """
        Update a legal entity.

        Args:
          addresses: A list of addresses for the entity.

          business_name: The business's legal business name.

          citizenship_country: The country of citizenship for an individual.

          date_formed: A business's formation date (YYYY-MM-DD).

          date_of_birth: An individual's date of birth (YYYY-MM-DD).

          email: The entity's primary email.

          first_name: An individual's first name.

          identifications: A list of identifications for the legal entity.

          last_name: An individual's last name.

          legal_structure: The business's legal structure.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          middle_name: An individual's middle name.

          politically_exposed_person: Whether the individual is a politically exposed person.

          preferred_name: An individual's preferred name.

          prefix: An individual's prefix.

          risk_rating: The risk rating of the legal entity. One of low, medium, high.

          suffix: An individual's suffix.

          website: The entity's primary website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/legal_entities/{id}",
            body=maybe_transform(
                {
                    "addresses": addresses,
                    "bank_settings": bank_settings,
                    "business_name": business_name,
                    "citizenship_country": citizenship_country,
                    "date_formed": date_formed,
                    "date_of_birth": date_of_birth,
                    "doing_business_as_names": doing_business_as_names,
                    "email": email,
                    "first_name": first_name,
                    "identifications": identifications,
                    "last_name": last_name,
                    "legal_structure": legal_structure,
                    "metadata": metadata,
                    "middle_name": middle_name,
                    "phone_numbers": phone_numbers,
                    "politically_exposed_person": politically_exposed_person,
                    "preferred_name": preferred_name,
                    "prefix": prefix,
                    "risk_rating": risk_rating,
                    "suffix": suffix,
                    "wealth_and_employment_details": wealth_and_employment_details,
                    "website": website,
                },
                legal_entity_update_params.LegalEntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LegalEntity,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        legal_entity_type: Literal["business", "individual"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        show_deleted: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[LegalEntity]:
        """
        Get a list of all legal entities.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/legal_entities",
            page=SyncPage[LegalEntity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "legal_entity_type": legal_entity_type,
                        "metadata": metadata,
                        "per_page": per_page,
                        "show_deleted": show_deleted,
                    },
                    legal_entity_list_params.LegalEntityListParams,
                ),
            ),
            model=LegalEntity,
        )


class AsyncLegalEntities(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLegalEntitiesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLegalEntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLegalEntitiesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncLegalEntitiesWithStreamingResponse(self)

    async def create(
        self,
        *,
        legal_entity_type: Literal["business", "individual"],
        addresses: Iterable[legal_entity_create_params.Address] | NotGiven = NOT_GIVEN,
        bank_settings: Optional[BankSettingsParam] | NotGiven = NOT_GIVEN,
        business_name: Optional[str] | NotGiven = NOT_GIVEN,
        citizenship_country: Optional[str] | NotGiven = NOT_GIVEN,
        date_formed: Union[str, date, None] | NotGiven = NOT_GIVEN,
        date_of_birth: Union[str, date, None] | NotGiven = NOT_GIVEN,
        doing_business_as_names: List[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        identifications: Iterable[legal_entity_create_params.Identification] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        legal_entity_associations: Optional[Iterable[legal_entity_create_params.LegalEntityAssociation]]
        | NotGiven = NOT_GIVEN,
        legal_structure: Optional[
            Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        middle_name: Optional[str] | NotGiven = NOT_GIVEN,
        phone_numbers: Iterable[legal_entity_create_params.PhoneNumber] | NotGiven = NOT_GIVEN,
        politically_exposed_person: Optional[bool] | NotGiven = NOT_GIVEN,
        preferred_name: Optional[str] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        risk_rating: Optional[Literal["low", "medium", "high"]] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        wealth_and_employment_details: Optional[WealthAndEmploymentDetailsParam] | NotGiven = NOT_GIVEN,
        website: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LegalEntity:
        """
        create legal_entity

        Args:
          legal_entity_type: The type of legal entity.

          addresses: A list of addresses for the entity.

          business_name: The business's legal business name.

          citizenship_country: The country of citizenship for an individual.

          date_formed: A business's formation date (YYYY-MM-DD).

          date_of_birth: An individual's date of birth (YYYY-MM-DD).

          email: The entity's primary email.

          first_name: An individual's first name.

          identifications: A list of identifications for the legal entity.

          last_name: An individual's last name.

          legal_entity_associations: The legal entity associations and its child legal entities.

          legal_structure: The business's legal structure.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          middle_name: An individual's middle name.

          politically_exposed_person: Whether the individual is a politically exposed person.

          preferred_name: An individual's preferred name.

          prefix: An individual's prefix.

          risk_rating: The risk rating of the legal entity. One of low, medium, high.

          suffix: An individual's suffix.

          website: The entity's primary website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/legal_entities",
            body=await async_maybe_transform(
                {
                    "legal_entity_type": legal_entity_type,
                    "addresses": addresses,
                    "bank_settings": bank_settings,
                    "business_name": business_name,
                    "citizenship_country": citizenship_country,
                    "date_formed": date_formed,
                    "date_of_birth": date_of_birth,
                    "doing_business_as_names": doing_business_as_names,
                    "email": email,
                    "first_name": first_name,
                    "identifications": identifications,
                    "last_name": last_name,
                    "legal_entity_associations": legal_entity_associations,
                    "legal_structure": legal_structure,
                    "metadata": metadata,
                    "middle_name": middle_name,
                    "phone_numbers": phone_numbers,
                    "politically_exposed_person": politically_exposed_person,
                    "preferred_name": preferred_name,
                    "prefix": prefix,
                    "risk_rating": risk_rating,
                    "suffix": suffix,
                    "wealth_and_employment_details": wealth_and_employment_details,
                    "website": website,
                },
                legal_entity_create_params.LegalEntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LegalEntity,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LegalEntity:
        """
        Get details on a single legal entity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/legal_entities/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LegalEntity,
        )

    async def update(
        self,
        id: str,
        *,
        addresses: Iterable[legal_entity_update_params.Address] | NotGiven = NOT_GIVEN,
        bank_settings: Optional[BankSettingsParam] | NotGiven = NOT_GIVEN,
        business_name: Optional[str] | NotGiven = NOT_GIVEN,
        citizenship_country: Optional[str] | NotGiven = NOT_GIVEN,
        date_formed: Union[str, date, None] | NotGiven = NOT_GIVEN,
        date_of_birth: Union[str, date, None] | NotGiven = NOT_GIVEN,
        doing_business_as_names: List[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        identifications: Iterable[legal_entity_update_params.Identification] | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        legal_structure: Optional[
            Literal["corporation", "llc", "non_profit", "partnership", "sole_proprietorship", "trust"]
        ]
        | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        middle_name: Optional[str] | NotGiven = NOT_GIVEN,
        phone_numbers: Iterable[legal_entity_update_params.PhoneNumber] | NotGiven = NOT_GIVEN,
        politically_exposed_person: Optional[bool] | NotGiven = NOT_GIVEN,
        preferred_name: Optional[str] | NotGiven = NOT_GIVEN,
        prefix: Optional[str] | NotGiven = NOT_GIVEN,
        risk_rating: Optional[Literal["low", "medium", "high"]] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        wealth_and_employment_details: Optional[WealthAndEmploymentDetailsParam] | NotGiven = NOT_GIVEN,
        website: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LegalEntity:
        """
        Update a legal entity.

        Args:
          addresses: A list of addresses for the entity.

          business_name: The business's legal business name.

          citizenship_country: The country of citizenship for an individual.

          date_formed: A business's formation date (YYYY-MM-DD).

          date_of_birth: An individual's date of birth (YYYY-MM-DD).

          email: The entity's primary email.

          first_name: An individual's first name.

          identifications: A list of identifications for the legal entity.

          last_name: An individual's last name.

          legal_structure: The business's legal structure.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          middle_name: An individual's middle name.

          politically_exposed_person: Whether the individual is a politically exposed person.

          preferred_name: An individual's preferred name.

          prefix: An individual's prefix.

          risk_rating: The risk rating of the legal entity. One of low, medium, high.

          suffix: An individual's suffix.

          website: The entity's primary website URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/legal_entities/{id}",
            body=await async_maybe_transform(
                {
                    "addresses": addresses,
                    "bank_settings": bank_settings,
                    "business_name": business_name,
                    "citizenship_country": citizenship_country,
                    "date_formed": date_formed,
                    "date_of_birth": date_of_birth,
                    "doing_business_as_names": doing_business_as_names,
                    "email": email,
                    "first_name": first_name,
                    "identifications": identifications,
                    "last_name": last_name,
                    "legal_structure": legal_structure,
                    "metadata": metadata,
                    "middle_name": middle_name,
                    "phone_numbers": phone_numbers,
                    "politically_exposed_person": politically_exposed_person,
                    "preferred_name": preferred_name,
                    "prefix": prefix,
                    "risk_rating": risk_rating,
                    "suffix": suffix,
                    "wealth_and_employment_details": wealth_and_employment_details,
                    "website": website,
                },
                legal_entity_update_params.LegalEntityUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LegalEntity,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        legal_entity_type: Literal["business", "individual"] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        show_deleted: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LegalEntity, AsyncPage[LegalEntity]]:
        """
        Get a list of all legal entities.

        Args:
          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/legal_entities",
            page=AsyncPage[LegalEntity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "legal_entity_type": legal_entity_type,
                        "metadata": metadata,
                        "per_page": per_page,
                        "show_deleted": show_deleted,
                    },
                    legal_entity_list_params.LegalEntityListParams,
                ),
            ),
            model=LegalEntity,
        )


class LegalEntitiesWithRawResponse:
    def __init__(self, legal_entities: LegalEntities) -> None:
        self._legal_entities = legal_entities

        self.create = _legacy_response.to_raw_response_wrapper(
            legal_entities.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            legal_entities.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            legal_entities.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            legal_entities.list,
        )


class AsyncLegalEntitiesWithRawResponse:
    def __init__(self, legal_entities: AsyncLegalEntities) -> None:
        self._legal_entities = legal_entities

        self.create = _legacy_response.async_to_raw_response_wrapper(
            legal_entities.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            legal_entities.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            legal_entities.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            legal_entities.list,
        )


class LegalEntitiesWithStreamingResponse:
    def __init__(self, legal_entities: LegalEntities) -> None:
        self._legal_entities = legal_entities

        self.create = to_streamed_response_wrapper(
            legal_entities.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            legal_entities.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            legal_entities.update,
        )
        self.list = to_streamed_response_wrapper(
            legal_entities.list,
        )


class AsyncLegalEntitiesWithStreamingResponse:
    def __init__(self, legal_entities: AsyncLegalEntities) -> None:
        self._legal_entities = legal_entities

        self.create = async_to_streamed_response_wrapper(
            legal_entities.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            legal_entities.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            legal_entities.update,
        )
        self.list = async_to_streamed_response_wrapper(
            legal_entities.list,
        )
