#!/usr/bin/env poetry run python

from modern_treasury import ModernTreasury

mt = ModernTreasury()

account = mt.external_accounts.create(
    name="Test",
    counterparty_id="123",
    party_address={"country": "USA", "locality": "New York City"},
)

print(account.party_address)
