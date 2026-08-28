# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .. import _legacy_response
from ..types import virtual_account_setting_list_params, virtual_account_setting_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.virtual_account_setting import VirtualAccountSetting

__all__ = ["VirtualAccountSettings", "AsyncVirtualAccountSettings"]


class VirtualAccountSettings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VirtualAccountSettingsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return VirtualAccountSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VirtualAccountSettingsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return VirtualAccountSettingsWithStreamingResponse(self)

    def create(
        self,
        *,
        allocation_type: str,
        internal_account_id: str,
        allocation_identifier: Optional[str] | Omit = omit,
        allocation_length: Optional[int] | Omit = omit,
        allocation_range_end: Optional[str] | Omit = omit,
        allocation_range_start: Optional[str] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        generated_allocation_identifier_length: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VirtualAccountSetting:
        """
        Create a virtual account setting.

        Args:
          allocation_type: The method used to allocate virtual account numbers.

          internal_account_id: The ID of the internal account for the virtual account setting.

          allocation_identifier: The prefix, suffix, or bank-assigned identifier for the virtual account numbers.

          allocation_length: The total length of generated virtual account numbers.

          allocation_range_end: The inclusive end of the virtual account number range.

          allocation_range_start: The inclusive start of the virtual account number range.

          external_id: A user-defined identifier for the virtual account setting.

          generated_allocation_identifier_length: The length of a generated virtual account setting prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/virtual_account_settings",
            body=maybe_transform(
                {
                    "allocation_type": allocation_type,
                    "internal_account_id": internal_account_id,
                    "allocation_identifier": allocation_identifier,
                    "allocation_length": allocation_length,
                    "allocation_range_end": allocation_range_end,
                    "allocation_range_start": allocation_range_start,
                    "external_id": external_id,
                    "generated_allocation_identifier_length": generated_allocation_identifier_length,
                },
                virtual_account_setting_create_params.VirtualAccountSettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=VirtualAccountSetting,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        external_id: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPage[VirtualAccountSetting]:
        """
        List virtual account settings.

        Args:
          external_id: A user-defined identifier for the virtual account setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/virtual_account_settings",
            page=SyncPage[VirtualAccountSetting],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "external_id": external_id,
                        "per_page": per_page,
                    },
                    virtual_account_setting_list_params.VirtualAccountSettingListParams,
                ),
            ),
            model=VirtualAccountSetting,
        )


class AsyncVirtualAccountSettings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVirtualAccountSettingsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVirtualAccountSettingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVirtualAccountSettingsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Modern-Treasury/modern-treasury-python#with_streaming_response
        """
        return AsyncVirtualAccountSettingsWithStreamingResponse(self)

    async def create(
        self,
        *,
        allocation_type: str,
        internal_account_id: str,
        allocation_identifier: Optional[str] | Omit = omit,
        allocation_length: Optional[int] | Omit = omit,
        allocation_range_end: Optional[str] | Omit = omit,
        allocation_range_start: Optional[str] | Omit = omit,
        external_id: Optional[str] | Omit = omit,
        generated_allocation_identifier_length: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> VirtualAccountSetting:
        """
        Create a virtual account setting.

        Args:
          allocation_type: The method used to allocate virtual account numbers.

          internal_account_id: The ID of the internal account for the virtual account setting.

          allocation_identifier: The prefix, suffix, or bank-assigned identifier for the virtual account numbers.

          allocation_length: The total length of generated virtual account numbers.

          allocation_range_end: The inclusive end of the virtual account number range.

          allocation_range_start: The inclusive start of the virtual account number range.

          external_id: A user-defined identifier for the virtual account setting.

          generated_allocation_identifier_length: The length of a generated virtual account setting prefix.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/virtual_account_settings",
            body=await async_maybe_transform(
                {
                    "allocation_type": allocation_type,
                    "internal_account_id": internal_account_id,
                    "allocation_identifier": allocation_identifier,
                    "allocation_length": allocation_length,
                    "allocation_range_end": allocation_range_end,
                    "allocation_range_start": allocation_range_start,
                    "external_id": external_id,
                    "generated_allocation_identifier_length": generated_allocation_identifier_length,
                },
                virtual_account_setting_create_params.VirtualAccountSettingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=VirtualAccountSetting,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | Omit = omit,
        external_id: str | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VirtualAccountSetting, AsyncPage[VirtualAccountSetting]]:
        """
        List virtual account settings.

        Args:
          external_id: A user-defined identifier for the virtual account setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/virtual_account_settings",
            page=AsyncPage[VirtualAccountSetting],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_cursor": after_cursor,
                        "external_id": external_id,
                        "per_page": per_page,
                    },
                    virtual_account_setting_list_params.VirtualAccountSettingListParams,
                ),
            ),
            model=VirtualAccountSetting,
        )


class VirtualAccountSettingsWithRawResponse:
    def __init__(self, virtual_account_settings: VirtualAccountSettings) -> None:
        self._virtual_account_settings = virtual_account_settings

        self.create = _legacy_response.to_raw_response_wrapper(
            virtual_account_settings.create,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            virtual_account_settings.list,
        )


class AsyncVirtualAccountSettingsWithRawResponse:
    def __init__(self, virtual_account_settings: AsyncVirtualAccountSettings) -> None:
        self._virtual_account_settings = virtual_account_settings

        self.create = _legacy_response.async_to_raw_response_wrapper(
            virtual_account_settings.create,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            virtual_account_settings.list,
        )


class VirtualAccountSettingsWithStreamingResponse:
    def __init__(self, virtual_account_settings: VirtualAccountSettings) -> None:
        self._virtual_account_settings = virtual_account_settings

        self.create = to_streamed_response_wrapper(
            virtual_account_settings.create,
        )
        self.list = to_streamed_response_wrapper(
            virtual_account_settings.list,
        )


class AsyncVirtualAccountSettingsWithStreamingResponse:
    def __init__(self, virtual_account_settings: AsyncVirtualAccountSettings) -> None:
        self._virtual_account_settings = virtual_account_settings

        self.create = async_to_streamed_response_wrapper(
            virtual_account_settings.create,
        )
        self.list = async_to_streamed_response_wrapper(
            virtual_account_settings.list,
        )
