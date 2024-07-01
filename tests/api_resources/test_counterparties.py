# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from modern_treasury import ModernTreasury, AsyncModernTreasury
from modern_treasury.types import (
    Counterparty,
    CounterpartyCollectAccountResponse,
)
from modern_treasury._utils import parse_date, parse_datetime
from modern_treasury.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCounterparties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.create(
            name="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.create(
            name="string",
            accounting={"type": "customer"},
            accounts=[
                {
                    "account_type": "cash",
                    "party_type": "business",
                    "party_address": {
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    "name": "string",
                    "account_details": [
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                    ],
                    "routing_details": [
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                    ],
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "party_name": "string",
                    "party_identifier": "string",
                    "ledger_account": {
                        "name": "string",
                        "description": "string",
                        "normal_balance": "credit",
                        "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "currency": "string",
                        "currency_exponent": 0,
                        "ledger_account_category_ids": [
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        ],
                        "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "ledgerable_type": "counterparty",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    "plaid_processor_token": "string",
                    "contact_details": [
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                    ],
                },
                {
                    "account_type": "cash",
                    "party_type": "business",
                    "party_address": {
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    "name": "string",
                    "account_details": [
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                    ],
                    "routing_details": [
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                    ],
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "party_name": "string",
                    "party_identifier": "string",
                    "ledger_account": {
                        "name": "string",
                        "description": "string",
                        "normal_balance": "credit",
                        "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "currency": "string",
                        "currency_exponent": 0,
                        "ledger_account_category_ids": [
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        ],
                        "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "ledgerable_type": "counterparty",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    "plaid_processor_token": "string",
                    "contact_details": [
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                    ],
                },
                {
                    "account_type": "cash",
                    "party_type": "business",
                    "party_address": {
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    "name": "string",
                    "account_details": [
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                    ],
                    "routing_details": [
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                    ],
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "party_name": "string",
                    "party_identifier": "string",
                    "ledger_account": {
                        "name": "string",
                        "description": "string",
                        "normal_balance": "credit",
                        "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "currency": "string",
                        "currency_exponent": 0,
                        "ledger_account_category_ids": [
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        ],
                        "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "ledgerable_type": "counterparty",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    "plaid_processor_token": "string",
                    "contact_details": [
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                    ],
                },
            ],
            email="dev@stainlessapi.com",
            ledger_type="customer",
            legal_entity={
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
                "legal_entity_associations": [
                    {
                        "relationship_types": ["beneficial_owner", "control_person"],
                        "title": "string",
                        "ownership_percentage": 0,
                        "child_legal_entity": {
                            "legal_entity_type": "business",
                            "risk_rating": "low",
                            "first_name": "string",
                            "last_name": "string",
                            "date_of_birth": parse_date("2019-12-27"),
                            "date_formed": parse_date("2019-12-27"),
                            "business_name": "string",
                            "doing_business_as_names": ["string", "string", "string"],
                            "legal_structure": "corporation",
                            "phone_numbers": [
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                            ],
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
                        "child_legal_entity_id": "string",
                    },
                    {
                        "relationship_types": ["beneficial_owner", "control_person"],
                        "title": "string",
                        "ownership_percentage": 0,
                        "child_legal_entity": {
                            "legal_entity_type": "business",
                            "risk_rating": "low",
                            "first_name": "string",
                            "last_name": "string",
                            "date_of_birth": parse_date("2019-12-27"),
                            "date_formed": parse_date("2019-12-27"),
                            "business_name": "string",
                            "doing_business_as_names": ["string", "string", "string"],
                            "legal_structure": "corporation",
                            "phone_numbers": [
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                            ],
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
                        "child_legal_entity_id": "string",
                    },
                    {
                        "relationship_types": ["beneficial_owner", "control_person"],
                        "title": "string",
                        "ownership_percentage": 0,
                        "child_legal_entity": {
                            "legal_entity_type": "business",
                            "risk_rating": "low",
                            "first_name": "string",
                            "last_name": "string",
                            "date_of_birth": parse_date("2019-12-27"),
                            "date_formed": parse_date("2019-12-27"),
                            "business_name": "string",
                            "doing_business_as_names": ["string", "string", "string"],
                            "legal_structure": "corporation",
                            "phone_numbers": [
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                            ],
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
                        "child_legal_entity_id": "string",
                    },
                ],
            },
            legal_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            send_remittance_advice=True,
            taxpayer_identifier="string",
            verification_status="denied",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = response.parse()
            assert_matches_type(Counterparty, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.retrieve(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = response.parse()
            assert_matches_type(Counterparty, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.counterparties.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.update(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.update(
            "string",
            email="dev@stainlessapi.com",
            legal_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            name="string",
            send_remittance_advice=True,
            taxpayer_identifier="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = response.parse()
            assert_matches_type(Counterparty, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.counterparties.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.list()
        assert_matches_type(SyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.list(
            after_cursor="string",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="dev@stainlessapi.com",
            legal_entity_id="string",
            metadata={"foo": "string"},
            name="string",
            per_page=0,
        )
        assert_matches_type(SyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(SyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = response.parse()
            assert_matches_type(SyncPage[Counterparty], counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.delete(
            "string",
        )
        assert counterparty is None

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert counterparty is None

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = response.parse()
            assert counterparty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.counterparties.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_collect_account(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.collect_account(
            "string",
            direction="credit",
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    def test_method_collect_account_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.collect_account(
            "string",
            direction="credit",
            custom_redirect="https://example.com",
            fields=["name", "nameOnAccount", "taxpayerIdentifier"],
            send_email=True,
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    def test_raw_response_collect_account(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.collect_account(
            "string",
            direction="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    def test_streaming_response_collect_account(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.collect_account(
            "string",
            direction="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = response.parse()
            assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_collect_account(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.counterparties.with_raw_response.collect_account(
                "",
                direction="credit",
            )


class TestAsyncCounterparties:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.create(
            name="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.create(
            name="string",
            accounting={"type": "customer"},
            accounts=[
                {
                    "account_type": "cash",
                    "party_type": "business",
                    "party_address": {
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    "name": "string",
                    "account_details": [
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                    ],
                    "routing_details": [
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                    ],
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "party_name": "string",
                    "party_identifier": "string",
                    "ledger_account": {
                        "name": "string",
                        "description": "string",
                        "normal_balance": "credit",
                        "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "currency": "string",
                        "currency_exponent": 0,
                        "ledger_account_category_ids": [
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        ],
                        "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "ledgerable_type": "counterparty",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    "plaid_processor_token": "string",
                    "contact_details": [
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                    ],
                },
                {
                    "account_type": "cash",
                    "party_type": "business",
                    "party_address": {
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    "name": "string",
                    "account_details": [
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                    ],
                    "routing_details": [
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                    ],
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "party_name": "string",
                    "party_identifier": "string",
                    "ledger_account": {
                        "name": "string",
                        "description": "string",
                        "normal_balance": "credit",
                        "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "currency": "string",
                        "currency_exponent": 0,
                        "ledger_account_category_ids": [
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        ],
                        "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "ledgerable_type": "counterparty",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    "plaid_processor_token": "string",
                    "contact_details": [
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                    ],
                },
                {
                    "account_type": "cash",
                    "party_type": "business",
                    "party_address": {
                        "line1": "string",
                        "line2": "string",
                        "locality": "string",
                        "region": "string",
                        "postal_code": "string",
                        "country": "string",
                    },
                    "name": "string",
                    "account_details": [
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                        {
                            "account_number": "string",
                            "account_number_type": "au_number",
                        },
                    ],
                    "routing_details": [
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                        {
                            "routing_number": "string",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        },
                    ],
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "party_name": "string",
                    "party_identifier": "string",
                    "ledger_account": {
                        "name": "string",
                        "description": "string",
                        "normal_balance": "credit",
                        "ledger_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "currency": "string",
                        "currency_exponent": 0,
                        "ledger_account_category_ids": [
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        ],
                        "ledgerable_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "ledgerable_type": "counterparty",
                        "metadata": {
                            "key": "value",
                            "foo": "bar",
                            "modern": "treasury",
                        },
                    },
                    "plaid_processor_token": "string",
                    "contact_details": [
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                        {
                            "contact_identifier": "string",
                            "contact_identifier_type": "email",
                        },
                    ],
                },
            ],
            email="dev@stainlessapi.com",
            ledger_type="customer",
            legal_entity={
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
                "legal_entity_associations": [
                    {
                        "relationship_types": ["beneficial_owner", "control_person"],
                        "title": "string",
                        "ownership_percentage": 0,
                        "child_legal_entity": {
                            "legal_entity_type": "business",
                            "risk_rating": "low",
                            "first_name": "string",
                            "last_name": "string",
                            "date_of_birth": parse_date("2019-12-27"),
                            "date_formed": parse_date("2019-12-27"),
                            "business_name": "string",
                            "doing_business_as_names": ["string", "string", "string"],
                            "legal_structure": "corporation",
                            "phone_numbers": [
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                            ],
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
                        "child_legal_entity_id": "string",
                    },
                    {
                        "relationship_types": ["beneficial_owner", "control_person"],
                        "title": "string",
                        "ownership_percentage": 0,
                        "child_legal_entity": {
                            "legal_entity_type": "business",
                            "risk_rating": "low",
                            "first_name": "string",
                            "last_name": "string",
                            "date_of_birth": parse_date("2019-12-27"),
                            "date_formed": parse_date("2019-12-27"),
                            "business_name": "string",
                            "doing_business_as_names": ["string", "string", "string"],
                            "legal_structure": "corporation",
                            "phone_numbers": [
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                            ],
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
                        "child_legal_entity_id": "string",
                    },
                    {
                        "relationship_types": ["beneficial_owner", "control_person"],
                        "title": "string",
                        "ownership_percentage": 0,
                        "child_legal_entity": {
                            "legal_entity_type": "business",
                            "risk_rating": "low",
                            "first_name": "string",
                            "last_name": "string",
                            "date_of_birth": parse_date("2019-12-27"),
                            "date_formed": parse_date("2019-12-27"),
                            "business_name": "string",
                            "doing_business_as_names": ["string", "string", "string"],
                            "legal_structure": "corporation",
                            "phone_numbers": [
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                                {"phone_number": "string"},
                            ],
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
                        "child_legal_entity_id": "string",
                    },
                ],
            },
            legal_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            send_remittance_advice=True,
            taxpayer_identifier="string",
            verification_status="denied",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = await response.parse()
            assert_matches_type(Counterparty, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.retrieve(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = await response.parse()
            assert_matches_type(Counterparty, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.counterparties.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.update(
            "string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.update(
            "string",
            email="dev@stainlessapi.com",
            legal_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            name="string",
            send_remittance_advice=True,
            taxpayer_identifier="string",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = await response.parse()
            assert_matches_type(Counterparty, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.counterparties.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.list()
        assert_matches_type(AsyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.list(
            after_cursor="string",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="dev@stainlessapi.com",
            legal_entity_id="string",
            metadata={"foo": "string"},
            name="string",
            per_page=0,
        )
        assert_matches_type(AsyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(AsyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = await response.parse()
            assert_matches_type(AsyncPage[Counterparty], counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.delete(
            "string",
        )
        assert counterparty is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert counterparty is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = await response.parse()
            assert counterparty is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.counterparties.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_collect_account(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.collect_account(
            "string",
            direction="credit",
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    async def test_method_collect_account_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.collect_account(
            "string",
            direction="credit",
            custom_redirect="https://example.com",
            fields=["name", "nameOnAccount", "taxpayerIdentifier"],
            send_email=True,
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_collect_account(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.collect_account(
            "string",
            direction="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    async def test_streaming_response_collect_account(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.collect_account(
            "string",
            direction="credit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = await response.parse()
            assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_collect_account(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.counterparties.with_raw_response.collect_account(
                "",
                direction="credit",
            )
