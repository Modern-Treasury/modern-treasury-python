# File generated from our OpenAPI spec by Stainless.

import os
import base64
from typing import Dict, Union, Optional

from . import resources
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
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
    counterparties: resources.Counterparties
    events: resources.Events
    expected_payments: resources.ExpectedPayments
    external_accounts: resources.ExternalAccounts
    incoming_payment_details: resources.IncomingPaymentDetails
    documents: resources.Documents
    internal_accounts: resources.InternalAccounts
    line_items: resources.LineItems
    payment_orders: resources.PaymentOrders
    returns: resources.Returns
    transactions: resources.Transactions
    validations: resources.Validations
    paper_items: resources.PaperItems
    webhooks: resources.Webhooks

    def __init__(
        self,
        *,
        organization_id: Optional[str] = None,
        webhook_key: Optional[str] = None,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
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
        api_key = api_key or os.environ.get("MODERN_TREASURY_API_KEY", "")
        if not api_key:
            raise Exception("No API key provided")

        if base_url is None:
            base_url = "https://app.moderntreasury.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            api_key=api_key,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            _strict_response_validation=_strict_response_validation,
        )

        self.organization_id = organization_id or os.environ.get("MODERN_TREASURY_ORGANIZATION_ID")
        if self.organization_id is None:
            raise ValueError(
                "The organization_id client option must be set either by passing organization_id to the client or by setting the MODERN_TREASURY_ORGANIZATION_ID environment variable"
            )

        self.webhook_key = webhook_key or os.environ.get("MODERN_TREASURY_WEBHOOK_KEY")

        self._idempotency_header = "Idempotency-Key"

        self.counterparties = resources.Counterparties(self)
        self.events = resources.Events(self)
        self.expected_payments = resources.ExpectedPayments(self)
        self.external_accounts = resources.ExternalAccounts(self)
        self.incoming_payment_details = resources.IncomingPaymentDetails(self)
        self.documents = resources.Documents(self)
        self.internal_accounts = resources.InternalAccounts(self)
        self.line_items = resources.LineItems(self)
        self.payment_orders = resources.PaymentOrders(self)
        self.returns = resources.Returns(self)
        self.transactions = resources.Transactions(self)
        self.validations = resources.Validations(self)
        self.paper_items = resources.PaperItems(self)
        self.webhooks = resources.Webhooks(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    def auth_headers(self) -> Dict[str, str]:
        key = f"{self.organization_id}:{self.api_key}".encode("ascii")
        header = f"Basic {base64.b64encode(key).decode('ascii')}"
        return {"Authorization": header}

    def ping(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PingResponse:
        """
        A test endpoint often used to confirm credentials and headers are being passed
        in correctly.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self.get(
            "/api/ping",
            options=options,
            cast_to=PingResponse,
        )


class AsyncModernTreasury(AsyncAPIClient):
    counterparties: resources.AsyncCounterparties
    events: resources.AsyncEvents
    expected_payments: resources.AsyncExpectedPayments
    external_accounts: resources.AsyncExternalAccounts
    incoming_payment_details: resources.AsyncIncomingPaymentDetails
    documents: resources.AsyncDocuments
    internal_accounts: resources.AsyncInternalAccounts
    line_items: resources.AsyncLineItems
    payment_orders: resources.AsyncPaymentOrders
    returns: resources.AsyncReturns
    transactions: resources.AsyncTransactions
    validations: resources.AsyncValidations
    paper_items: resources.AsyncPaperItems
    webhooks: resources.AsyncWebhooks

    def __init__(
        self,
        *,
        organization_id: Optional[str] = None,
        webhook_key: Optional[str] = None,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
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
        api_key = api_key or os.environ.get("MODERN_TREASURY_API_KEY", "")
        if not api_key:
            raise Exception("No API key provided")

        if base_url is None:
            base_url = "https://app.moderntreasury.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            api_key=api_key,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            _strict_response_validation=_strict_response_validation,
        )

        self.organization_id = organization_id or os.environ.get("MODERN_TREASURY_ORGANIZATION_ID")
        if self.organization_id is None:
            raise ValueError(
                "The organization_id client option must be set either by passing organization_id to the client or by setting the MODERN_TREASURY_ORGANIZATION_ID environment variable"
            )

        self.webhook_key = webhook_key or os.environ.get("MODERN_TREASURY_WEBHOOK_KEY")

        self._idempotency_header = "Idempotency-Key"

        self.counterparties = resources.AsyncCounterparties(self)
        self.events = resources.AsyncEvents(self)
        self.expected_payments = resources.AsyncExpectedPayments(self)
        self.external_accounts = resources.AsyncExternalAccounts(self)
        self.incoming_payment_details = resources.AsyncIncomingPaymentDetails(self)
        self.documents = resources.AsyncDocuments(self)
        self.internal_accounts = resources.AsyncInternalAccounts(self)
        self.line_items = resources.AsyncLineItems(self)
        self.payment_orders = resources.AsyncPaymentOrders(self)
        self.returns = resources.AsyncReturns(self)
        self.transactions = resources.AsyncTransactions(self)
        self.validations = resources.AsyncValidations(self)
        self.paper_items = resources.AsyncPaperItems(self)
        self.webhooks = resources.AsyncWebhooks(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    def auth_headers(self) -> Dict[str, str]:
        key = f"{self.organization_id}:{self.api_key}".encode("ascii")
        header = f"Basic {base64.b64encode(key).decode('ascii')}"
        return {"Authorization": header}

    async def ping(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> PingResponse:
        """
        A test endpoint often used to confirm credentials and headers are being passed
        in correctly.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self.get(
            "/api/ping",
            options=options,
            cast_to=PingResponse,
        )


Client = ModernTreasury

AsyncClient = AsyncModernTreasury
