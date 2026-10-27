# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import embeddable_flow_list_params, embeddable_flow_create_params, embeddable_flow_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.embeddable_flow import EmbeddableFlow

__all__ = ["EmbeddableFlows", "AsyncEmbeddableFlows"]


class EmbeddableFlows(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmbeddableFlowsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return EmbeddableFlowsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmbeddableFlowsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return EmbeddableFlowsWithStreamingResponse(self)

    def create(
        self,
        *,
        options: embeddable_flow_create_params.Options,
        template: Literal["legal_entity_onboarding", "account_collection", "payment"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EmbeddableFlow:
        """
        create embeddable_flow

        Args:
          options: The parameters for the selected template's flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/embeddable_flows",
            body=maybe_transform(
                {
                    "options": options,
                    "template": template,
                },
                embeddable_flow_create_params.EmbeddableFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EmbeddableFlow,
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
    ) -> EmbeddableFlow:
        """
        get embeddable_flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/embeddable_flows/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddableFlow,
        )

    def update(
        self,
        id: str,
        *,
        status: Literal["cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EmbeddableFlow:
        """update embeddable_flow

        Args:
          status: The updated status of the flow.

        Can only be used to mark the flow as
              `cancelled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/api/embeddable_flows/{id}", id=id),
            body=maybe_transform({"status": status}, embeddable_flow_update_params.EmbeddableFlowUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EmbeddableFlow,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        per_page: int | Omit = omit,
        status: str | Omit = omit,
        template: Literal["legal_entity_onboarding", "account_collection", "payment"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[EmbeddableFlow]:
        """
        list embeddable_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/embeddable_flows",
            page=SyncPage[EmbeddableFlow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "status": status,
                        "template": template,
                    },
                    embeddable_flow_list_params.EmbeddableFlowListParams,
                ),
            ),
            model=EmbeddableFlow,
        )


class AsyncEmbeddableFlows(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmbeddableFlowsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmbeddableFlowsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmbeddableFlowsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncEmbeddableFlowsWithStreamingResponse(self)

    async def create(
        self,
        *,
        options: embeddable_flow_create_params.Options,
        template: Literal["legal_entity_onboarding", "account_collection", "payment"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EmbeddableFlow:
        """
        create embeddable_flow

        Args:
          options: The parameters for the selected template's flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/embeddable_flows",
            body=await async_maybe_transform(
                {
                    "options": options,
                    "template": template,
                },
                embeddable_flow_create_params.EmbeddableFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EmbeddableFlow,
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
    ) -> EmbeddableFlow:
        """
        get embeddable_flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/embeddable_flows/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddableFlow,
        )

    async def update(
        self,
        id: str,
        *,
        status: Literal["cancelled"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> EmbeddableFlow:
        """update embeddable_flow

        Args:
          status: The updated status of the flow.

        Can only be used to mark the flow as
              `cancelled`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/api/embeddable_flows/{id}", id=id),
            body=await async_maybe_transform(
                {"status": status}, embeddable_flow_update_params.EmbeddableFlowUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=EmbeddableFlow,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        per_page: int | Omit = omit,
        status: str | Omit = omit,
        template: Literal["legal_entity_onboarding", "account_collection", "payment"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EmbeddableFlow, AsyncPage[EmbeddableFlow]]:
        """
        list embeddable_flows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/embeddable_flows",
            page=AsyncPage[EmbeddableFlow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "per_page": per_page,
                        "status": status,
                        "template": template,
                    },
                    embeddable_flow_list_params.EmbeddableFlowListParams,
                ),
            ),
            model=EmbeddableFlow,
        )


class EmbeddableFlowsWithRawResponse:
    def __init__(self, embeddable_flows: EmbeddableFlows) -> None:
        self._embeddable_flows = embeddable_flows

        self.create = _legacy_response.to_raw_response_wrapper(
            embeddable_flows.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            embeddable_flows.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            embeddable_flows.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            embeddable_flows.list,
        )


class AsyncEmbeddableFlowsWithRawResponse:
    def __init__(self, embeddable_flows: AsyncEmbeddableFlows) -> None:
        self._embeddable_flows = embeddable_flows

        self.create = _legacy_response.async_to_raw_response_wrapper(
            embeddable_flows.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            embeddable_flows.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            embeddable_flows.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            embeddable_flows.list,
        )


class EmbeddableFlowsWithStreamingResponse:
    def __init__(self, embeddable_flows: EmbeddableFlows) -> None:
        self._embeddable_flows = embeddable_flows

        self.create = to_streamed_response_wrapper(
            embeddable_flows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            embeddable_flows.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            embeddable_flows.update,
        )
        self.list = to_streamed_response_wrapper(
            embeddable_flows.list,
        )


class AsyncEmbeddableFlowsWithStreamingResponse:
    def __init__(self, embeddable_flows: AsyncEmbeddableFlows) -> None:
        self._embeddable_flows = embeddable_flows

        self.create = async_to_streamed_response_wrapper(
            embeddable_flows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            embeddable_flows.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            embeddable_flows.update,
        )
        self.list = async_to_streamed_response_wrapper(
            embeddable_flows.list,
        )
