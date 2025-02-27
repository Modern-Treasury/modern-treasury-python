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
            name="name",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.create(
            name="name",
            accounting={"type": "customer"},
            accounts=[
                {
                    "account_details": [
                        {
                            "account_number": "account_number",
                            "account_number_type": "au_number",
                        }
                    ],
                    "account_type": "cash",
                    "contact_details": [
                        {
                            "contact_identifier": "contact_identifier",
                            "contact_identifier_type": "email",
                        }
                    ],
                    "ledger_account": {
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "name": "name",
                    "party_address": {
                        "country": "country",
                        "line1": "line1",
                        "line2": "line2",
                        "locality": "locality",
                        "postal_code": "postal_code",
                        "region": "region",
                    },
                    "party_identifier": "party_identifier",
                    "party_name": "party_name",
                    "party_type": "business",
                    "plaid_processor_token": "plaid_processor_token",
                    "routing_details": [
                        {
                            "routing_number": "routing_number",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        }
                    ],
                }
            ],
            email="dev@stainless.com",
            ledger_type="customer",
            legal_entity={
                "legal_entity_type": "business",
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
                "legal_entity_associations": [
                    {
                        "relationship_types": ["beneficial_owner"],
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
                        "child_legal_entity_id": "child_legal_entity_id",
                        "ownership_percentage": 0,
                        "title": "title",
                    }
                ],
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
            legal_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            send_remittance_advice=True,
            taxpayer_identifier="taxpayer_identifier",
            verification_status="denied",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = response.parse()
            assert_matches_type(Counterparty, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.retrieve(
            "id",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.retrieve(
            "id",
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
            id="id",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.update(
            id="id",
            email="dev@stainless.com",
            legal_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            name="name",
            send_remittance_advice=True,
            taxpayer_identifier="taxpayer_identifier",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.update(
            id="id",
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
                id="",
            )

    @parametrize
    def test_method_list(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.list()
        assert_matches_type(SyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.list(
            after_cursor="after_cursor",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="dev@stainless.com",
            legal_entity_id="legal_entity_id",
            metadata={"foo": "string"},
            name="name",
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
            "id",
        )
        assert counterparty is None

    @parametrize
    def test_raw_response_delete(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert counterparty is None

    @parametrize
    def test_streaming_response_delete(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.delete(
            "id",
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
            id="id",
            direction="credit",
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    def test_method_collect_account_with_all_params(self, client: ModernTreasury) -> None:
        counterparty = client.counterparties.collect_account(
            id="id",
            direction="credit",
            custom_redirect="https://example.com",
            fields=["name"],
            send_email=True,
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    def test_raw_response_collect_account(self, client: ModernTreasury) -> None:
        response = client.counterparties.with_raw_response.collect_account(
            id="id",
            direction="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    def test_streaming_response_collect_account(self, client: ModernTreasury) -> None:
        with client.counterparties.with_streaming_response.collect_account(
            id="id",
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
                id="",
                direction="credit",
            )


class TestAsyncCounterparties:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.create(
            name="name",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.create(
            name="name",
            accounting={"type": "customer"},
            accounts=[
                {
                    "account_details": [
                        {
                            "account_number": "account_number",
                            "account_number_type": "au_number",
                        }
                    ],
                    "account_type": "cash",
                    "contact_details": [
                        {
                            "contact_identifier": "contact_identifier",
                            "contact_identifier_type": "email",
                        }
                    ],
                    "ledger_account": {
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
                    "metadata": {
                        "key": "value",
                        "foo": "bar",
                        "modern": "treasury",
                    },
                    "name": "name",
                    "party_address": {
                        "country": "country",
                        "line1": "line1",
                        "line2": "line2",
                        "locality": "locality",
                        "postal_code": "postal_code",
                        "region": "region",
                    },
                    "party_identifier": "party_identifier",
                    "party_name": "party_name",
                    "party_type": "business",
                    "plaid_processor_token": "plaid_processor_token",
                    "routing_details": [
                        {
                            "routing_number": "routing_number",
                            "routing_number_type": "aba",
                            "payment_type": "ach",
                        }
                    ],
                }
            ],
            email="dev@stainless.com",
            ledger_type="customer",
            legal_entity={
                "legal_entity_type": "business",
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
                "legal_entity_associations": [
                    {
                        "relationship_types": ["beneficial_owner"],
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
                        "child_legal_entity_id": "child_legal_entity_id",
                        "ownership_percentage": 0,
                        "title": "title",
                    }
                ],
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
            legal_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "key": "value",
                "foo": "bar",
                "modern": "treasury",
            },
            send_remittance_advice=True,
            taxpayer_identifier="taxpayer_identifier",
            verification_status="denied",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            counterparty = await response.parse()
            assert_matches_type(Counterparty, counterparty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.retrieve(
            "id",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.retrieve(
            "id",
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
            id="id",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.update(
            id="id",
            email="dev@stainless.com",
            legal_entity_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={"foo": "string"},
            name="name",
            send_remittance_advice=True,
            taxpayer_identifier="taxpayer_identifier",
        )
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(Counterparty, counterparty, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.update(
            id="id",
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
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.list()
        assert_matches_type(AsyncPage[Counterparty], counterparty, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.list(
            after_cursor="after_cursor",
            created_at_lower_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_upper_bound=parse_datetime("2019-12-27T18:11:19.117Z"),
            email="dev@stainless.com",
            legal_entity_id="legal_entity_id",
            metadata={"foo": "string"},
            name="name",
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
            "id",
        )
        assert counterparty is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert counterparty is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.delete(
            "id",
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
            id="id",
            direction="credit",
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    async def test_method_collect_account_with_all_params(self, async_client: AsyncModernTreasury) -> None:
        counterparty = await async_client.counterparties.collect_account(
            id="id",
            direction="credit",
            custom_redirect="https://example.com",
            fields=["name"],
            send_email=True,
        )
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    async def test_raw_response_collect_account(self, async_client: AsyncModernTreasury) -> None:
        response = await async_client.counterparties.with_raw_response.collect_account(
            id="id",
            direction="credit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        counterparty = response.parse()
        assert_matches_type(CounterpartyCollectAccountResponse, counterparty, path=["response"])

    @parametrize
    async def test_streaming_response_collect_account(self, async_client: AsyncModernTreasury) -> None:
        async with async_client.counterparties.with_streaming_response.collect_account(
            id="id",
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
                id="",
                direction="credit",
            )
