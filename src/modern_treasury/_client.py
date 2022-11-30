# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import base64
from typing import Dict, Union, Mapping, Optional

from . import resources
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._version import __version__
from ._base_client import (
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.ping_response import PingResponse

__all__ = [
    "ModernTreasury",
    "AsyncModernTreasury",
    "Client",
    "AsyncClient",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
]


class ModernTreasury(SyncAPIClient):
    connections: resources.Connections
    counterparties: resources.Counterparties
    events: resources.Events
    expected_payments: resources.ExpectedPayments
    external_accounts: resources.ExternalAccounts
    incoming_payment_details: resources.IncomingPaymentDetails
    documents: resources.Documents
    account_details: resources.AccountDetails
    routing_details: resources.RoutingDetails
    internal_accounts: resources.InternalAccounts
    ledgers: resources.Ledgers
    ledger_account_categories: resources.LedgerAccountCategories
    ledger_accounts: resources.LedgerAccounts
    ledger_entries: resources.LedgerEntries
    ledger_transactions: resources.LedgerTransactions
    line_items: resources.LineItems
    payment_orders: resources.PaymentOrders
    returns: resources.Returns
    transactions: resources.Transactions
    validations: resources.Validations
    paper_items: resources.PaperItems
    webhooks: resources.Webhooks
    virtual_accounts: resources.VirtualAccounts

    # client options
    api_key: str
    organization_id: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Modern Treasury client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `MODERN_TREASURY_API_KEY`
        - `organization_id` from `MODERN_TREASURY_ORGANIZATION_ID`
        - `webhook_key` from `MODERN_TREASURY_WEBHOOK_KEY`
        """
        api_key = api_key or os.environ.get("MODERN_TREASURY_API_KEY", "")
        if not api_key:
            raise Exception(
                "The api_key client option must be set either by passing api_key to the client or by setting the MODERN_TREASURY_API_KEY environment variable"
            )

        if base_url is None:
            base_url = "https://app.moderntreasury.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api_key = api_key

        organization_id = organization_id or os.environ.get("MODERN_TREASURY_ORGANIZATION_ID")

        if organization_id is None:
            raise ValueError(
                "The organization_id client option must be set either by passing organization_id to the client or by setting the MODERN_TREASURY_ORGANIZATION_ID environment variable"
            )
        self.organization_id = organization_id

        self.webhook_key = webhook_key or os.environ.get("MODERN_TREASURY_WEBHOOK_KEY")

        self._idempotency_header = "Idempotency-Key"

        self.connections = resources.Connections(self)
        self.counterparties = resources.Counterparties(self)
        self.events = resources.Events(self)
        self.expected_payments = resources.ExpectedPayments(self)
        self.external_accounts = resources.ExternalAccounts(self)
        self.incoming_payment_details = resources.IncomingPaymentDetails(self)
        self.documents = resources.Documents(self)
        self.account_details = resources.AccountDetails(self)
        self.routing_details = resources.RoutingDetails(self)
        self.internal_accounts = resources.InternalAccounts(self)
        self.ledgers = resources.Ledgers(self)
        self.ledger_account_categories = resources.LedgerAccountCategories(self)
        self.ledger_accounts = resources.LedgerAccounts(self)
        self.ledger_entries = resources.LedgerEntries(self)
        self.ledger_transactions = resources.LedgerTransactions(self)
        self.line_items = resources.LineItems(self)
        self.payment_orders = resources.PaymentOrders(self)
        self.returns = resources.Returns(self)
        self.transactions = resources.Transactions(self)
        self.validations = resources.Validations(self)
        self.paper_items = resources.PaperItems(self)
        self.webhooks = resources.Webhooks(self)
        self.virtual_accounts = resources.VirtualAccounts(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    def auth_headers(self) -> Dict[str, str]:
        key = f"{self.organization_id}:{self.api_key}".encode("ascii")
        header = f"Basic {base64.b64encode(key).decode('ascii')}"
        return {"Authorization": header}

    def copy(
        self,
        *,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> ModernTreasury:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        # TODO: share the same httpx client between instances
        return self.__class__(
            organization_id=organization_id or self.organization_id,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or str(self.base_url),
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PingResponse:
        """
        A test endpoint often used to confirm credentials and headers are being passed
        in correctly.
        """
        return self.get(
            "/api/ping",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PingResponse,
        )


class AsyncModernTreasury(AsyncAPIClient):
    connections: resources.AsyncConnections
    counterparties: resources.AsyncCounterparties
    events: resources.AsyncEvents
    expected_payments: resources.AsyncExpectedPayments
    external_accounts: resources.AsyncExternalAccounts
    incoming_payment_details: resources.AsyncIncomingPaymentDetails
    documents: resources.AsyncDocuments
    account_details: resources.AsyncAccountDetails
    routing_details: resources.AsyncRoutingDetails
    internal_accounts: resources.AsyncInternalAccounts
    ledgers: resources.AsyncLedgers
    ledger_account_categories: resources.AsyncLedgerAccountCategories
    ledger_accounts: resources.AsyncLedgerAccounts
    ledger_entries: resources.AsyncLedgerEntries
    ledger_transactions: resources.AsyncLedgerTransactions
    line_items: resources.AsyncLineItems
    payment_orders: resources.AsyncPaymentOrders
    returns: resources.AsyncReturns
    transactions: resources.AsyncTransactions
    validations: resources.AsyncValidations
    paper_items: resources.AsyncPaperItems
    webhooks: resources.AsyncWebhooks
    virtual_accounts: resources.AsyncVirtualAccounts

    # client options
    api_key: str
    organization_id: str
    webhook_key: str | None

    def __init__(
        self,
        *,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async Modern Treasury client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `MODERN_TREASURY_API_KEY`
        - `organization_id` from `MODERN_TREASURY_ORGANIZATION_ID`
        - `webhook_key` from `MODERN_TREASURY_WEBHOOK_KEY`
        """
        api_key = api_key or os.environ.get("MODERN_TREASURY_API_KEY", "")
        if not api_key:
            raise Exception(
                "The api_key client option must be set either by passing api_key to the client or by setting the MODERN_TREASURY_API_KEY environment variable"
            )

        if base_url is None:
            base_url = "https://app.moderntreasury.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.api_key = api_key

        organization_id = organization_id or os.environ.get("MODERN_TREASURY_ORGANIZATION_ID")

        if organization_id is None:
            raise ValueError(
                "The organization_id client option must be set either by passing organization_id to the client or by setting the MODERN_TREASURY_ORGANIZATION_ID environment variable"
            )
        self.organization_id = organization_id

        self.webhook_key = webhook_key or os.environ.get("MODERN_TREASURY_WEBHOOK_KEY")

        self._idempotency_header = "Idempotency-Key"

        self.connections = resources.AsyncConnections(self)
        self.counterparties = resources.AsyncCounterparties(self)
        self.events = resources.AsyncEvents(self)
        self.expected_payments = resources.AsyncExpectedPayments(self)
        self.external_accounts = resources.AsyncExternalAccounts(self)
        self.incoming_payment_details = resources.AsyncIncomingPaymentDetails(self)
        self.documents = resources.AsyncDocuments(self)
        self.account_details = resources.AsyncAccountDetails(self)
        self.routing_details = resources.AsyncRoutingDetails(self)
        self.internal_accounts = resources.AsyncInternalAccounts(self)
        self.ledgers = resources.AsyncLedgers(self)
        self.ledger_account_categories = resources.AsyncLedgerAccountCategories(self)
        self.ledger_accounts = resources.AsyncLedgerAccounts(self)
        self.ledger_entries = resources.AsyncLedgerEntries(self)
        self.ledger_transactions = resources.AsyncLedgerTransactions(self)
        self.line_items = resources.AsyncLineItems(self)
        self.payment_orders = resources.AsyncPaymentOrders(self)
        self.returns = resources.AsyncReturns(self)
        self.transactions = resources.AsyncTransactions(self)
        self.validations = resources.AsyncValidations(self)
        self.paper_items = resources.AsyncPaperItems(self)
        self.webhooks = resources.AsyncWebhooks(self)
        self.virtual_accounts = resources.AsyncVirtualAccounts(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    def auth_headers(self) -> Dict[str, str]:
        key = f"{self.organization_id}:{self.api_key}".encode("ascii")
        header = f"Basic {base64.b64encode(key).decode('ascii')}"
        return {"Authorization": header}

    def copy(
        self,
        *,
        organization_id: str | None = None,
        webhook_key: str | None = None,
        api_key: str | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> AsyncModernTreasury:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        # TODO: share the same httpx client between instances
        return self.__class__(
            organization_id=organization_id or self.organization_id,
            webhook_key=webhook_key or self.webhook_key,
            base_url=base_url or str(self.base_url),
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def ping(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PingResponse:
        """
        A test endpoint often used to confirm credentials and headers are being passed
        in correctly.
        """
        return await self.get(
            "/api/ping",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PingResponse,
        )


Client = ModernTreasury

AsyncClient = AsyncModernTreasury
