# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LegalEntityAssociation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLegalEntityAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        legal_entity_association = client.legal_entity_associations.create(
            child_legal_entity_id="child_legal_entity_id",
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["authorized_signer"],
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        legal_entity_association = client.legal_entity_associations.create(
            child_legal_entity_id="child_legal_entity_id",
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["authorized_signer"],
            ownership_percentage=0,
            title="title",
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.legal_entity_associations.with_raw_response.create(
            child_legal_entity_id="child_legal_entity_id",
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["authorized_signer"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity_association = response.parse()
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.legal_entity_associations.with_streaming_response.create(
            child_legal_entity_id="child_legal_entity_id",
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["authorized_signer"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity_association = response.parse()
            assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        legal_entity_association = client.legal_entity_associations.delete(
            "id",
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.legal_entity_associations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity_association = response.parse()
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.legal_entity_associations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity_association = response.parse()
            assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.legal_entity_associations.with_raw_response.delete(
                "",
            )


class TestAsyncLegalEntityAssociations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        legal_entity_association = await async_client.legal_entity_associations.create(
            child_legal_entity_id="child_legal_entity_id",
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["authorized_signer"],
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        legal_entity_association = await async_client.legal_entity_associations.create(
            child_legal_entity_id="child_legal_entity_id",
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["authorized_signer"],
            ownership_percentage=0,
            title="title",
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.legal_entity_associations.with_raw_response.create(
            child_legal_entity_id="child_legal_entity_id",
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["authorized_signer"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity_association = response.parse()
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.legal_entity_associations.with_streaming_response.create(
            child_legal_entity_id="child_legal_entity_id",
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["authorized_signer"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity_association = await response.parse()
            assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        legal_entity_association = await async_client.legal_entity_associations.delete(
            "id",
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.legal_entity_associations.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity_association = response.parse()
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.legal_entity_associations.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity_association = await response.parse()
            assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.legal_entity_associations.with_raw_response.delete(
                "",
            )
