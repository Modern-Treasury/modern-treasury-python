#!/usr/bin/env -S poetry run python

from datetime import datetime

from modern_treasury import ModernTreasury

client = ModernTreasury()

now = datetime.now()

# datetime responses will always be instances of `datetime`
account = client.internal_accounts.list().items[0]
assert isinstance(account.created_at, datetime)
assert account.created_at.tzname() == "UTC"

dt = datetime.fromisoformat("2023-03-01T12:40:40+00:00")

# both `datetime` instances or datetime strings can be passed as a request param
page = client.counterparties.list(created_at_upper_bound=dt, per_page=1)
assert len(page.items) == 1

page = client.counterparties.list(created_at_upper_bound=dt.isoformat(), per_page=1)
assert len(page.items) == 1
