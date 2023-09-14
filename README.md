# Modern Treasury Python API Library

> **Migration Guide**
>
> We've made some major improvements to how you pass arguments to methods which will require migrating your existing code.
>
> If you want to migrate to the new patterns incrementally you can do so by installing `v0.5.0`. This release contains both
> the new and old patterns with a backwards compatibility layer.
>
> You can find a guide to migrating in [this document](#migration-guide).

[![PyPI version](https://img.shields.io/pypi/v/modern-treasury.svg)](https://pypi.org/project/modern-treasury/)

The Modern Treasury Python library provides convenient access to the Modern Treasury REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

https://user-images.githubusercontent.com/704302/216504942-09ed8dd7-7f44-40a6-a580-3764e91f11b4.mov

## Documentation

The API documentation can be found [here](https://docs.moderntreasury.com).

## Installation

```sh
pip install modern-treasury
```

## Usage

The full API of this library can be found in [api.md](https://www.github.com/Modern-Treasury/modern-treasury-python/blob/main/api.md).

```python
from modern_treasury import ModernTreasury

client = ModernTreasury(
    # defaults to os.environ.get("MODERN_TREASURY_API_KEY")
    api_key="my api key",
    organization_id="my-organization-ID",
)

external_account = client.external_accounts.create(
    counterparty_id="9eba513a-53fd-4d6d-ad52-ccce122ab92a",
    name="my bank",
)
print(external_account.id)
```

While you can provide an `api_key` keyword argument, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
and adding `MODERN_TREASURY_API_KEY="my api key"` to your `.env` file so that your API Key is not stored in source control.

## Async Usage

Simply import `AsyncModernTreasury` instead of `ModernTreasury` and use `await` with each API call:

```python
from modern_treasury import AsyncModernTreasury

client = AsyncModernTreasury(
    # defaults to os.environ.get("MODERN_TREASURY_API_KEY")
    api_key="my api key",
    organization_id="my-organization-ID",
)


async def main():
    external_account = await client.external_accounts.create(
        counterparty_id="9eba513a-53fd-4d6d-ad52-ccce122ab92a",
        name="my bank",
    )
    print(external_account.id)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using Types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev), which provide helper methods for things like serializing back into json ([v1](https://docs.pydantic.dev/1.10/usage/models/), [v2](https://docs.pydantic.dev/latest/usage/serialization/)). To get a dictionary, you can call `dict(model)`.

This helps provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Modern Treasury API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import modern_treasury

client = ModernTreasury(
    organization_id="my-organization-ID",
)

all_external_accounts = []
# Automatically fetches more pages as needed.
for external_account in client.external_accounts.list():
    # Do something with external_account here
    all_external_accounts.append(external_account)
print(all_external_accounts)
```

Or, asynchronously:

```python
import asyncio
import modern_treasury

client = AsyncModernTreasury(
    organization_id="my-organization-ID",
)


async def main() -> None:
    all_external_accounts = []
    # Iterate through items across all pages, issuing requests as needed.
    async for external_account in client.external_accounts.list():
        all_external_accounts.append(external_account)
    print(all_external_accounts)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await client.external_accounts.list()
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.items)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await client.external_accounts.list()

print(f"next page cursor: {first_page.after_cursor}")  # => "next page cursor: ..."
for external_account in first_page.items:
    print(external_account.id)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from modern_treasury import ModernTreasury

client = ModernTreasury(
    organization_id="my-organization-ID",
)

client.external_accounts.create(
    foo={
        "bar": True,
    },
)
```

## File Uploads

Request parameters that correspond to file uploads can be passed as `bytes` or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from modern_treasury import ModernTreasury

client = ModernTreasury(
    organization_id="my-organization-ID",
)

contents = Path("my/file.txt").read_bytes()
client.documents.create(
    file=contents,
    documentable_type="counterparties",
    documentable_id="24c6b7a3-02...",
)
```

The async client uses the exact same interface. This example uses `aiofiles` to asynchronously read the file contents but you can use whatever method you would like.

```python
import aiofiles
from modern_treasury import ModernTreasury

client = ModernTreasury(
    organization_id="my-organization-ID",
)

async with aiofiles.open("my/file.txt", mode="rb") as f:
    contents = await f.read()

await client.documents.create(
    file=contents,
    documentable_type="counterparties",
    documentable_id="24c6b7a3-02...",
)
```

## Handling errors

When the library is unable to connect to the API (e.g., due to network connection problems or a timeout), a subclass of `modern_treasury.APIConnectionError` is raised.

When the API returns a non-success status code (i.e., 4xx or 5xx
response), a subclass of `modern_treasury.APIStatusError` will be raised, containing `status_code` and `response` properties.

All errors inherit from `modern_treasury.APIError`.

```python
import modern_treasury
from modern_treasury import ModernTreasury

client = ModernTreasury(
    organization_id="my-organization-ID",
)

try:
    client.external_accounts.create(
        counterparty_id="missing",
    )
except modern_treasury.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
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
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from modern_treasury import ModernTreasury

# Configure the default for all requests:
client = ModernTreasury(
    # default is 2
    max_retries=0,
    organization_id="my-organization-ID",
)

# Or, configure per-request:
client.with_options(max_retries=5).external_accounts.list()
```

### Timeouts

Requests time out after 1 minute by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
from modern_treasury import ModernTreasury

# Configure the default for all requests:
client = ModernTreasury(
    # default is 60s
    timeout=20.0,
    organization_id="my-organization-ID",
)

# More granular control:
client = ModernTreasury(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
    organization_id="my-organization-ID",
)

# Override per-request:
client.with_options(timeout=5 * 1000).external_accounts.list(
    party_name="my bank",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Advanced

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly null, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
from modern_treasury import ModernTreasury

client = ModernTreasury(
    # Use a custom base URL
    base_url="http://my.test.server.example.com:8083",
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    organization_id="my-organization-ID",
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

### Managing HTTP resources

By default we will close the underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__) is called but you can also manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

# Migration guide

This section outlines the features that were deprecated in `v0.5.0`, and subsequently removed in `v0.6.0` and how to migrate your code.

## Breaking changes

### TypedDict → keyword arguments

The way you pass arguments to methods has been changed from a single `TypedDict` to individual arguments. For example, this snippet:

```python
account = await client.external_accounts.create(
    {
        "name": "my bank",
        "counterparty_id": "123",
    }
)
```

Now becomes:

```python
account = await client.external_accounts.create(
    name="my bank",
    counterparty_id="123",
)
```

#### Migrating

The easiest way to make your code compatible with this change is to add `**{`, for example:

```diff
- account = await client.external_accounts.create({
-   "name": "my bank",
-   "counterparty_id": "123",
- })
+ account = await client.external_accounts.create(**{
+   "name": "my bank",
+   "counterparty_id": "123",
+ })
```

However, it is highly recommended to completely switch to explicit keyword arguments:

```diff
- account = await client.external_accounts.create({
-   "name": "my bank",
-   "counterparty_id": "123",
- })
+ account = await client.external_accounts.create(
+   name='my bank',
+   counterparty_id='123',
+ )
```

### Named path arguments

All but the last path parameter must now be passed as named arguments instead of positional arguments, for example, for a method that calls the endpoint `/api/{itemizable_type}/{itemizable_id}/line_items/{id}` you would've been able to call the method like this:

```python
line_item = await client.line_items.retrieve(
    "itemizable_type",
    "itemizable_id",
    "my_line_id",
)
```

But now you must call the method like this:

```python
line_item = await client.line_items.retrieve(
    "my_line_id",
    itemizable_id="itemizable_id",
    itemizable_type="itemizable_type",
)
```

If you have type checking enabled in your IDE it will tell you which parts of your code need to be updated.

### Request options

You used to be able to set request options on a per-method basis, now you can only set them on the client. There are two methods that you can use to make this easy, `with_options` and `copy`.

If you need to make multiple requests with changed options, you can use `.copy()` to get a new client object with those options. This can be useful if you need to set a custom header for multiple requests, for example:

```python
copied = client.copy(default_headers={"X-My-Header": "Foo"})
account = await copied.external_accounts.create(
    name="my bank",
    counterparty_id="123",
)
await copied.cards.provision(card.token, digital_wallet="GOOGLE_PAY")
```

If you just need to override one of the client options for one request, you can use `.with_options()`, for example:

```python
await client.with_options(timeout=None).external_accounts.create(
    name="my bank",
    counterparty_id="123",
)
```

It should be noted that the `.with_options()` method is simply an alias to `.copy()`, you can use them interchangeably.

You can pass nearly every argument that is supported by the Client `__init__` method to the `.copy()` method, except for `proxies` and `transport`.

```python
copied = client.copy(
    api_key="...",
    timeout=httpx.Timeout(read=10),
    max_retries=5,
    default_headers={
        "X-My-Header": "value",
    },
    default_query={
        "my_default_param": "value",
    },
)
```

## New features

### Pass custom headers

If you need to add additional headers to a request you can easily do so with the `extra_headers` argument:

```python
account = await client.external_accounts.create(
    name="my bank",
    counterparty_id="123",
    extra_headers={
        "X-Foo": "my header",
    },
)
```

### Pass custom JSON properties

You can add additional properties to the JSON request body that are not included directly in the method definition through the `extra_body` argument. This can be useful when there are in new properties in the API that are in beta and aren't in the SDK yet.

```python
account = await client.external_accounts.create(
    name="my bank",
    counterparty_id="123",
    extra_body={
        "special_prop": "foo",
    },
)
# sends this to the API:
# {"name": "my bank", "counterparty_id": "123", "special_prop": "foo"}
```

### Pass custom query parameters

You can add additional query parameters that aren't specified in the method definition through the `extra_query` argument. This can be useful when there are any new/beta query parameters that are not yet in the SDK.

```python
account = await client.external_accounts.create(
    name="my bank",
    counterparty_id="123",
    extra_query={
        "special_param": "bar",
    },
)
# makes the request to this URL:
# https://app.moderntreasury.com/api/external_accounts?special_param=bar
```

## Array items type name improvements

In `v1.5.0` we improved the names for types that come from arrays so that they always us a singular name, e.g. `LedgerEntries` -> `LedgerEntry`.

We've added aliases for the old type names so you can continue to use them without any breaking changes but they will be removed in the future.

Full list of all changed type names:

- `Accounts` -> `Account`
- `Balances` -> `Balance`
- `Documents` -> `Document`
- `LineItems` -> `LineItem`
- `LedgerEntries` -> `LedgerEntry`
- `AccountDetail` -> `AccountDetail`
- `RoutingDetail` -> `RoutingDetail`
- `AccountDetails` -> `AccountDetail`
- `ContactDetails` -> `ContactDetail`
- `RoutingDetails` -> `RoutingDetail`
- `ReferenceNumbers` -> `ReferenceNumber`
- `AccountsPartyAddress` -> `AccountPartyAddress`
- `AccountsAccountDetails` -> `AccountAccountDetail`
- `AccountsContactDetails` -> `AccountContactDetail`
- `AccountsRoutingDetails` -> `AccountRoutingDetail`
- `RoutingDetailBankAddress` -> `RoutingDetailBankAddress`
- `LedgerTransactionLedgerEntries` -> `LedgerTransactionLedgerEntry`
- `ReceivingAccountAccountDetails` -> `ReceivingAccountAccountDetail`
- `ReceivingAccountContactDetails` -> `ReceivingAccountContactDetail`
- `ReceivingAccountRoutingDetails` -> `ReceivingAccountRoutingDetail`
- `LedgerEntriesResultingLedgerAccountBalances` -> `LedgerEntryResultingLedgerAccountBalances`
- `LedgerEntriesResultingLedgerAccountBalancesPostedBalance` -> `LedgerEntryResultingLedgerAccountBalancesPostedBalance`
- `LedgerEntriesResultingLedgerAccountBalancesPendingBalance` -> `LedgerEntryResultingLedgerAccountBalancesPendingBalance`
- `LedgerEntriesResultingLedgerAccountBalancesAvailableBalance` -> `LedgerEntryResultingLedgerAccountBalancesAvailableBalance`

## Rich `date` and `datetime` types

We've improved the types for response fields / request params that correspond to `date` or `datetime` values!

Previously they were just raw strings but now response fields will be instances of `date` or `datetime`.

This means that if you're working with these fields and parsing them into `datetime` instances manually you will have to remove
any code that performs said parsing.

```diff
account = client.internal_accounts.retrieve('<id>')
- created_at = datetime.fromisoformat(account.created_at)
+ created_at = account.created_at
print(created_at.month)
```

For request params you can continue to pass in strings if you want to use a datetime library other than the standard library version but if you
were writing code that looked like this:

```py
dt = datetime(...)
for counterparty in client.counterparties.list(created_at_upper_bound=dt.isoformat()):
  ...
```

You can remove the explicit call to `isoformat`!

```diff
dt = datetime(...)
- for counterparty in client.counterparties.list(created_at_upper_bound=dt.isoformat()):
+ for counterparty in client.counterparties.list(created_at_upper_bound=dt):
  ...
```

## Versioning

This package generally attempts to follow [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/Modern-Treasury/modern-treasury-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.
