# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.pagination import SyncPage, AsyncPage
from modern_treasury.types.document import Document

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestDocuments:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        resource = client.documents.create(
            "cases",
            "string",
            file=b"raw file contents",
        )
        assert isinstance(resource, Document)

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.documents.create(
            "cases",
            "string",
            document_type="string",
            file=b"raw file contents",
        )
        assert isinstance(resource, Document)

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        resource = client.documents.retrieve(
            "cases",
            "string",
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Document)

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        resource = client.documents.list(
            "cases",
            "string",
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        resource = client.documents.list(
            "cases",
            "string",
            after_cursor="string",
            per_page=0,
        )
        assert isinstance(resource, SyncPage)


class TestAsyncDocuments:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    async def test_method_create(self, client: AsyncModernTreasury) -> None:
        resource = await client.documents.create(
            "cases",
            "string",
            file=b"raw file contents",
        )
        assert isinstance(resource, Document)

    @pytest.mark.skip(reason="file upload tests are broken on the Prism mock server")
    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.documents.create(
            "cases",
            "string",
            document_type="string",
            file=b"raw file contents",
        )
        assert isinstance(resource, Document)

    @parametrize
    async def test_method_retrieve(self, client: AsyncModernTreasury) -> None:
        resource = await client.documents.retrieve(
            "cases",
            "string",
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Document)

    @parametrize
    async def test_method_list(self, client: AsyncModernTreasury) -> None:
        resource = await client.documents.list(
            "cases",
            "string",
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncModernTreasury) -> None:
        resource = await client.documents.list(
            "cases",
            "string",
            after_cursor="string",
            per_page=0,
        )
        assert isinstance(resource, AsyncPage)
