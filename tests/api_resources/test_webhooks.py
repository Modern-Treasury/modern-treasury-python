# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Mapping

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestWebhooks:
    strict_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = ModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
    def test_get_signature(self, payload: str, expected: str) -> None:
        sig = self.strict_client.webhooks.get_signature(payload, key="foo")
        assert sig == expected

    def test_get_signature_key_not_set(self) -> None:
        with pytest.raises(ValueError, match="webhook key"):
            self.strict_client.webhooks.get_signature("foo")

    def test_get_signature_client_key(self) -> None:
        client = self.strict_client.__class__(
            base_url=base_url,
            api_key=api_key,
            organization_id="c40c0b40-11d3-42ee-8f2e-18ee8b8239aa",
            webhook_key="foo",
        )
        assert client.webhook_key == "foo"

        payload = '{"foo":"bar"}'
        sig = client.webhooks.get_signature(payload)
        assert sig == "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"

        other_sig = client.webhooks.get_signature(payload, key="bar")
        assert sig != other_sig

    def test_validate_signature_no_header(self) -> None:
        with pytest.raises(ValueError, match="Could not find an X-Signature header"):
            self.strict_client.webhooks.validate_signature("foo", headers={"foo": "bar"}, key="foo")

    def test_validate_signature(self) -> None:
        payload = '{"foo":"bar"}'
        result = self.strict_client.webhooks.validate_signature(
            payload,
            headers={"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is True

        # lowercased header
        result = self.strict_client.webhooks.validate_signature(
            payload,
            headers={"x-signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is True

        # modified payload
        result = self.strict_client.webhooks.validate_signature(
            payload + "foo",
            headers={"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is False

        # modified signature
        result = self.strict_client.webhooks.validate_signature(
            payload,
            headers={"X-Signature": "bar"},
            key="foo",
        )
        assert result is False

    def test_validate_signature_custom_headers_class(self) -> None:
        class Headers:
            def __init__(self, raw: Mapping[str, str]) -> None:
                self._raw = raw

            def get(self, key: str) -> str | None:
                return self._raw.get(key)

        result = self.strict_client.webhooks.validate_signature(
            '{"foo":"bar"}',
            headers=Headers({"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"}),
            key="foo",
        )
        assert result is True

        with pytest.raises(ValueError, match="Could not find an X-Signature header"):
            self.strict_client.webhooks.validate_signature(
                '{"foo":"bar"}',
                headers=Headers({}),
                key="foo",
            )


class TestAsyncWebhooks:
    strict_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, organization_id="my-organization-ID"
    )
    loose_client = AsyncModernTreasury(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, organization_id="my-organization-ID"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
    def test_get_signature(self, payload: str, expected: str) -> None:
        sig = self.strict_client.webhooks.get_signature(payload, key="foo")
        assert sig == expected

    def test_get_signature_key_not_set(self) -> None:
        with pytest.raises(ValueError, match="webhook key"):
            self.strict_client.webhooks.get_signature("foo")

    def test_get_signature_client_key(self) -> None:
        client = self.strict_client.__class__(
            base_url=base_url,
            api_key=api_key,
            organization_id="c40c0b40-11d3-42ee-8f2e-18ee8b8239aa",
            webhook_key="foo",
        )
        assert client.webhook_key == "foo"

        payload = '{"foo":"bar"}'
        sig = client.webhooks.get_signature(payload)
        assert sig == "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"

        other_sig = client.webhooks.get_signature(payload, key="bar")
        assert sig != other_sig

    def test_validate_signature_no_header(self) -> None:
        with pytest.raises(ValueError, match="Could not find an X-Signature header"):
            self.strict_client.webhooks.validate_signature("foo", headers={"foo": "bar"}, key="foo")

    def test_validate_signature(self) -> None:
        payload = '{"foo":"bar"}'
        result = self.strict_client.webhooks.validate_signature(
            payload,
            headers={"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is True

        # lowercased header
        result = self.strict_client.webhooks.validate_signature(
            payload,
            headers={"x-signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is True

        # modified payload
        result = self.strict_client.webhooks.validate_signature(
            payload + "foo",
            headers={"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"},
            key="foo",
        )
        assert result is False

        # modified signature
        result = self.strict_client.webhooks.validate_signature(
            payload,
            headers={"X-Signature": "bar"},
            key="foo",
        )
        assert result is False

    def test_validate_signature_custom_headers_class(self) -> None:
        class Headers:
            def __init__(self, raw: Mapping[str, str]) -> None:
                self._raw = raw

            def get(self, key: str) -> str | None:
                return self._raw.get(key)

        result = self.strict_client.webhooks.validate_signature(
            '{"foo":"bar"}',
            headers=Headers({"X-Signature": "57e14f6f354543f0101fb06ea24df7731d90087b76651e3497345e22a3622940"}),
            key="foo",
        )
        assert result is True

        with pytest.raises(ValueError, match="Could not find an X-Signature header"):
            self.strict_client.webhooks.validate_signature(
                '{"foo":"bar"}',
                headers=Headers({}),
                key="foo",
            )
