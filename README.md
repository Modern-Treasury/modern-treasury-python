# Modern Treasury Python API library

[![PyPI version](https://img.shields.io/pypi/v/modern-treasury.svg)](https://pypi.org/project/modern-treasury/)

The Modern Treasury Python library provides convenient access to the Modern Treasury REST API from any Python 3.7+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

https://user-images.githubusercontent.com/704302/216504942-09ed8dd7-7f44-40a6-a580-3764e91f11b4.mov

## Documentation

The REST API documentation can be found [on docs.moderntreasury.com](https://docs.moderntreasury.com). The full API of this library can be found in [api.md](api.md).

## Installation

```sh
# install from PyPI
pip install modern-treasury
```

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from modern_treasury import ModernTreasury

client = ModernTreasury(
    # This is the default and can be omitted
    organization_id=os.environ.get("MODERN_TREASURY_ORGANIZATION_ID"),
    # This is the default and can be omitted
    api_key=os.environ.get("MODERN_TREASURY_API_KEY"),
)

external_account = client.external_accounts.create(
    counterparty_id="9eba513a-53fd-4d6d-ad52-ccce122ab92a",
    name="my bank",
)
print(external_account.id)
```

While you can provide a `organization_id` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `MODERN_TREASURY_ORGANIZATION_ID="my-organization-ID"` to your `.env` file
so that your Organization ID is not stored in source control.

## Async usage

Simply import `AsyncModernTreasury` instead of `ModernTreasury` and use `await` with each API call:

```python
import os
import asyncio
from modern_treasury import AsyncModernTreasury

client = AsyncModernTreasury(
    # This is the default and can be omitted
    organization_id=os.environ.get("MODERN_TREASURY_ORGANIZATION_ID"),
    # This is the default and can be omitted
    api_key=os.environ.get("MODERN_TREASURY_API_KEY"),
)


async def main() -> None:
    external_account = await client.external_accounts.create(
        counterparty_id="9eba513a-53fd-4d6d-ad52-ccce122ab92a",
        name="my bank",
    )
    print(external_account.id)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev), which provide helper methods for things like:

- Serializing back into JSON, `model.model_dump_json(indent=2, exclude_unset=True)`
- Converting to a dictionary, `model.model_dump(exclude_unset=True)`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Pagination

List methods in the Modern Treasury API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import modern_treasury

client = ModernTreasury()

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

client = AsyncModernTreasury()


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

client = ModernTreasury()

external_account = client.external_accounts.create(
    counterparty_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
)
print(external_account.id)
```

## File Uploads

Request parameters that correspond to file uploads can be passed as `bytes`, a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance or a tuple of `(filename, contents, media type)`.

```python
from pathlib import Path
from modern_treasury import ModernTreasury

client = ModernTreasury()

client.documents.create(
    documentable_id="24c6b7a3-02...",
    documentable_type="counterparties",
    file=Path("my/file.txt"),
)
```

The async client uses the exact same interface. If you pass a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, the file contents will be read asynchronously automatically.

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `modern_treasury.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `modern_treasury.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `modern_treasury.APIError`.

```python
import modern_treasury
from modern_treasury import ModernTreasury

client = ModernTreasury()

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

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from modern_treasury import ModernTreasury

# Configure the default for all requests:
client = ModernTreasury(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).external_accounts.list()
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from modern_treasury import ModernTreasury

# Configure the default for all requests:
client = ModernTreasury(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = ModernTreasury(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5 * 1000).external_accounts.list(
    party_name="my bank",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `MODERN_TREASURY_LOG` to `debug`.

```shell
$ export MODERN_TREASURY_LOG=debug
```

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from modern_treasury import ModernTreasury

client = ModernTreasury()
response = client.external_accounts.with_raw_response.create(
    counterparty_id="9eba513a-53fd-4d6d-ad52-ccce122ab92a",
    name="my bank",
)
print(response.headers.get('X-My-Header'))

external_account = response.parse()  # get the object that `external_accounts.create()` would have returned
print(external_account.id)
```

These methods return an [`LegacyAPIResponse`](https://github.com/Modern-Treasury/modern-treasury-python/tree/main/src/modern_treasury/_legacy_response.py) object. This is a legacy class as we're changing it slightly in the next major version.

For the sync client this will mostly be the same with the exception
of `content` & `text` will be methods instead of properties. In the
async client, all methods will be async.

A migration script will be provided & the migration in general should
be smooth.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

As such, `.with_streaming_response` methods return a different [`APIResponse`](https://github.com/Modern-Treasury/modern-treasury-python/tree/main/src/modern_treasury/_response.py) object, and the async client returns an [`AsyncAPIResponse`](https://github.com/Modern-Treasury/modern-treasury-python/tree/main/src/modern_treasury/_response.py) object.

```python
with client.external_accounts.with_streaming_response.create(
    counterparty_id="9eba513a-53fd-4d6d-ad52-ccce122ab92a",
    name="my bank",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for proxies
- Custom transports
- Additional [advanced](https://www.python-httpx.org/advanced/#client-instances) functionality

```python
import httpx
from modern_treasury import ModernTreasury

client = ModernTreasury(
    # Or use the `MODERN_TREASURY_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/Modern-Treasury/modern-treasury-python/issues) with questions, bugs, or suggestions.

## Requirements

Python 3.7 or higher.
