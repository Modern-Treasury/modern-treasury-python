# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import AccountDetail
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        account_detail = client.account_details.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
        )
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        account_detail = client.account_details.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
            account_number_type="au_number",
        )
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.account_details.with_raw_response.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_detail = response.parse()
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.account_details.with_streaming_response.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_detail = response.parse()
            assert_matches_type(AccountDetail, account_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.account_details.with_raw_response.create(
                "",
                accounts_type="external_accounts",
                account_number="string",
            )

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        account_detail = client.account_details.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.account_details.with_raw_response.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_detail = response.parse()
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.account_details.with_streaming_response.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_detail = response.parse()
            assert_matches_type(AccountDetail, account_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.account_details.with_raw_response.retrieve(
                "string",
                accounts_type="external_accounts",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.account_details.with_raw_response.retrieve(
                "",
                accounts_type="external_accounts",
                account_id="string",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        account_detail = client.account_details.list(
            "string",
            accounts_type="external_accounts",
        )
        assert_matches_type(SyncPage[AccountDetail], account_detail, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        account_detail = client.account_details.list(
            "string",
            accounts_type="external_accounts",
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[AccountDetail], account_detail, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.account_details.with_raw_response.list(
            "string",
            accounts_type="external_accounts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_detail = response.parse()
        assert_matches_type(SyncPage[AccountDetail], account_detail, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.account_details.with_streaming_response.list(
            "string",
            accounts_type="external_accounts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_detail = response.parse()
            assert_matches_type(SyncPage[AccountDetail], account_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.account_details.with_raw_response.list(
                "",
                accounts_type="external_accounts",
            )

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        account_detail = client.account_details.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert account_detail is None

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.account_details.with_raw_response.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_detail = response.parse()
        assert account_detail is None

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.account_details.with_streaming_response.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_detail = response.parse()
            assert account_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.account_details.with_raw_response.delete(
                "string",
                accounts_type="external_accounts",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.account_details.with_raw_response.delete(
                "",
                accounts_type="external_accounts",
                account_id="string",
            )


class TestAsyncAccountDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        account_detail = await async_client.account_details.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
        )
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        account_detail = await async_client.account_details.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
            account_number_type="au_number",
        )
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.account_details.with_raw_response.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_detail = response.parse()
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.account_details.with_streaming_response.create(
            "string",
            accounts_type="external_accounts",
            account_number="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_detail = await response.parse()
            assert_matches_type(AccountDetail, account_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.account_details.with_raw_response.create(
                "",
                accounts_type="external_accounts",
                account_number="string",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        account_detail = await async_client.account_details.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.account_details.with_raw_response.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_detail = response.parse()
        assert_matches_type(AccountDetail, account_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.account_details.with_streaming_response.retrieve(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_detail = await response.parse()
            assert_matches_type(AccountDetail, account_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.account_details.with_raw_response.retrieve(
                "string",
                accounts_type="external_accounts",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.account_details.with_raw_response.retrieve(
                "",
                accounts_type="external_accounts",
                account_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        account_detail = await async_client.account_details.list(
            "string",
            accounts_type="external_accounts",
        )
        assert_matches_type(AsyncPage[AccountDetail], account_detail, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        account_detail = await async_client.account_details.list(
            "string",
            accounts_type="external_accounts",
            after_cursor="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[AccountDetail], account_detail, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.account_details.with_raw_response.list(
            "string",
            accounts_type="external_accounts",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_detail = response.parse()
        assert_matches_type(AsyncPage[AccountDetail], account_detail, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.account_details.with_streaming_response.list(
            "string",
            accounts_type="external_accounts",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_detail = await response.parse()
            assert_matches_type(AsyncPage[AccountDetail], account_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.account_details.with_raw_response.list(
                "",
                accounts_type="external_accounts",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        account_detail = await async_client.account_details.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )
        assert account_detail is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.account_details.with_raw_response.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_detail = response.parse()
        assert account_detail is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.account_details.with_streaming_response.delete(
            "string",
            accounts_type="external_accounts",
            account_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_detail = await response.parse()
            assert account_detail is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.account_details.with_raw_response.delete(
                "string",
                accounts_type="external_accounts",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.account_details.with_raw_response.delete(
                "",
                accounts_type="external_accounts",
                account_id="string",
            )
