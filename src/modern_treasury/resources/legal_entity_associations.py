# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import LegalEntityAssociation, legal_entity_association_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["LegalEntityAssociations", "AsyncLegalEntityAssociations"]


class LegalEntityAssociations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LegalEntityAssociationsWithRawResponse:
        return LegalEntityAssociationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LegalEntityAssociationsWithStreamingResponse:
        return LegalEntityAssociationsWithStreamingResponse(self)

    def create(
        self,
        *,
        relationship_types: List[Literal["beneficial_owner", "control_person"]],
        associated_legal_entity: legal_entity_association_create_params.AssociatedLegalEntity | NotGiven = NOT_GIVEN,
        associated_legal_entity_id: str | NotGiven = NOT_GIVEN,
        associator_legal_entity_id: str | NotGiven = NOT_GIVEN,
        ownership_percentage: Optional[int] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LegalEntityAssociation:
        """
        create legal_entity_association

        Args:
          associated_legal_entity: The associated legal entity.

          associated_legal_entity_id: The ID of the associated legal entity.

          associator_legal_entity_id: The ID of the associator legal entity. This must be a business or joint legal
              entity.

          ownership_percentage: The associated entity's ownership percentage iff they are a beneficial owner.

          title: The job title of the associated entity at the associator entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/legal_entity_associations",
            body=maybe_transform(
                {
                    "relationship_types": relationship_types,
                    "associated_legal_entity": associated_legal_entity,
                    "associated_legal_entity_id": associated_legal_entity_id,
                    "associator_legal_entity_id": associator_legal_entity_id,
                    "ownership_percentage": ownership_percentage,
                    "title": title,
                },
                legal_entity_association_create_params.LegalEntityAssociationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LegalEntityAssociation,
        )


class AsyncLegalEntityAssociations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLegalEntityAssociationsWithRawResponse:
        return AsyncLegalEntityAssociationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLegalEntityAssociationsWithStreamingResponse:
        return AsyncLegalEntityAssociationsWithStreamingResponse(self)

    async def create(
        self,
        *,
        relationship_types: List[Literal["beneficial_owner", "control_person"]],
        associated_legal_entity: legal_entity_association_create_params.AssociatedLegalEntity | NotGiven = NOT_GIVEN,
        associated_legal_entity_id: str | NotGiven = NOT_GIVEN,
        associator_legal_entity_id: str | NotGiven = NOT_GIVEN,
        ownership_percentage: Optional[int] | NotGiven = NOT_GIVEN,
        title: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> LegalEntityAssociation:
        """
        create legal_entity_association

        Args:
          associated_legal_entity: The associated legal entity.

          associated_legal_entity_id: The ID of the associated legal entity.

          associator_legal_entity_id: The ID of the associator legal entity. This must be a business or joint legal
              entity.

          ownership_percentage: The associated entity's ownership percentage iff they are a beneficial owner.

          title: The job title of the associated entity at the associator entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/legal_entity_associations",
            body=await async_maybe_transform(
                {
                    "relationship_types": relationship_types,
                    "associated_legal_entity": associated_legal_entity,
                    "associated_legal_entity_id": associated_legal_entity_id,
                    "associator_legal_entity_id": associator_legal_entity_id,
                    "ownership_percentage": ownership_percentage,
                    "title": title,
                },
                legal_entity_association_create_params.LegalEntityAssociationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=LegalEntityAssociation,
        )


class LegalEntityAssociationsWithRawResponse:
    def __init__(self, legal_entity_associations: LegalEntityAssociations) -> None:
        self._legal_entity_associations = legal_entity_associations

        self.create = _legacy_response.to_raw_response_wrapper(
            legal_entity_associations.create,
        )


class AsyncLegalEntityAssociationsWithRawResponse:
    def __init__(self, legal_entity_associations: AsyncLegalEntityAssociations) -> None:
        self._legal_entity_associations = legal_entity_associations

        self.create = _legacy_response.async_to_raw_response_wrapper(
            legal_entity_associations.create,
        )


class LegalEntityAssociationsWithStreamingResponse:
    def __init__(self, legal_entity_associations: LegalEntityAssociations) -> None:
        self._legal_entity_associations = legal_entity_associations

        self.create = to_streamed_response_wrapper(
            legal_entity_associations.create,
        )


class AsyncLegalEntityAssociationsWithStreamingResponse:
    def __init__(self, legal_entity_associations: AsyncLegalEntityAssociations) -> None:
        self._legal_entity_associations = legal_entity_associations

        self.create = async_to_streamed_response_wrapper(
            legal_entity_associations.create,
        )
