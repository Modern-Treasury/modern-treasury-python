# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Mapping

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.parametrize(
        "payload,expected",
        [
            ("foo", "08ba357e274f528065766c770a639abf6809b39ccfd37c2a3157c7f51954da0a"),
            ('{"foo":"bar"}', "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"),
            ('{"foo":"bar","bar":"baz","a": true}', "ec1c86d16075e6937fc26d55b7dc60bac9b1178a2f714312f7c5cb13a319b0ac"),
            (
                '{"a":{"b":{"c":{"d":[null,1,true,false,["foo",{"bar":[true, false]}]]}}}}',
                "39b6fc0f5b02a5aefbdd7fb337245b4209036334e837d8c5b6a4092965ebc0a5",
            ),
        ],
    )
    def test_get_signature(self, payload: str, expected: str, client: ModernTreasury) -> None:
        sig = client.webhooks.get_signature(payload, key="foo")
        assert sig == expected

    def test_get_signature_key_not_set(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match="webhook key"):
            client.webhooks.get_signature("foo")

    def test_get_signature_client_key(self, client: ModernTreasury) -> None:
        client = client.__class__(
            base_url=base_url,
            api_key=client.api_key,
            organization_id="c40c0b40-11d3-42ee-8f2e-18ee8b8239aa",
            webhook_key="foo",
        )
        assert client.webhook_key == "foo"

        payload = '{"foo":"bar"}'
        sig = client.webhooks.get_signature(payload)
        assert sig == "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"

        other_sig = client.webhooks.get_signature(payload, key="bar")
        assert sig != other_sig

    def test_validate_signature_no_header(self, client: ModernTreasury) -> None:
        with pytest.raises(ValueError, match="Could not find X-Signature header"):
            client.webhooks.validate_signature("foo", headers={"foo": "bar"}, key="foo")

    def test_validate_signature(self, client: ModernTreasury) -> None:
        payload = '{"foo":"bar"}'
        result = client.webhooks.validate_signature(
            payload,
            headers={"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is True

        # lowercased header
        result = client.webhooks.validate_signature(
            payload,
            headers={"x-signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is True

        # modified payload
        result = client.webhooks.validate_signature(
            payload + "foo",
            headers={"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is False

        # modified signature
        result = client.webhooks.validate_signature(
            payload,
            headers={"X-Signature": "bar"},
            key="foo",
        )
        assert result is False

    def test_validate_signature_custom_headers_class(self, client: ModernTreasury) -> None:
        class Headers:
            def __init__(self, raw: Mapping[str, str]) -> None:
                self._raw = raw

            def get(self, key: str) -> str | None:
                return self._raw.get(key)

        result = client.webhooks.validate_signature(
            '{"foo":"bar"}',
            headers=Headers({"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"}),
            key="foo",
        )
        assert result is True

        with pytest.raises(ValueError, match="Could not find X-Signature header"):
            client.webhooks.validate_signature(
                '{"foo":"bar"}',
                headers=Headers({}),
                key="foo",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.parametrize(
        "payload,expected",
        [
            ("foo", "08ba357e274f528065766c770a639abf6809b39ccfd37c2a3157c7f51954da0a"),
            ('{"foo":"bar"}', "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"),
            ('{"foo":"bar","bar":"baz","a": true}', "ec1c86d16075e6937fc26d55b7dc60bac9b1178a2f714312f7c5cb13a319b0ac"),
            (
                '{"a":{"b":{"c":{"d":[null,1,true,false,["foo",{"bar":[true, false]}]]}}}}',
                "39b6fc0f5b02a5aefbdd7fb337245b4209036334e837d8c5b6a4092965ebc0a5",
            ),
        ],
    )
    def test_get_signature(self, payload: str, expected: str, async_client: AsyncModernTreasury) -> None:
        sig = async_client.webhooks.get_signature(payload, key="foo")
        assert sig == expected

    def test_get_signature_key_not_set(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match="webhook key"):
            async_client.webhooks.get_signature("foo")

    def test_get_signature_client_key(self, async_client: AsyncModernTreasury) -> None:
        client = async_client.__class__(
            base_url=base_url,
            api_key=async_client.api_key,
            organization_id="c40c0b40-11d3-42ee-8f2e-18ee8b8239aa",
            webhook_key="foo",
        )
        assert client.webhook_key == "foo"

        payload = '{"foo":"bar"}'
        sig = client.webhooks.get_signature(payload)
        assert sig == "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"

        other_sig = client.webhooks.get_signature(payload, key="bar")
        assert sig != other_sig

    def test_validate_signature_no_header(self, async_client: AsyncModernTreasury) -> None:
        with pytest.raises(ValueError, match="Could not find X-Signature header"):
            async_client.webhooks.validate_signature("foo", headers={"foo": "bar"}, key="foo")

    def test_validate_signature(self, async_client: AsyncModernTreasury) -> None:
        payload = '{"foo":"bar"}'
        result = async_client.webhooks.validate_signature(
            payload,
            headers={"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is True

        # lowercased header
        result = async_client.webhooks.validate_signature(
            payload,
            headers={"x-signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is True

        # modified payload
        result = async_client.webhooks.validate_signature(
            payload + "foo",
            headers={"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is False

        # modified signature
        result = async_client.webhooks.validate_signature(
            payload,
            headers={"X-Signature": "bar"},
            key="foo",
        )
        assert result is False

    def test_validate_signature_custom_headers_class(self, async_client: AsyncModernTreasury) -> None:
        class Headers:
            def __init__(self, raw: Mapping[str, str]) -> None:
                self._raw = raw

            def get(self, key: str) -> str | None:
                return self._raw.get(key)

        result = async_client.webhooks.validate_signature(
            '{"foo":"bar"}',
            headers=Headers({"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"}),
            key="foo",
        )
        assert result is True

        with pytest.raises(ValueError, match="Could not find X-Signature header"):
            async_client.webhooks.validate_signature(
                '{"foo":"bar"}',
                headers=Headers({}),
                key="foo",
            )
