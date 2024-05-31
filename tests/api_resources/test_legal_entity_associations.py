# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LegalEntityAssociation
from modern_treasury._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLegalEntityAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        legal_entity_association = client.legal_entity_associations.create(
            parent_legal_entity_id="string",
            relationship_types=["beneficial_owner", "control_person"],
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        legal_entity_association = client.legal_entity_associations.create(
            parent_legal_entity_id="string",
            relationship_types=["beneficial_owner", "control_person"],
            child_legal_entity={
                "legal_entity_type": "business",
                "risk_rating": "low",
                "first_name": "string",
                "last_name": "string",
                "date_of_birth": parse_date("2019-12-27"),
                "date_formed": parse_date("2019-12-27"),
                "business_name": "string",
                "doing_business_as_names": ["string", "string", "string"],
                "legal_structure": "corporation",
                "phone_numbers": [{"phone_number": "string"}, {"phone_number": "string"}, {"phone_number": "string"}],
                "email": "string",
                "website": "string",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "addresses": [
                    {
                        "address_types": ["business", "mailing", "other"],
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    {
                        "address_types": ["business", "mailing", "other"],
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    {
                        "address_types": ["business", "mailing", "other"],
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                ],
                "identifications": [
                    {
                        "id_number": "string",
                        "id_type": "ar_cuil",
                        "issuing_country": "string",
                    },
                    {
                        "id_number": "string",
                        "id_type": "ar_cuil",
                        "issuing_country": "string",
                    },
                    {
                        "id_number": "string",
                        "id_type": "ar_cuil",
                        "issuing_country": "string",
                    },
                ],
            },
            child_legal_entity_id="string",
            ownership_percentage=0,
            title="string",
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.legal_entity_associations.with_raw_response.create(
            parent_legal_entity_id="string",
            relationship_types=["beneficial_owner", "control_person"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity_association = response.parse()
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.legal_entity_associations.with_streaming_response.create(
            parent_legal_entity_id="string",
            relationship_types=["beneficial_owner", "control_person"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity_association = response.parse()
            assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLegalEntityAssociations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        legal_entity_association = await async_client.legal_entity_associations.create(
            parent_legal_entity_id="string",
            relationship_types=["beneficial_owner", "control_person"],
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        legal_entity_association = await async_client.legal_entity_associations.create(
            parent_legal_entity_id="string",
            relationship_types=["beneficial_owner", "control_person"],
            child_legal_entity={
                "legal_entity_type": "business",
                "risk_rating": "low",
                "first_name": "string",
                "last_name": "string",
                "date_of_birth": parse_date("2019-12-27"),
                "date_formed": parse_date("2019-12-27"),
                "business_name": "string",
                "doing_business_as_names": ["string", "string", "string"],
                "legal_structure": "corporation",
                "phone_numbers": [{"phone_number": "string"}, {"phone_number": "string"}, {"phone_number": "string"}],
                "email": "string",
                "website": "string",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "addresses": [
                    {
                        "address_types": ["business", "mailing", "other"],
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    {
                        "address_types": ["business", "mailing", "other"],
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    {
                        "address_types": ["business", "mailing", "other"],
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                ],
                "identifications": [
                    {
                        "id_number": "string",
                        "id_type": "ar_cuil",
                        "issuing_country": "string",
                    },
                    {
                        "id_number": "string",
                        "id_type": "ar_cuil",
                        "issuing_country": "string",
                    },
                    {
                        "id_number": "string",
                        "id_type": "ar_cuil",
                        "issuing_country": "string",
                    },
                ],
            },
            child_legal_entity_id="string",
            ownership_percentage=0,
            title="string",
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.legal_entity_associations.with_raw_response.create(
            parent_legal_entity_id="string",
            relationship_types=["beneficial_owner", "control_person"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity_association = response.parse()
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.legal_entity_associations.with_streaming_response.create(
            parent_legal_entity_id="string",
            relationship_types=["beneficial_owner", "control_person"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity_association = await response.parse()
            assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

        assert cast(Any, response.is_closed) is True
