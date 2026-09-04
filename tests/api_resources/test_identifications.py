# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import Identification
from modern_treasury._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdentifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        identification = client.identifications.create(
            id_number="id_number",
            id_type="ar_cuil",
            legal_entity_id="legal_entity_id",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        identification = client.identifications.create(
            id_number="id_number",
            id_type="ar_cuil",
            legal_entity_id="legal_entity_id",
            documents=[
                {
                    "document_type": "articles_of_incorporation",
                    "file_data": "file_data",
                    "filename": "filename",
                }
            ],
            expiration_date=parse_date("2019-12-27"),
            issuing_country="issuing_country",
            issuing_region="issuing_region",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.identifications.with_raw_response.create(
            id_number="id_number",
            id_type="ar_cuil",
            legal_entity_id="legal_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identification = response.parse()
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.identifications.with_streaming_response.create(
            id_number="id_number",
            id_type="ar_cuil",
            legal_entity_id="legal_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identification = response.parse()
            assert_matches_type(Identification, identification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        identification = client.identifications.retrieve(
            "id",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.identifications.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identification = response.parse()
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.identifications.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identification = response.parse()
            assert_matches_type(Identification, identification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.identifications.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        identification = client.identifications.update(
            id="id",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        identification = client.identifications.update(
            id="id",
            expiration_date=parse_date("2019-12-27"),
            id_number="id_number",
            id_type="ar_cuil",
            issuing_country="issuing_country",
            issuing_region="issuing_region",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.identifications.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identification = response.parse()
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.identifications.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identification = response.parse()
            assert_matches_type(Identification, identification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.identifications.with_raw_response.update(
                id="",
            )


class TestAsyncIdentifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        identification = await async_client.identifications.create(
            id_number="id_number",
            id_type="ar_cuil",
            legal_entity_id="legal_entity_id",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        identification = await async_client.identifications.create(
            id_number="id_number",
            id_type="ar_cuil",
            legal_entity_id="legal_entity_id",
            documents=[
                {
                    "document_type": "articles_of_incorporation",
                    "file_data": "file_data",
                    "filename": "filename",
                }
            ],
            expiration_date=parse_date("2019-12-27"),
            issuing_country="issuing_country",
            issuing_region="issuing_region",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.identifications.with_raw_response.create(
            id_number="id_number",
            id_type="ar_cuil",
            legal_entity_id="legal_entity_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identification = response.parse()
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.identifications.with_streaming_response.create(
            id_number="id_number",
            id_type="ar_cuil",
            legal_entity_id="legal_entity_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identification = await response.parse()
            assert_matches_type(Identification, identification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        identification = await async_client.identifications.retrieve(
            "id",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.identifications.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identification = response.parse()
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.identifications.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identification = await response.parse()
            assert_matches_type(Identification, identification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.identifications.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        identification = await async_client.identifications.update(
            id="id",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        identification = await async_client.identifications.update(
            id="id",
            expiration_date=parse_date("2019-12-27"),
            id_number="id_number",
            id_type="ar_cuil",
            issuing_country="issuing_country",
            issuing_region="issuing_region",
        )
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.identifications.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identification = response.parse()
        assert_matches_type(Identification, identification, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.identifications.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identification = await response.parse()
            assert_matches_type(Identification, identification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.identifications.with_raw_response.update(
                id="",
            )
