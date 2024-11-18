# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    ExternalAccount,
    ExternalAccountVerifyResponse,
)
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_details=[
                {
                    "account_number": "account_number",
                    "account_number_type": "au_number",
                }
            ],
            account_type="cash",
            contact_details=[
                {
                    "contact_identifier": "contact_identifier",
                    "contact_identifier_type": "email",
                }
            ],
            ledger_account={
                "currency": "currency",
                "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "normal_balance": "credit",
                "currency_exponent": 0,
                "description": "description",
                "ledger_account_category_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "ledgerable_type": "counterparty",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
            },
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="name",
            party_address={
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
            },
            party_identifier="party_identifier",
            party_name="party_name",
            party_type="business",
            plaid_processor_token="plaid_processor_token",
            routing_details=[
                {
                    "routing_number": "routing_number",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                }
            ],
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.external_accounts.with_raw_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.external_accounts.with_streaming_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.retrieve(
            "id",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.external_accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.external_accounts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.update(
            id="id",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.update(
            id="id",
            account_type="cash",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            name="name",
            party_address={
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
            },
            party_name="party_name",
            party_type="business",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.external_accounts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.external_accounts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_accounts.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.list()
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            metadata={"foo": "string"},
            party_name="party_name",
            per_page=0,
        )
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.external_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.external_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(SyncPage[ExternalAccount], external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.delete(
            "id",
        )
        assert external_account is None

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.external_accounts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert external_account is None

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.external_accounts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert external_account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_accounts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_complete_verification(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.complete_verification(
            id="id",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_method_complete_verification_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.complete_verification(
            id="id",
            amounts=[2, 4],
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_raw_response_complete_verification(self, client: ModernTreasury) -> None:
        response = client.external_accounts.with_raw_response.complete_verification(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    def test_streaming_response_complete_verification(self, client: ModernTreasury) -> None:
        with client.external_accounts.with_streaming_response.complete_verification(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_complete_verification(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_accounts.with_raw_response.complete_verification(
                id="",
            )

    @parametrize
    def test_method_verify(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.verify(
            id="id",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
        )
        assert_matches_type(ExternalAccountVerifyResponse, external_account, path=["response"])

    @parametrize
    def test_method_verify_with_all_params(self, client: ModernTreasury) -> None:
        external_account = client.external_accounts.verify(
            id="id",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
            currency="AED",
            fallback_type="ach",
            priority="high",
        )
        assert_matches_type(ExternalAccountVerifyResponse, external_account, path=["response"])

    @parametrize
    def test_raw_response_verify(self, client: ModernTreasury) -> None:
        response = client.external_accounts.with_raw_response.verify(
            id="id",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccountVerifyResponse, external_account, path=["response"])

    @parametrize
    def test_streaming_response_verify(self, client: ModernTreasury) -> None:
        with client.external_accounts.with_streaming_response.verify(
            id="id",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = response.parse()
            assert_matches_type(ExternalAccountVerifyResponse, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_verify(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.external_accounts.with_raw_response.verify(
                id="",
                originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                payment_type="ach",
            )


class TestAsyncExternalAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_details=[
                {
                    "account_number": "account_number",
                    "account_number_type": "au_number",
                }
            ],
            account_type="cash",
            contact_details=[
                {
                    "contact_identifier": "contact_identifier",
                    "contact_identifier_type": "email",
                }
            ],
            ledger_account={
                "currency": "currency",
                "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "name": "name",
                "normal_balance": "credit",
                "currency_exponent": 0,
                "description": "description",
                "ledger_account_category_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "ledgerable_type": "counterparty",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
            },
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            name="name",
            party_address={
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
            },
            party_identifier="party_identifier",
            party_name="party_name",
            party_type="business",
            plaid_processor_token="plaid_processor_token",
            routing_details=[
                {
                    "routing_number": "routing_number",
                    "routing_number_type": "aba",
                    "payment_type": "ach",
                }
            ],
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.external_accounts.with_raw_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.external_accounts.with_streaming_response.create(
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.retrieve(
            "id",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.external_accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.external_accounts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.update(
            id="id",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.update(
            id="id",
            account_type="cash",
            counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            name="name",
            party_address={
                "country": "country",
                "line1": "line1",
                "line2": "line2",
                "locality": "locality",
                "postal_code": "postal_code",
                "region": "region",
            },
            party_name="party_name",
            party_type="business",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.external_accounts.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.external_accounts.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_accounts.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.list()
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.list(
            after_cursor="after_cursor",
            counterparty_id="counterparty_id",
            metadata={"foo": "string"},
            party_name="party_name",
            per_page=0,
        )
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.external_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.external_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(AsyncPage[ExternalAccount], external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.delete(
            "id",
        )
        assert external_account is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.external_accounts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert external_account is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.external_accounts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert external_account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_accounts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_complete_verification(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.complete_verification(
            id="id",
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_method_complete_verification_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.complete_verification(
            id="id",
            amounts=[2, 4],
        )
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_raw_response_complete_verification(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.external_accounts.with_raw_response.complete_verification(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccount, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_complete_verification(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.external_accounts.with_streaming_response.complete_verification(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccount, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete_verification(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_accounts.with_raw_response.complete_verification(
                id="",
            )

    @parametrize
    async def test_method_verify(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.verify(
            id="id",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
        )
        assert_matches_type(ExternalAccountVerifyResponse, external_account, path=["response"])

    @parametrize
    async def test_method_verify_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        external_account = await async_client.external_accounts.verify(
            id="id",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
            currency="AED",
            fallback_type="ach",
            priority="high",
        )
        assert_matches_type(ExternalAccountVerifyResponse, external_account, path=["response"])

    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.external_accounts.with_raw_response.verify(
            id="id",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_account = response.parse()
        assert_matches_type(ExternalAccountVerifyResponse, external_account, path=["response"])

    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.external_accounts.with_streaming_response.verify(
            id="id",
            originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="ach",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_account = await response.parse()
            assert_matches_type(ExternalAccountVerifyResponse, external_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_verify(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.external_accounts.with_raw_response.verify(
                id="",
                originating_account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                payment_type="ach",
            )
