# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import LegalEntityAssociation
from modern_treasury._utils import parse_date, parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLegalEntityAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        legal_entity_association = client.legal_entity_associations.create(
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["beneficial_owner"],
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        legal_entity_association = client.legal_entity_associations.create(
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["beneficial_owner"],
            child_legal_entity={
                "addresses": [
                    {
                        "country": "country",
                        "line1": "line1",
                        "locality": "locality",
                        "postal_code": "postal_code",
                        "region": "region",
                        "address_types": ["business"],
                        "line2": "line2",
                    }
                ],
                "bank_settings": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "backup_withholding_percentage": 0,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "enable_backup_withholding": True,
                    "live_mode": True,
                    "object": "object",
                    "privacy_opt_out": True,
                    "regulation_o": True,
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
                "business_name": "business_name",
                "citizenship_country": "citizenship_country",
                "date_formed": parse_date("2019-12-27"),
                "date_of_birth": parse_date("2019-12-27"),
                "doing_business_as_names": ["string"],
                "email": "email",
                "first_name": "first_name",
                "identifications": [
                    {
                        "id_number": "id_number",
                        "id_type": "ar_cuil",
                        "issuing_country": "issuing_country",
                    }
                ],
                "last_name": "last_name",
                "legal_entity_type": "business",
                "legal_structure": "corporation",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "middle_name": "middle_name",
                "phone_numbers": [{"phone_number": "phone_number"}],
                "politically_exposed_person": True,
                "preferred_name": "preferred_name",
                "prefix": "prefix",
                "risk_rating": "low",
                "suffix": "suffix",
                "wealth_and_employment_details": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "annual_income": 0,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "employer_country": "employer_country",
                    "employer_name": "employer_name",
                    "employer_state": "employer_state",
                    "employment_status": "employed",
                    "income_country": "income_country",
                    "income_source": "family_support",
                    "income_state": "income_state",
                    "industry": "accounting",
                    "live_mode": True,
                    "object": "object",
                    "occupation": "consulting",
                    "source_of_funds": "alimony",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "wealth_source": "business_sale",
                },
                "website": "website",
            },
            child_legal_entity_id="child_legal_entity_id",
            ownership_percentage=0,
            title="title",
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.legal_entity_associations.with_raw_response.create(
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["beneficial_owner"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity_association = response.parse()
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.legal_entity_associations.with_streaming_response.create(
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["beneficial_owner"],
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
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["beneficial_owner"],
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        legal_entity_association = await async_client.legal_entity_associations.create(
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["beneficial_owner"],
            child_legal_entity={
                "addresses": [
                    {
                        "country": "country",
                        "line1": "line1",
                        "locality": "locality",
                        "postal_code": "postal_code",
                        "region": "region",
                        "address_types": ["business"],
                        "line2": "line2",
                    }
                ],
                "bank_settings": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "backup_withholding_percentage": 0,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "enable_backup_withholding": True,
                    "live_mode": True,
                    "object": "object",
                    "privacy_opt_out": True,
                    "regulation_o": True,
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                },
                "business_name": "business_name",
                "citizenship_country": "citizenship_country",
                "date_formed": parse_date("2019-12-27"),
                "date_of_birth": parse_date("2019-12-27"),
                "doing_business_as_names": ["string"],
                "email": "email",
                "first_name": "first_name",
                "identifications": [
                    {
                        "id_number": "id_number",
                        "id_type": "ar_cuil",
                        "issuing_country": "issuing_country",
                    }
                ],
                "last_name": "last_name",
                "legal_entity_type": "business",
                "legal_structure": "corporation",
                "metadata": {
                    "key": "value",
                    "foo": "bar",
                    "modern": "treasury",
                },
                "middle_name": "middle_name",
                "phone_numbers": [{"phone_number": "phone_number"}],
                "politically_exposed_person": True,
                "preferred_name": "preferred_name",
                "prefix": "prefix",
                "risk_rating": "low",
                "suffix": "suffix",
                "wealth_and_employment_details": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "annual_income": 0,
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "employer_country": "employer_country",
                    "employer_name": "employer_name",
                    "employer_state": "employer_state",
                    "employment_status": "employed",
                    "income_country": "income_country",
                    "income_source": "family_support",
                    "income_state": "income_state",
                    "industry": "accounting",
                    "live_mode": True,
                    "object": "object",
                    "occupation": "consulting",
                    "source_of_funds": "alimony",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "wealth_source": "business_sale",
                },
                "website": "website",
            },
            child_legal_entity_id="child_legal_entity_id",
            ownership_percentage=0,
            title="title",
        )
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.legal_entity_associations.with_raw_response.create(
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["beneficial_owner"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity_association = response.parse()
        assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.legal_entity_associations.with_streaming_response.create(
            parent_legal_entity_id="parent_legal_entity_id",
            relationship_types=["beneficial_owner"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity_association = await response.parse()
            assert_matches_type(LegalEntityAssociation, legal_entity_association, path=["response"])

        assert cast(Any, response.is_closed) is True
