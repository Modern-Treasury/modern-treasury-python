import hmac
from hashlib import sha256

import pytest

from modern_treasury import ModernTreasury, AsyncModernTreasury


@pytest.mark.parametrize("body", ['{"message":"hello"}', '{"message":"café ☕"}'])
@pytest.mark.parametrize("as_bytes", [False, True])
def test_sync_webhook_raw_body(body: str, as_bytes: bool) -> None:
    raw = body.encode("utf-8")
    expected = hmac.new(b"test-webhook-key", raw, sha256).hexdigest()
    payload = raw if as_bytes else body
    with ModernTreasury(api_key="test-key", organization_id="test-org") as client:
        assert client.webhooks.get_signature(payload, key="test-webhook-key") == expected
        assert client.webhooks.validate_signature(payload, {"X-Signature": expected}, key="test-webhook-key")
        assert not client.webhooks.validate_signature(payload, {"X-Signature": "0" * 64}, key="test-webhook-key")


@pytest.mark.parametrize("body", ['{"message":"hello"}', '{"message":"café ☕"}'])
@pytest.mark.parametrize("as_bytes", [False, True])
async def test_async_webhook_raw_body(body: str, as_bytes: bool) -> None:
    raw = body.encode("utf-8")
    expected = hmac.new(b"test-webhook-key", raw, sha256).hexdigest()
    payload = raw if as_bytes else body
    async with AsyncModernTreasury(api_key="test-key", organization_id="test-org") as client:
        assert client.webhooks.get_signature(payload, key="test-webhook-key") == expected
        assert client.webhooks.validate_signature(payload, {"X-Signature": expected}, key="test-webhook-key")
        assert not client.webhooks.validate_signature(payload, {"X-Signature": "0" * 64}, key="test-webhook-key")
