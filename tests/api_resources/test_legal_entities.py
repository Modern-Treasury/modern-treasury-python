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
from modern_treasury._utils import parse_date
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
                    "address_types": ["business", "mailing", "other"],
                    "line2": "line2",
                },
                {
                    "country": "country",
                    "line1": "line1",
                    "locality": "locality",
                    "postal_code": "postal_code",
                    "region": "region",
                    "address_types": ["business", "mailing", "other"],
                    "line2": "line2",
                },
                {
                    "country": "country",
                    "line1": "line1",
                    "locality": "locality",
                    "postal_code": "postal_code",
                    "region": "region",
                    "address_types": ["business", "mailing", "other"],
                    "line2": "line2",
                },
            ],
            business_name="business_name",
            date_formed=parse_date("2019-12-27"),
            date_of_birth=parse_date("2019-12-27"),
            doing_business_as_names=["string", "string", "string"],
            email="email",
            first_name="first_name",
            identifications=[
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "issuing_country": "issuing_country",
                },
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "issuing_country": "issuing_country",
                },
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "issuing_country": "issuing_country",
                },
            ],
            last_name="last_name",
            legal_entity_associations=[
                {
                    "relationship_types": ["beneficial_owner", "control_person"],
                    "child_legal_entity": {
                        "addresses": [
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                        ],
                        "business_name": "business_name",
                        "date_formed": parse_date("2019-12-27"),
                        "date_of_birth": parse_date("2019-12-27"),
                        "doing_business_as_names": ["string", "string", "string"],
                        "email": "email",
                        "first_name": "first_name",
                        "identifications": [
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                        ],
                        "last_name": "last_name",
                        "legal_entity_type": "business",
                        "legal_structure": "corporation",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                        "phone_numbers": [
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                        ],
                        "risk_rating": "low",
                        "website": "website",
                    },
                    "child_legal_entity_id": "child_legal_entity_id",
                    "ownership_percentage": 0,
                    "title": "title",
                },
                {
                    "relationship_types": ["beneficial_owner", "control_person"],
                    "child_legal_entity": {
                        "addresses": [
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                        ],
                        "business_name": "business_name",
                        "date_formed": parse_date("2019-12-27"),
                        "date_of_birth": parse_date("2019-12-27"),
                        "doing_business_as_names": ["string", "string", "string"],
                        "email": "email",
                        "first_name": "first_name",
                        "identifications": [
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                        ],
                        "last_name": "last_name",
                        "legal_entity_type": "business",
                        "legal_structure": "corporation",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                        "phone_numbers": [
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                        ],
                        "risk_rating": "low",
                        "website": "website",
                    },
                    "child_legal_entity_id": "child_legal_entity_id",
                    "ownership_percentage": 0,
                    "title": "title",
                },
                {
                    "relationship_types": ["beneficial_owner", "control_person"],
                    "child_legal_entity": {
                        "addresses": [
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                        ],
                        "business_name": "business_name",
                        "date_formed": parse_date("2019-12-27"),
                        "date_of_birth": parse_date("2019-12-27"),
                        "doing_business_as_names": ["string", "string", "string"],
                        "email": "email",
                        "first_name": "first_name",
                        "identifications": [
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                        ],
                        "last_name": "last_name",
                        "legal_entity_type": "business",
                        "legal_structure": "corporation",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                        "phone_numbers": [
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                        ],
                        "risk_rating": "low",
                        "website": "website",
                    },
                    "child_legal_entity_id": "child_legal_entity_id",
                    "ownership_percentage": 0,
                    "title": "title",
                },
            ],
            legal_structure="corporation",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            phone_numbers=[
                {"phone_number": "phone_number"},
                {"phone_number": "phone_number"},
                {"phone_number": "phone_number"},
            ],
            risk_rating="low",
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
            business_name="business_name",
            date_formed=parse_date("2019-12-27"),
            date_of_birth=parse_date("2019-12-27"),
            doing_business_as_names=["string", "string", "string"],
            email="email",
            first_name="first_name",
            last_name="last_name",
            legal_structure="corporation",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            phone_numbers=[
                {"phone_number": "phone_number"},
                {"phone_number": "phone_number"},
                {"phone_number": "phone_number"},
            ],
            risk_rating="low",
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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

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
                    "address_types": ["business", "mailing", "other"],
                    "line2": "line2",
                },
                {
                    "country": "country",
                    "line1": "line1",
                    "locality": "locality",
                    "postal_code": "postal_code",
                    "region": "region",
                    "address_types": ["business", "mailing", "other"],
                    "line2": "line2",
                },
                {
                    "country": "country",
                    "line1": "line1",
                    "locality": "locality",
                    "postal_code": "postal_code",
                    "region": "region",
                    "address_types": ["business", "mailing", "other"],
                    "line2": "line2",
                },
            ],
            business_name="business_name",
            date_formed=parse_date("2019-12-27"),
            date_of_birth=parse_date("2019-12-27"),
            doing_business_as_names=["string", "string", "string"],
            email="email",
            first_name="first_name",
            identifications=[
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "issuing_country": "issuing_country",
                },
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "issuing_country": "issuing_country",
                },
                {
                    "id_number": "id_number",
                    "id_type": "ar_cuil",
                    "issuing_country": "issuing_country",
                },
            ],
            last_name="last_name",
            legal_entity_associations=[
                {
                    "relationship_types": ["beneficial_owner", "control_person"],
                    "child_legal_entity": {
                        "addresses": [
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                        ],
                        "business_name": "business_name",
                        "date_formed": parse_date("2019-12-27"),
                        "date_of_birth": parse_date("2019-12-27"),
                        "doing_business_as_names": ["string", "string", "string"],
                        "email": "email",
                        "first_name": "first_name",
                        "identifications": [
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                        ],
                        "last_name": "last_name",
                        "legal_entity_type": "business",
                        "legal_structure": "corporation",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                        "phone_numbers": [
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                        ],
                        "risk_rating": "low",
                        "website": "website",
                    },
                    "child_legal_entity_id": "child_legal_entity_id",
                    "ownership_percentage": 0,
                    "title": "title",
                },
                {
                    "relationship_types": ["beneficial_owner", "control_person"],
                    "child_legal_entity": {
                        "addresses": [
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                        ],
                        "business_name": "business_name",
                        "date_formed": parse_date("2019-12-27"),
                        "date_of_birth": parse_date("2019-12-27"),
                        "doing_business_as_names": ["string", "string", "string"],
                        "email": "email",
                        "first_name": "first_name",
                        "identifications": [
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                        ],
                        "last_name": "last_name",
                        "legal_entity_type": "business",
                        "legal_structure": "corporation",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                        "phone_numbers": [
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                        ],
                        "risk_rating": "low",
                        "website": "website",
                    },
                    "child_legal_entity_id": "child_legal_entity_id",
                    "ownership_percentage": 0,
                    "title": "title",
                },
                {
                    "relationship_types": ["beneficial_owner", "control_person"],
                    "child_legal_entity": {
                        "addresses": [
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                            {
                                "country": "country",
                                "line1": "line1",
                                "locality": "locality",
                                "postal_code": "postal_code",
                                "region": "region",
                                "address_types": ["business", "mailing", "other"],
                                "line2": "line2",
                            },
                        ],
                        "business_name": "business_name",
                        "date_formed": parse_date("2019-12-27"),
                        "date_of_birth": parse_date("2019-12-27"),
                        "doing_business_as_names": ["string", "string", "string"],
                        "email": "email",
                        "first_name": "first_name",
                        "identifications": [
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                            {
                                "id_number": "id_number",
                                "id_type": "ar_cuil",
                                "issuing_country": "issuing_country",
                            },
                        ],
                        "last_name": "last_name",
                        "legal_entity_type": "business",
                        "legal_structure": "corporation",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                        "phone_numbers": [
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                            {"phone_number": "phone_number"},
                        ],
                        "risk_rating": "low",
                        "website": "website",
                    },
                    "child_legal_entity_id": "child_legal_entity_id",
                    "ownership_percentage": 0,
                    "title": "title",
                },
            ],
            legal_structure="corporation",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            phone_numbers=[
                {"phone_number": "phone_number"},
                {"phone_number": "phone_number"},
                {"phone_number": "phone_number"},
            ],
            risk_rating="low",
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
            business_name="business_name",
            date_formed=parse_date("2019-12-27"),
            date_of_birth=parse_date("2019-12-27"),
            doing_business_as_names=["string", "string", "string"],
            email="email",
            first_name="first_name",
            last_name="last_name",
            legal_structure="corporation",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            phone_numbers=[
                {"phone_number": "phone_number"},
                {"phone_number": "phone_number"},
                {"phone_number": "phone_number"},
            ],
            risk_rating="low",
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
