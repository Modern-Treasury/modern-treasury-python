# Modern Treasury Python API Library

[![PyPI version](https://img.shields.io/pypi/v/modern-treasury.svg)](https://pypi.org/project/modern-treasury/)

The Modern Treasury Python library provides convenient access to the Modern Treasury REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

![GIF showcasing modern_treasury usage](./showcase.gif)

## Documentation

The API documentation can be found [here](https://docs.moderntreasury.com).

## Installation

```sh
pip install modern-treasury
```

## Usage

```python
from modern_treasury import ModernTreasury

modern_treasury = ModernTreasury(
    # defaults to os.environ.get("MODERN_TREASURY_API_KEY")
    api_key="my api key",
    organization_id="my-organization-ID",
)

external_account = modern_treasury.external_accounts.create({
    "counterparty_id": "123",
    "name": "my bank",
})
print(external_account.id)
```

While you can provide an `api_key` keyword argument, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
and adding `MODERN_TREASURY_API_KEY="my api key"` to your `.env` file so that your API Key is not stored in source control.

## Async Usage

Simply import `AsyncModernTreasury` instead of `ModernTreasury` and use `await` with each API call:

```python
from modern_treasury import AsyncModernTreasury

modern_treasury = AsyncModernTreasury(
    # defaults to os.environ.get("MODERN_TREASURY_API_KEY")
    api_key="my api key",
    organization_id="my-organization-ID",
)

async def main():
    external_account = await modern_treasury.external_accounts.create({
        "counterparty_id": "123",
        "name": "my bank",
    })
    print(external_account.id)

asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients are otherwise identical.

## Using Types

Request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), while responses are [Pydantic](https://pydantic-docs.helpmanual.io/) models. This helps provide autocomplete and documentation within your editor.

If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Modern Treasury API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```py
import modern_treasury

modern_treasury = ModernTreasury(
    organization_id="my-organization-ID",
)

all_external_accounts = []
# Automatically fetches more pages as needed.
for external_account in modern_treasury.external_accounts.list():
    # Do something with external_account here
    all_external_accounts.append(external_account)
return all_external_accounts
```

Or, asynchronously:

```python
import asyncio
import modern_treasury

modern_treasury = AsyncModernTreasury(
    organization_id="my-organization-ID",
)

async def main() -> None:
    all_external_accounts = []
    # Iterate through items across all pages, issuing requests as needed.
    async for external_account in modern_treasury.external_accounts.list():
        all_external_accounts.append(external_account)
    print(all_external_accounts)

asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_params()`,
or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await modern_treasury.external_accounts.list()
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.items)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await modern_treasury.external_accounts.list()

print(f"next page cursor: {first_page.after_cursor}") # => "next page cursor: ..."
for external_account in first_page.items:
    print(external_account.id)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```py
from modern_treasury import ModernTreasury

modern_treasury = ModernTreasury(
    organization_id="my-organization-ID",
)

modern_treasury.external_accounts.create({
    "foo": {
        "bar": True
    },
})
```

## Handling errors

When the library is unable to connect to the API (e.g., due to network connection problems or a timeout), a subclass of `modern_treasury.APIConnectionError` is raised.

When the API returns a non-success status code (i.e., 4xx or 5xx
response), a subclass of `modern_treasury.APIStatusError` will be raised, containing `status_code` and `response` properties.

All errors inherit from `modern_treasury.APIError`.

```python
from modern_treasury import ModernTreasury

modern_treasury = ModernTreasury(
    organization_id="my-organization-ID",
)

try:
    modern_treasury.external_accounts.create({
        "counterparty_id": "missing",
    })
except modern_treasury.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__) # an underlying Exception, likely raised within httpx.
except modern_treasury.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except modern_treasury.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 409 Conflict, 429 Rate Limit,
and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from modern_treasury import ModernTreasury

# Configure the default for all requests:
modern_treasury = ModernTreasury(
    # default is 2
    max_retries=0,
    organization_id="my-organization-ID",
)

# Or, configure per-request:
modern_treasury.external_accounts.list(max_retries=5);
```

### Timeouts

Requests time out after 60 seconds by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
from modern_treasury import ModernTreasury

# Configure the default for all requests:
modern_treasury = ModernTreasury(
    # default is 60s
    timeout=20.0,
    organization_id="my-organization-ID",
)

# More granular control:
modern_treasury = ModernTreasury(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
    organization_id="my-organization-ID",
)

# Override per-request:
modern_treasury.external_accounts.list({
    "party_name": "my bank",
}, timeout=5 * 1000)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Advanced: Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
from modern_treasury import ModernTreasury

modern_treasury = ModernTreasury(
    # Use a custom base URL
    base_url="http://my.test.server.example.com:8083",
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    organization_id="my-organization-ID",
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

## Status

This package is in beta. Its internals and interfaces are not stable and subject to change without a major semver bump;
please reach out if you rely on any undocumented behavior.

We are keen for your feedback; please email us at [sdk-feedback@moderntreasury.com](mailto:sdk-feedback@moderntreasury.com) or open an issue with questions,
bugs, or suggestions.

## Requirements

Python 3.7 or higher.