# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    LegalEntity,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLegalEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        legal_entity = client.legal_entities.create(
            legal_entity_type="business",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        legal_entity = client.legal_entities.create(
            legal_entity_type="business",
            addresses=[
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
            bank_settings={
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
            business_name="business_name",
            citizenship_country="citizenship_country",
            compliance_details={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "issuer": "issuer",
                "live_mode": True,
                "object": "object",
                "token_expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "token_issued_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "token_url": "token_url",
                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "validated": True,
                "validated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            date_formed=parse_date("2019-12-27"),
            date_of_birth=parse_date("2019-12-27"),
            doing_business_as_names=["string"],
            email="email",
            first_name="first_name",
            identifications=[
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "expiration_date": parse_date("2019-12-27"),
                    "issuing_country": "issuing_country",
                    "issuing_region": "issuing_region",
                }
            ],
            industry_classifications=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "classification_codes": ["string"],
                    "classification_type": "anzsic",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "live_mode": True,
                    "object": "object",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            last_name="last_name",
            legal_entity_associations=[
                {
                    "relationship_types": ["authorized_signer"],
                    "child_legal_entity": {
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
                        "compliance_details": {
                            "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "issuer": "issuer",
                            "live_mode": True,
                            "object": "object",
                            "token_expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "token_issued_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "token_url": "token_url",
                            "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "validated": True,
                            "validated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        "date_formed": parse_date("2019-12-27"),
                        "date_of_birth": parse_date("2019-12-27"),
                        "doing_business_as_names": ["string"],
                        "email": "email",
                        "first_name": "first_name",
                        "identifications": [
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "expiration_date": parse_date("2019-12-27"),
                                "issuing_country": "issuing_country",
                                "issuing_region": "issuing_region",
                            }
                        ],
                        "industry_classifications": [
                            {
                                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                "classification_codes": ["string"],
                                "classification_type": "anzsic",
                                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "live_mode": True,
                                "object": "object",
                                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
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
                    "child_legal_entity_id": "child_legal_entity_id",
                    "ownership_percentage": 0,
                    "title": "title",
                }
            ],
            legal_structure="corporation",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            middle_name="middle_name",
            phone_numbers=[{"phone_number": "phone_number"}],
            politically_exposed_person=True,
            preferred_name="preferred_name",
            prefix="prefix",
            risk_rating="low",
            suffix="suffix",
            wealth_and_employment_details={
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
            website="website",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.legal_entities.with_raw_response.create(
            legal_entity_type="business",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity = response.parse()
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.legal_entities.with_streaming_response.create(
            legal_entity_type="business",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity = response.parse()
            assert_matches_type(LegalEntity, legal_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        legal_entity = client.legal_entities.retrieve(
            "id",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.legal_entities.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity = response.parse()
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.legal_entities.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity = response.parse()
            assert_matches_type(LegalEntity, legal_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.legal_entities.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        legal_entity = client.legal_entities.update(
            id="id",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        legal_entity = client.legal_entities.update(
            id="id",
            addresses=[
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
            bank_settings={
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
            business_name="business_name",
            citizenship_country="citizenship_country",
            compliance_details={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "issuer": "issuer",
                "live_mode": True,
                "object": "object",
                "token_expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "token_issued_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "token_url": "token_url",
                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "validated": True,
                "validated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            date_formed=parse_date("2019-12-27"),
            date_of_birth=parse_date("2019-12-27"),
            doing_business_as_names=["string"],
            email="email",
            first_name="first_name",
            identifications=[
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "expiration_date": parse_date("2019-12-27"),
                    "issuing_country": "issuing_country",
                    "issuing_region": "issuing_region",
                }
            ],
            industry_classifications=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "classification_codes": ["string"],
                    "classification_type": "anzsic",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "live_mode": True,
                    "object": "object",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            last_name="last_name",
            legal_structure="corporation",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            middle_name="middle_name",
            phone_numbers=[{"phone_number": "phone_number"}],
            politically_exposed_person=True,
            preferred_name="preferred_name",
            prefix="prefix",
            risk_rating="low",
            suffix="suffix",
            wealth_and_employment_details={
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
            website="website",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.legal_entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity = response.parse()
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.legal_entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity = response.parse()
            assert_matches_type(LegalEntity, legal_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.legal_entities.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        legal_entity = client.legal_entities.list()
        assert_matches_type(SyncPage[LegalEntity], legal_entity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        legal_entity = client.legal_entities.list(
            after_cursor="after_cursor",
            legal_entity_type="business",
            metadata={"foo": "string"},
            per_page=0,
            show_deleted="show_deleted",
        )
        assert_matches_type(SyncPage[LegalEntity], legal_entity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.legal_entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity = response.parse()
        assert_matches_type(SyncPage[LegalEntity], legal_entity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.legal_entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity = response.parse()
            assert_matches_type(SyncPage[LegalEntity], legal_entity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLegalEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        legal_entity = await async_client.legal_entities.create(
            legal_entity_type="business",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        legal_entity = await async_client.legal_entities.create(
            legal_entity_type="business",
            addresses=[
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
            bank_settings={
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
            business_name="business_name",
            citizenship_country="citizenship_country",
            compliance_details={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "issuer": "issuer",
                "live_mode": True,
                "object": "object",
                "token_expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "token_issued_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "token_url": "token_url",
                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "validated": True,
                "validated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            date_formed=parse_date("2019-12-27"),
            date_of_birth=parse_date("2019-12-27"),
            doing_business_as_names=["string"],
            email="email",
            first_name="first_name",
            identifications=[
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "expiration_date": parse_date("2019-12-27"),
                    "issuing_country": "issuing_country",
                    "issuing_region": "issuing_region",
                }
            ],
            industry_classifications=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "classification_codes": ["string"],
                    "classification_type": "anzsic",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "live_mode": True,
                    "object": "object",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            last_name="last_name",
            legal_entity_associations=[
                {
                    "relationship_types": ["authorized_signer"],
                    "child_legal_entity": {
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
                        "compliance_details": {
                            "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "issuer": "issuer",
                            "live_mode": True,
                            "object": "object",
                            "token_expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "token_issued_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "token_url": "token_url",
                            "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                            "validated": True,
                            "validated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                        },
                        "date_formed": parse_date("2019-12-27"),
                        "date_of_birth": parse_date("2019-12-27"),
                        "doing_business_as_names": ["string"],
                        "email": "email",
                        "first_name": "first_name",
                        "identifications": [
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "expiration_date": parse_date("2019-12-27"),
                                "issuing_country": "issuing_country",
                                "issuing_region": "issuing_region",
                            }
                        ],
                        "industry_classifications": [
                            {
                                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                                "classification_codes": ["string"],
                                "classification_type": "anzsic",
                                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                                "live_mode": True,
                                "object": "object",
                                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
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
                    "child_legal_entity_id": "child_legal_entity_id",
                    "ownership_percentage": 0,
                    "title": "title",
                }
            ],
            legal_structure="corporation",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            middle_name="middle_name",
            phone_numbers=[{"phone_number": "phone_number"}],
            politically_exposed_person=True,
            preferred_name="preferred_name",
            prefix="prefix",
            risk_rating="low",
            suffix="suffix",
            wealth_and_employment_details={
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
            website="website",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.legal_entities.with_raw_response.create(
            legal_entity_type="business",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity = response.parse()
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.legal_entities.with_streaming_response.create(
            legal_entity_type="business",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity = await response.parse()
            assert_matches_type(LegalEntity, legal_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        legal_entity = await async_client.legal_entities.retrieve(
            "id",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.legal_entities.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity = response.parse()
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.legal_entities.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity = await response.parse()
            assert_matches_type(LegalEntity, legal_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.legal_entities.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        legal_entity = await async_client.legal_entities.update(
            id="id",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        legal_entity = await async_client.legal_entities.update(
            id="id",
            addresses=[
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
            bank_settings={
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
            business_name="business_name",
            citizenship_country="citizenship_country",
            compliance_details={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "issuer": "issuer",
                "live_mode": True,
                "object": "object",
                "token_expires_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "token_issued_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "token_url": "token_url",
                "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "validated": True,
                "validated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            date_formed=parse_date("2019-12-27"),
            date_of_birth=parse_date("2019-12-27"),
            doing_business_as_names=["string"],
            email="email",
            first_name="first_name",
            identifications=[
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "expiration_date": parse_date("2019-12-27"),
                    "issuing_country": "issuing_country",
                    "issuing_region": "issuing_region",
                }
            ],
            industry_classifications=[
                {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "classification_codes": ["string"],
                    "classification_type": "anzsic",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "discarded_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "live_mode": True,
                    "object": "object",
                    "updated_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                }
            ],
            last_name="last_name",
            legal_structure="corporation",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            middle_name="middle_name",
            phone_numbers=[{"phone_number": "phone_number"}],
            politically_exposed_person=True,
            preferred_name="preferred_name",
            prefix="prefix",
            risk_rating="low",
            suffix="suffix",
            wealth_and_employment_details={
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
            website="website",
        )
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.legal_entities.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity = response.parse()
        assert_matches_type(LegalEntity, legal_entity, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.legal_entities.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity = await response.parse()
            assert_matches_type(LegalEntity, legal_entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.legal_entities.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        legal_entity = await async_client.legal_entities.list()
        assert_matches_type(AsyncPage[LegalEntity], legal_entity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        legal_entity = await async_client.legal_entities.list(
            after_cursor="after_cursor",
            legal_entity_type="business",
            metadata={"foo": "string"},
            per_page=0,
            show_deleted="show_deleted",
        )
        assert_matches_type(AsyncPage[LegalEntity], legal_entity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.legal_entities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        legal_entity = response.parse()
        assert_matches_type(AsyncPage[LegalEntity], legal_entity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.legal_entities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            legal_entity = await response.parse()
            assert_matches_type(AsyncPage[LegalEntity], legal_entity, path=["response"])

        assert cast(Any, response.is_closed) is True
