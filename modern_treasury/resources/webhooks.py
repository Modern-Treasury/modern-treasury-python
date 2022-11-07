# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import hmac
from hashlib import sha256

from .._types import HeadersLike
from .._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Webhooks", "AsyncWebhooks"]


class Webhooks(SyncAPIResource):
    def get_signature(
        self,
        payload: str,
        *,
        key: str | None = None,
    ) -> str:
        """
        To verify that a webhook was actually sent by Modern Treasury, every payload is
        signed with a signature that is passed through the `X-Signature` HTTP header.

        This method will generate a signature based off of your webhook key which can be
        found in the Developer Settings,
        https://app.moderntreasury.com/developers/webhooks, and the webhook payload.

        You can then compare the generated signature with the signature sent with the
        request, if they match then the webhook was sent by Modern Treasury.
        """
        if key is None:
            key = self._client.webhook_key

        if key is None:
            raise ValueError(
                "The webhook key must either be set using the env var, MODERN_TREASURY_WEBHOOK_KEY, on the client class, ModernTreasury(webhook_key='123'), or passed to this function"
            )

        if not key:
            raise ValueError("The webhook is set but appears to be empty")

        mac = hmac.new(
            key.encode("utf-8"),
            msg=payload.encode("utf-8"),
            digestmod=sha256,
        )
        return mac.hexdigest()

    def validate_signature(
        self,
        payload: str,
        headers: HeadersLike,
        *,
        key: str | None = None,
    ) -> bool:
        """Returns whether or not the webhook payload was sent by Modern Treasury."""
        signature = self.get_signature(payload, key=key)
        expected_signature = headers.get("X-Signature") or headers.get("x-signature")
        if expected_signature is None:
            raise ValueError("Could not find an X-Signature header")

        return signature == expected_signature


class AsyncWebhooks(AsyncAPIResource):
    def get_signature(
        self,
        payload: str,
        *,
        key: str | None = None,
    ) -> str:
        """
        To verify that a webhook was actually sent by Modern Treasury, every payload is
        signed with a signature that is passed through the `X-Signature` HTTP header.

        This method will generate a signature based off of your webhook key which can be
        found in the Developer Settings,
        https://app.moderntreasury.com/developers/webhooks, and the webhook payload.

        You can then compare the generated signature with the signature sent with the
        request, if they match then the webhook was sent by Modern Treasury.
        """
        if key is None:
            key = self._client.webhook_key

        if key is None:
            raise ValueError(
                "The webhook key must either be set using the env var, MODERN_TREASURY_WEBHOOK_KEY, on the client class, ModernTreasury(webhook_key='123'), or passed to this function"
            )

        if not key:
            raise ValueError("The webhook is set but appears to be empty")

        mac = hmac.new(
            key.encode("utf-8"),
            msg=payload.encode("utf-8"),
            digestmod=sha256,
        )
        return mac.hexdigest()

    def validate_signature(
        self,
        payload: str,
        headers: HeadersLike,
        *,
        key: str | None = None,
    ) -> bool:
        """Returns whether or not the webhook payload was sent by Modern Treasury."""
        signature = self.get_signature(payload, key=key)
        expected_signature = headers.get("X-Signature") or headers.get("x-signature")
        if expected_signature is None:
            raise ValueError("Could not find an X-Signature header")

        return signature == expected_signature
