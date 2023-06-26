# Shared Types

```python
from modern_treasury.types import AccountsType, AsyncResponse, Currency
```

# Top Level

Types:

```python
from modern_treasury.types import PingResponse
```

Methods:

- <code title="get /api/ping">client..<a href="./src/modern_treasury/_client.py">ping</a>() -> <a href="./src/modern_treasury/types/ping_response.py">PingResponse</a></code>

# Connections

Types:

```python
from modern_treasury.types import Connection
```

Methods:

- <code title="get /api/connections">client.connections.<a href="./src/modern_treasury/resources/connections.py">list</a>(\*\*<a href="src/modern_treasury/types/connection_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/connection.py">SyncPage[Connection]</a></code>

# Counterparties

Types:

```python
from modern_treasury.types import Counterparty, CounterpartyCollectAccountResponse
```

Methods:

- <code title="post /api/counterparties">client.counterparties.<a href="./src/modern_treasury/resources/counterparties.py">create</a>(\*\*<a href="src/modern_treasury/types/counterparty_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/counterparty.py">Counterparty</a></code>
- <code title="get /api/counterparties/{id}">client.counterparties.<a href="./src/modern_treasury/resources/counterparties.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/counterparty.py">Counterparty</a></code>
- <code title="patch /api/counterparties/{id}">client.counterparties.<a href="./src/modern_treasury/resources/counterparties.py">update</a>(id, \*\*<a href="src/modern_treasury/types/counterparty_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/counterparty.py">Counterparty</a></code>
- <code title="get /api/counterparties">client.counterparties.<a href="./src/modern_treasury/resources/counterparties.py">list</a>(\*\*<a href="src/modern_treasury/types/counterparty_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/counterparty.py">SyncPage[Counterparty]</a></code>
- <code title="delete /api/counterparties/{id}">client.counterparties.<a href="./src/modern_treasury/resources/counterparties.py">delete</a>(id) -> None</code>
- <code title="post /api/counterparties/{id}/collect_account">client.counterparties.<a href="./src/modern_treasury/resources/counterparties.py">collect_account</a>(id, \*\*<a href="src/modern_treasury/types/counterparty_collect_account_params.py">params</a>) -> <a href="./src/modern_treasury/types/counterparty_collect_account_response.py">CounterpartyCollectAccountResponse</a></code>

# Events

Types:

```python
from modern_treasury.types import Event
```

Methods:

- <code title="get /api/events/{id}">client.events.<a href="./src/modern_treasury/resources/events.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/event.py">Event</a></code>
- <code title="get /api/events">client.events.<a href="./src/modern_treasury/resources/events.py">list</a>(\*\*<a href="src/modern_treasury/types/event_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/event.py">SyncPage[Event]</a></code>

# ExpectedPayments

Types:

```python
from modern_treasury.types import ExpectedPayment, ExpectedPaymentType
```

Methods:

- <code title="post /api/expected_payments">client.expected_payments.<a href="./src/modern_treasury/resources/expected_payments.py">create</a>(\*\*<a href="src/modern_treasury/types/expected_payment_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/expected_payment.py">ExpectedPayment</a></code>
- <code title="get /api/expected_payments/{id}">client.expected_payments.<a href="./src/modern_treasury/resources/expected_payments.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/expected_payment.py">ExpectedPayment</a></code>
- <code title="patch /api/expected_payments/{id}">client.expected_payments.<a href="./src/modern_treasury/resources/expected_payments.py">update</a>(id, \*\*<a href="src/modern_treasury/types/expected_payment_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/expected_payment.py">ExpectedPayment</a></code>
- <code title="get /api/expected_payments">client.expected_payments.<a href="./src/modern_treasury/resources/expected_payments.py">list</a>(\*\*<a href="src/modern_treasury/types/expected_payment_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/expected_payment.py">SyncPage[ExpectedPayment]</a></code>
- <code title="delete /api/expected_payments/{id}">client.expected_payments.<a href="./src/modern_treasury/resources/expected_payments.py">delete</a>(id) -> <a href="./src/modern_treasury/types/expected_payment.py">ExpectedPayment</a></code>

# ExternalAccounts

Types:

```python
from modern_treasury.types import ExternalAccount, ExternalAccountType
```

Methods:

- <code title="post /api/external_accounts">client.external_accounts.<a href="./src/modern_treasury/resources/external_accounts.py">create</a>(\*\*<a href="src/modern_treasury/types/external_account_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/external_account.py">ExternalAccount</a></code>
- <code title="get /api/external_accounts/{id}">client.external_accounts.<a href="./src/modern_treasury/resources/external_accounts.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/external_account.py">ExternalAccount</a></code>
- <code title="patch /api/external_accounts/{id}">client.external_accounts.<a href="./src/modern_treasury/resources/external_accounts.py">update</a>(id, \*\*<a href="src/modern_treasury/types/external_account_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/external_account.py">ExternalAccount</a></code>
- <code title="get /api/external_accounts">client.external_accounts.<a href="./src/modern_treasury/resources/external_accounts.py">list</a>(\*\*<a href="src/modern_treasury/types/external_account_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/external_account.py">SyncPage[ExternalAccount]</a></code>
- <code title="delete /api/external_accounts/{id}">client.external_accounts.<a href="./src/modern_treasury/resources/external_accounts.py">delete</a>(id) -> None</code>
- <code title="post /api/external_accounts/{id}/complete_verification">client.external_accounts.<a href="./src/modern_treasury/resources/external_accounts.py">complete_verification</a>(id, \*\*<a href="src/modern_treasury/types/external_account_complete_verification_params.py">params</a>) -> <a href="./src/modern_treasury/types/external_account.py">ExternalAccount</a></code>
- <code title="post /api/external_accounts/{id}/verify">client.external_accounts.<a href="./src/modern_treasury/resources/external_accounts.py">verify</a>(id, \*\*<a href="src/modern_treasury/types/external_account_verify_params.py">params</a>) -> <a href="./src/modern_treasury/types/external_account.py">ExternalAccount</a></code>

# IncomingPaymentDetails

Types:

```python
from modern_treasury.types import IncomingPaymentDetail
```

Methods:

- <code title="get /api/incoming_payment_details/{id}">client.incoming_payment_details.<a href="./src/modern_treasury/resources/incoming_payment_details.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/incoming_payment_detail.py">IncomingPaymentDetail</a></code>
- <code title="patch /api/incoming_payment_details/{id}">client.incoming_payment_details.<a href="./src/modern_treasury/resources/incoming_payment_details.py">update</a>(id, \*\*<a href="src/modern_treasury/types/incoming_payment_detail_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/incoming_payment_detail.py">IncomingPaymentDetail</a></code>
- <code title="get /api/incoming_payment_details">client.incoming_payment_details.<a href="./src/modern_treasury/resources/incoming_payment_details.py">list</a>(\*\*<a href="src/modern_treasury/types/incoming_payment_detail_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/incoming_payment_detail.py">SyncPage[IncomingPaymentDetail]</a></code>
- <code title="post /api/simulations/incoming_payment_details/create_async">client.incoming_payment_details.<a href="./src/modern_treasury/resources/incoming_payment_details.py">create_async</a>(\*\*<a href="src/modern_treasury/types/incoming_payment_detail_create_async_params.py">params</a>) -> <a href="./src/modern_treasury/types/shared/async_response.py">shared.AsyncResponse</a></code>

# Invoices

Types:

```python
from modern_treasury.types import Invoice
```

Methods:

- <code title="post /api/invoices">client.invoices.<a href="./src/modern_treasury/resources/invoices/invoices.py">create</a>(\*\*<a href="src/modern_treasury/types/invoice_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/invoice.py">Invoice</a></code>
- <code title="get /api/invoices/{id}">client.invoices.<a href="./src/modern_treasury/resources/invoices/invoices.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/invoice.py">Invoice</a></code>
- <code title="patch /api/invoices/{id}">client.invoices.<a href="./src/modern_treasury/resources/invoices/invoices.py">update</a>(id, \*\*<a href="src/modern_treasury/types/invoice_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/invoice.py">Invoice</a></code>
- <code title="get /api/invoices">client.invoices.<a href="./src/modern_treasury/resources/invoices/invoices.py">list</a>(\*\*<a href="src/modern_treasury/types/invoice_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/invoice.py">SyncPage[Invoice]</a></code>

## LineItems

Types:

```python
from modern_treasury.types.invoices import InvoiceLineItem
```

Methods:

- <code title="post /api/invoices/{invoice_id}/invoice_line_items">client.invoices.line_items.<a href="./src/modern_treasury/resources/invoices/line_items.py">create</a>(invoice_id, \*\*<a href="src/modern_treasury/types/invoices/line_item_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/invoices/invoice_line_item.py">InvoiceLineItem</a></code>
- <code title="get /api/invoices/{invoice_id}/invoice_line_items/{id}">client.invoices.line_items.<a href="./src/modern_treasury/resources/invoices/line_items.py">retrieve</a>(invoice_id, id) -> <a href="./src/modern_treasury/types/invoices/invoice_line_item.py">InvoiceLineItem</a></code>
- <code title="patch /api/invoices/{invoice_id}/invoice_line_items/{id}">client.invoices.line_items.<a href="./src/modern_treasury/resources/invoices/line_items.py">update</a>(invoice_id, id, \*\*<a href="src/modern_treasury/types/invoices/line_item_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/invoices/invoice_line_item.py">InvoiceLineItem</a></code>
- <code title="get /api/invoices/{invoice_id}/invoice_line_items">client.invoices.line_items.<a href="./src/modern_treasury/resources/invoices/line_items.py">list</a>(invoice_id, \*\*<a href="src/modern_treasury/types/invoices/line_item_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/invoices/invoice_line_item.py">SyncPage[InvoiceLineItem]</a></code>
- <code title="delete /api/invoices/{invoice_id}/invoice_line_items/{id}">client.invoices.line_items.<a href="./src/modern_treasury/resources/invoices/line_items.py">delete</a>(invoice_id, id) -> <a href="./src/modern_treasury/types/invoices/invoice_line_item.py">InvoiceLineItem</a></code>

# Documents

Types:

```python
from modern_treasury.types import Document
```

Methods:

- <code title="post /api/documents">client.documents.<a href="./src/modern_treasury/resources/documents.py">create</a>(\*\*<a href="src/modern_treasury/types/document_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/document.py">Document</a></code>
- <code title="get /api/documents/{id}">client.documents.<a href="./src/modern_treasury/resources/documents.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/document.py">Document</a></code>
- <code title="get /api/documents">client.documents.<a href="./src/modern_treasury/resources/documents.py">list</a>(\*\*<a href="src/modern_treasury/types/document_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/document.py">SyncPage[Document]</a></code>

# AccountCollectionFlows

Types:

```python
from modern_treasury.types import AccountConnectionFlow
```

Methods:

- <code title="post /api/account_collection_flows">client.account_collection_flows.<a href="./src/modern_treasury/resources/account_collection_flows.py">create</a>(\*\*<a href="src/modern_treasury/types/account_collection_flow_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/account_connection_flow.py">AccountConnectionFlow</a></code>
- <code title="get /api/account_collection_flows/{id}">client.account_collection_flows.<a href="./src/modern_treasury/resources/account_collection_flows.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/account_connection_flow.py">AccountConnectionFlow</a></code>
- <code title="patch /api/account_collection_flows/{id}">client.account_collection_flows.<a href="./src/modern_treasury/resources/account_collection_flows.py">update</a>(id, \*\*<a href="src/modern_treasury/types/account_collection_flow_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/account_connection_flow.py">AccountConnectionFlow</a></code>
- <code title="get /api/account_collection_flows">client.account_collection_flows.<a href="./src/modern_treasury/resources/account_collection_flows.py">list</a>(\*\*<a href="src/modern_treasury/types/account_collection_flow_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/account_connection_flow.py">SyncPage[AccountConnectionFlow]</a></code>

# AccountDetails

Types:

```python
from modern_treasury.types import AccountDetail
```

Methods:

- <code title="post /api/{accounts_type}/{account_id}/account_details">client.account_details.<a href="./src/modern_treasury/resources/account_details.py">create</a>(accounts_type, account_id, \*\*<a href="src/modern_treasury/types/account_detail_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/account_detail.py">AccountDetail</a></code>
- <code title="get /api/{accounts_type}/{account_id}/account_details/{id}">client.account_details.<a href="./src/modern_treasury/resources/account_details.py">retrieve</a>(accounts_type, account_id, id) -> <a href="./src/modern_treasury/types/account_detail.py">AccountDetail</a></code>
- <code title="get /api/{accounts_type}/{account_id}/account_details">client.account_details.<a href="./src/modern_treasury/resources/account_details.py">list</a>(accounts_type, account_id, \*\*<a href="src/modern_treasury/types/account_detail_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/account_detail.py">SyncPage[AccountDetail]</a></code>
- <code title="delete /api/{accounts_type}/{account_id}/account_details/{id}">client.account_details.<a href="./src/modern_treasury/resources/account_details.py">delete</a>(accounts_type, account_id, id) -> None</code>

# RoutingDetails

Types:

```python
from modern_treasury.types import RoutingDetail
```

Methods:

- <code title="post /api/{accounts_type}/{account_id}/routing_details">client.routing_details.<a href="./src/modern_treasury/resources/routing_details.py">create</a>(accounts_type, account_id, \*\*<a href="src/modern_treasury/types/routing_detail_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/routing_detail.py">RoutingDetail</a></code>
- <code title="get /api/{accounts_type}/{account_id}/routing_details/{id}">client.routing_details.<a href="./src/modern_treasury/resources/routing_details.py">retrieve</a>(accounts_type, account_id, id) -> <a href="./src/modern_treasury/types/routing_detail.py">RoutingDetail</a></code>
- <code title="get /api/{accounts_type}/{account_id}/routing_details">client.routing_details.<a href="./src/modern_treasury/resources/routing_details.py">list</a>(accounts_type, account_id, \*\*<a href="src/modern_treasury/types/routing_detail_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/routing_detail.py">SyncPage[RoutingDetail]</a></code>
- <code title="delete /api/{accounts_type}/{account_id}/routing_details/{id}">client.routing_details.<a href="./src/modern_treasury/resources/routing_details.py">delete</a>(accounts_type, account_id, id) -> None</code>

# InternalAccounts

Types:

```python
from modern_treasury.types import InternalAccount
```

Methods:

- <code title="post /api/internal_accounts">client.internal_accounts.<a href="./src/modern_treasury/resources/internal_accounts/internal_accounts.py">create</a>(\*\*<a href="src/modern_treasury/types/internal_account_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/internal_account.py">InternalAccount</a></code>
- <code title="get /api/internal_accounts/{id}">client.internal_accounts.<a href="./src/modern_treasury/resources/internal_accounts/internal_accounts.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/internal_account.py">InternalAccount</a></code>
- <code title="patch /api/internal_accounts/{id}">client.internal_accounts.<a href="./src/modern_treasury/resources/internal_accounts/internal_accounts.py">update</a>(id, \*\*<a href="src/modern_treasury/types/internal_account_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/internal_account.py">InternalAccount</a></code>
- <code title="get /api/internal_accounts">client.internal_accounts.<a href="./src/modern_treasury/resources/internal_accounts/internal_accounts.py">list</a>(\*\*<a href="src/modern_treasury/types/internal_account_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/internal_account.py">SyncPage[InternalAccount]</a></code>

## BalanceReports

Types:

```python
from modern_treasury.types.internal_accounts import BalanceReport
```

Methods:

- <code title="get /api/internal_accounts/{internal_account_id}/balance_reports/{id}">client.internal_accounts.balance_reports.<a href="./src/modern_treasury/resources/internal_accounts/balance_reports.py">retrieve</a>(internal_account_id, id) -> <a href="./src/modern_treasury/types/internal_accounts/balance_report.py">BalanceReport</a></code>
- <code title="get /api/internal_accounts/{internal_account_id}/balance_reports">client.internal_accounts.balance_reports.<a href="./src/modern_treasury/resources/internal_accounts/balance_reports.py">list</a>(internal_account_id, \*\*<a href="src/modern_treasury/types/internal_accounts/balance_report_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/internal_accounts/balance_report.py">SyncPage[BalanceReport]</a></code>

# Ledgers

Types:

```python
from modern_treasury.types import Ledger
```

Methods:

- <code title="post /api/ledgers">client.ledgers.<a href="./src/modern_treasury/resources/ledgers.py">create</a>(\*\*<a href="src/modern_treasury/types/ledger_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger.py">Ledger</a></code>
- <code title="get /api/ledgers/{id}">client.ledgers.<a href="./src/modern_treasury/resources/ledgers.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/ledger.py">Ledger</a></code>
- <code title="patch /api/ledgers/{id}">client.ledgers.<a href="./src/modern_treasury/resources/ledgers.py">update</a>(id, \*\*<a href="src/modern_treasury/types/ledger_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger.py">Ledger</a></code>
- <code title="get /api/ledgers">client.ledgers.<a href="./src/modern_treasury/resources/ledgers.py">list</a>(\*\*<a href="src/modern_treasury/types/ledger_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger.py">SyncPage[Ledger]</a></code>
- <code title="delete /api/ledgers/{id}">client.ledgers.<a href="./src/modern_treasury/resources/ledgers.py">delete</a>(id) -> <a href="./src/modern_treasury/types/ledger.py">Ledger</a></code>

# LedgerableEvents

Types:

```python
from modern_treasury.types import LedgerableEvent
```

Methods:

- <code title="post /api/ledgerable_events">client.ledgerable_events.<a href="./src/modern_treasury/resources/ledgerable_events.py">create</a>(\*\*<a href="src/modern_treasury/types/ledgerable_event_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledgerable_event.py">LedgerableEvent</a></code>
- <code title="get /api/ledgerable_events/{id}">client.ledgerable_events.<a href="./src/modern_treasury/resources/ledgerable_events.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/ledgerable_event.py">LedgerableEvent</a></code>

# LedgerAccountCategories

Types:

```python
from modern_treasury.types import LedgerAccountCategory
```

Methods:

- <code title="post /api/ledger_account_categories">client.ledger_account_categories.<a href="./src/modern_treasury/resources/ledger_account_categories.py">create</a>(\*\*<a href="src/modern_treasury/types/ledger_account_category_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account_category.py">LedgerAccountCategory</a></code>
- <code title="get /api/ledger_account_categories/{id}">client.ledger_account_categories.<a href="./src/modern_treasury/resources/ledger_account_categories.py">retrieve</a>(id, \*\*<a href="src/modern_treasury/types/ledger_account_category_retrieve_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account_category.py">LedgerAccountCategory</a></code>
- <code title="patch /api/ledger_account_categories/{id}">client.ledger_account_categories.<a href="./src/modern_treasury/resources/ledger_account_categories.py">update</a>(id, \*\*<a href="src/modern_treasury/types/ledger_account_category_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account_category.py">LedgerAccountCategory</a></code>
- <code title="get /api/ledger_account_categories">client.ledger_account_categories.<a href="./src/modern_treasury/resources/ledger_account_categories.py">list</a>(\*\*<a href="src/modern_treasury/types/ledger_account_category_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account_category.py">SyncPage[LedgerAccountCategory]</a></code>
- <code title="delete /api/ledger_account_categories/{id}">client.ledger_account_categories.<a href="./src/modern_treasury/resources/ledger_account_categories.py">delete</a>(id, \*\*<a href="src/modern_treasury/types/ledger_account_category_delete_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account_category.py">LedgerAccountCategory</a></code>
- <code title="put /api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}">client.ledger_account_categories.<a href="./src/modern_treasury/resources/ledger_account_categories.py">add_ledger_account</a>(id, ledger_account_id) -> None</code>
- <code title="put /api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}">client.ledger_account_categories.<a href="./src/modern_treasury/resources/ledger_account_categories.py">add_nested_category</a>(id, sub_category_id) -> None</code>
- <code title="delete /api/ledger_account_categories/{id}/ledger_accounts/{ledger_account_id}">client.ledger_account_categories.<a href="./src/modern_treasury/resources/ledger_account_categories.py">remove_ledger_account</a>(id, ledger_account_id) -> None</code>
- <code title="delete /api/ledger_account_categories/{id}/ledger_account_categories/{sub_category_id}">client.ledger_account_categories.<a href="./src/modern_treasury/resources/ledger_account_categories.py">remove_nested_category</a>(id, sub_category_id) -> None</code>

# LedgerAccounts

Types:

```python
from modern_treasury.types import LedgerAccount
```

Methods:

- <code title="post /api/ledger_accounts">client.ledger_accounts.<a href="./src/modern_treasury/resources/ledger_accounts.py">create</a>(\*\*<a href="src/modern_treasury/types/ledger_account_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account.py">LedgerAccount</a></code>
- <code title="get /api/ledger_accounts/{id}">client.ledger_accounts.<a href="./src/modern_treasury/resources/ledger_accounts.py">retrieve</a>(id, \*\*<a href="src/modern_treasury/types/ledger_account_retrieve_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account.py">LedgerAccount</a></code>
- <code title="patch /api/ledger_accounts/{id}">client.ledger_accounts.<a href="./src/modern_treasury/resources/ledger_accounts.py">update</a>(id, \*\*<a href="src/modern_treasury/types/ledger_account_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account.py">LedgerAccount</a></code>
- <code title="get /api/ledger_accounts">client.ledger_accounts.<a href="./src/modern_treasury/resources/ledger_accounts.py">list</a>(\*\*<a href="src/modern_treasury/types/ledger_account_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account.py">SyncPage[LedgerAccount]</a></code>
- <code title="delete /api/ledger_accounts/{id}">client.ledger_accounts.<a href="./src/modern_treasury/resources/ledger_accounts.py">delete</a>(id) -> <a href="./src/modern_treasury/types/ledger_account.py">LedgerAccount</a></code>

# LedgerAccountPayouts

Types:

```python
from modern_treasury.types import LedgerAccountPayout
```

Methods:

- <code title="post /api/ledger_account_payouts">client.ledger_account_payouts.<a href="./src/modern_treasury/resources/ledger_account_payouts.py">create</a>(\*\*<a href="src/modern_treasury/types/ledger_account_payout_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account_payout.py">LedgerAccountPayout</a></code>
- <code title="patch /api/ledger_account_payouts/{id}">client.ledger_account_payouts.<a href="./src/modern_treasury/resources/ledger_account_payouts.py">update</a>(id, \*\*<a href="src/modern_treasury/types/ledger_account_payout_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account_payout.py">LedgerAccountPayout</a></code>
- <code title="get /api/ledger_account_payouts">client.ledger_account_payouts.<a href="./src/modern_treasury/resources/ledger_account_payouts.py">list</a>(\*\*<a href="src/modern_treasury/types/ledger_account_payout_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account_payout.py">SyncPage[LedgerAccountPayout]</a></code>
- <code title="get /api/ledger_account_payouts/{id}">client.ledger_account_payouts.<a href="./src/modern_treasury/resources/ledger_account_payouts.py">retireve</a>(id) -> <a href="./src/modern_treasury/types/ledger_account_payout.py">LedgerAccountPayout</a></code>

# LedgerAccountStatements

Types:

```python
from modern_treasury.types import (
    LedgerAccountStatementCreateResponse,
    LedgerAccountStatementRetrieveResponse,
)
```

Methods:

- <code title="post /api/ledger_account_statements">client.ledger_account_statements.<a href="./src/modern_treasury/resources/ledger_account_statements.py">create</a>(\*\*<a href="src/modern_treasury/types/ledger_account_statement_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_account_statement_create_response.py">LedgerAccountStatementCreateResponse</a></code>
- <code title="get /api/ledger_account_statements/{id}">client.ledger_account_statements.<a href="./src/modern_treasury/resources/ledger_account_statements.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/ledger_account_statement_retrieve_response.py">LedgerAccountStatementRetrieveResponse</a></code>

# LedgerEntries

Types:

```python
from modern_treasury.types import LedgerEntry
```

Methods:

- <code title="get /api/ledger_entries/{id}">client.ledger_entries.<a href="./src/modern_treasury/resources/ledger_entries.py">retrieve</a>(id, \*\*<a href="src/modern_treasury/types/ledger_entry_retrieve_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_entry.py">LedgerEntry</a></code>
- <code title="get /api/ledger_entries">client.ledger_entries.<a href="./src/modern_treasury/resources/ledger_entries.py">list</a>(\*\*<a href="src/modern_treasury/types/ledger_entry_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_entry.py">SyncPage[LedgerEntry]</a></code>

# LedgerEventHandlers

Types:

```python
from modern_treasury.types import (
    LedgerEventHandlerCreateResponse,
    LedgerEventHandlerRetrieveResponse,
    LedgerEventHandlerListResponse,
    LedgerEventHandlerDeleteResponse,
)
```

Methods:

- <code title="post /api/ledger_event_handlers">client.ledger_event_handlers.<a href="./src/modern_treasury/resources/ledger_event_handlers.py">create</a>(\*\*<a href="src/modern_treasury/types/ledger_event_handler_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_event_handler_create_response.py">LedgerEventHandlerCreateResponse</a></code>
- <code title="get /api/ledger_event_handlers/{id}">client.ledger_event_handlers.<a href="./src/modern_treasury/resources/ledger_event_handlers.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/ledger_event_handler_retrieve_response.py">LedgerEventHandlerRetrieveResponse</a></code>
- <code title="get /api/ledger_event_handlers">client.ledger_event_handlers.<a href="./src/modern_treasury/resources/ledger_event_handlers.py">list</a>(\*\*<a href="src/modern_treasury/types/ledger_event_handler_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_event_handler_list_response.py">SyncPage[LedgerEventHandlerListResponse]</a></code>
- <code title="delete /api/ledger_event_handlers/{id}">client.ledger_event_handlers.<a href="./src/modern_treasury/resources/ledger_event_handlers.py">delete</a>(id) -> <a href="./src/modern_treasury/types/ledger_event_handler_delete_response.py">LedgerEventHandlerDeleteResponse</a></code>

# LedgerTransactions

Types:

```python
from modern_treasury.types import LedgerTransaction
```

Methods:

- <code title="post /api/ledger_transactions">client.ledger_transactions.<a href="./src/modern_treasury/resources/ledger_transactions/ledger_transactions.py">create</a>(\*\*<a href="src/modern_treasury/types/ledger_transaction_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_transaction.py">LedgerTransaction</a></code>
- <code title="get /api/ledger_transactions/{id}">client.ledger_transactions.<a href="./src/modern_treasury/resources/ledger_transactions/ledger_transactions.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/ledger_transaction.py">LedgerTransaction</a></code>
- <code title="patch /api/ledger_transactions/{id}">client.ledger_transactions.<a href="./src/modern_treasury/resources/ledger_transactions/ledger_transactions.py">update</a>(id, \*\*<a href="src/modern_treasury/types/ledger_transaction_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_transaction.py">LedgerTransaction</a></code>
- <code title="get /api/ledger_transactions">client.ledger_transactions.<a href="./src/modern_treasury/resources/ledger_transactions/ledger_transactions.py">list</a>(\*\*<a href="src/modern_treasury/types/ledger_transaction_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_transaction.py">SyncPage[LedgerTransaction]</a></code>
- <code title="post /api/ledger_transactions/{ledger_transaction_id}/reversal">client.ledger_transactions.<a href="./src/modern_treasury/resources/ledger_transactions/ledger_transactions.py">create_reversal</a>(ledger_transaction_id, \*\*<a href="src/modern_treasury/types/ledger_transaction_create_reversal_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_transaction.py">LedgerTransaction</a></code>

## Versions

Types:

```python
from modern_treasury.types.ledger_transactions import LedgerTransactionVersion
```

Methods:

- <code title="get /api/ledger_transaction_versions">client.ledger_transactions.versions.<a href="./src/modern_treasury/resources/ledger_transactions/versions.py">list</a>(\*\*<a href="src/modern_treasury/types/ledger_transactions/version_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/ledger_transactions/ledger_transaction_version.py">SyncPage[LedgerTransactionVersion]</a></code>

# LineItems

Types:

```python
from modern_treasury.types import LineItem
```

Methods:

- <code title="get /api/{itemizable_type}/{itemizable_id}/line_items/{id}">client.line_items.<a href="./src/modern_treasury/resources/line_items.py">retrieve</a>(itemizable_type, itemizable_id, id) -> <a href="./src/modern_treasury/types/line_item.py">LineItem</a></code>
- <code title="patch /api/{itemizable_type}/{itemizable_id}/line_items/{id}">client.line_items.<a href="./src/modern_treasury/resources/line_items.py">update</a>(itemizable_type, itemizable_id, id, \*\*<a href="src/modern_treasury/types/line_item_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/line_item.py">LineItem</a></code>
- <code title="get /api/{itemizable_type}/{itemizable_id}/line_items">client.line_items.<a href="./src/modern_treasury/resources/line_items.py">list</a>(itemizable_type, itemizable_id, \*\*<a href="src/modern_treasury/types/line_item_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/line_item.py">SyncPage[LineItem]</a></code>

# PaymentFlows

Types:

```python
from modern_treasury.types import PaymentFlow
```

Methods:

- <code title="post /api/payment_flows">client.payment_flows.<a href="./src/modern_treasury/resources/payment_flows.py">create</a>(\*\*<a href="src/modern_treasury/types/payment_flow_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/payment_flow.py">PaymentFlow</a></code>
- <code title="get /api/payment_flows/{id}">client.payment_flows.<a href="./src/modern_treasury/resources/payment_flows.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/payment_flow.py">PaymentFlow</a></code>
- <code title="patch /api/payment_flows/{id}">client.payment_flows.<a href="./src/modern_treasury/resources/payment_flows.py">update</a>(id, \*\*<a href="src/modern_treasury/types/payment_flow_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/payment_flow.py">PaymentFlow</a></code>
- <code title="get /api/payment_flows">client.payment_flows.<a href="./src/modern_treasury/resources/payment_flows.py">list</a>(\*\*<a href="src/modern_treasury/types/payment_flow_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/payment_flow.py">SyncPage[PaymentFlow]</a></code>

# PaymentOrders

Types:

```python
from modern_treasury.types import PaymentOrder, PaymentOrderSubtype, PaymentOrderType
```

Methods:

- <code title="post /api/payment_orders">client.payment_orders.<a href="./src/modern_treasury/resources/payment_orders/payment_orders.py">create</a>(\*\*<a href="src/modern_treasury/types/payment_order_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/payment_order.py">PaymentOrder</a></code>
- <code title="get /api/payment_orders/{id}">client.payment_orders.<a href="./src/modern_treasury/resources/payment_orders/payment_orders.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/payment_order.py">PaymentOrder</a></code>
- <code title="patch /api/payment_orders/{id}">client.payment_orders.<a href="./src/modern_treasury/resources/payment_orders/payment_orders.py">update</a>(id, \*\*<a href="src/modern_treasury/types/payment_order_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/payment_order.py">PaymentOrder</a></code>
- <code title="get /api/payment_orders">client.payment_orders.<a href="./src/modern_treasury/resources/payment_orders/payment_orders.py">list</a>(\*\*<a href="src/modern_treasury/types/payment_order_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/payment_order.py">SyncPage[PaymentOrder]</a></code>
- <code title="post /api/payment_orders/create_async">client.payment_orders.<a href="./src/modern_treasury/resources/payment_orders/payment_orders.py">create_async</a>(\*\*<a href="src/modern_treasury/types/payment_order_create_async_params.py">params</a>) -> <a href="./src/modern_treasury/types/shared/async_response.py">shared.AsyncResponse</a></code>

## Reversals

Types:

```python
from modern_treasury.types.payment_orders import Reversal
```

Methods:

- <code title="post /api/payment_orders/{payment_order_id}/reversals">client.payment_orders.reversals.<a href="./src/modern_treasury/resources/payment_orders/reversals.py">create</a>(payment_order_id, \*\*<a href="src/modern_treasury/types/payment_orders/reversal_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/payment_orders/reversal.py">Reversal</a></code>
- <code title="get /api/payment_orders/{payment_order_id}/reversals/{reversal_id}">client.payment_orders.reversals.<a href="./src/modern_treasury/resources/payment_orders/reversals.py">retrieve</a>(payment_order_id, reversal_id) -> <a href="./src/modern_treasury/types/payment_orders/reversal.py">Reversal</a></code>
- <code title="get /api/payment_orders/{payment_order_id}/reversals">client.payment_orders.reversals.<a href="./src/modern_treasury/resources/payment_orders/reversals.py">list</a>(payment_order_id, \*\*<a href="src/modern_treasury/types/payment_orders/reversal_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/payment_orders/reversal.py">SyncPage[Reversal]</a></code>

# PaymentReferences

Types:

```python
from modern_treasury.types import PaymentReference
```

Methods:

- <code title="get /api/payment_references">client.payment_references.<a href="./src/modern_treasury/resources/payment_references.py">list</a>(\*\*<a href="src/modern_treasury/types/payment_reference_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/payment_reference.py">SyncPage[PaymentReference]</a></code>
- <code title="get /api/payment_references/{id}">client.payment_references.<a href="./src/modern_treasury/resources/payment_references.py">retireve</a>(id) -> <a href="./src/modern_treasury/types/payment_reference.py">PaymentReference</a></code>

# Returns

Types:

```python
from modern_treasury.types import ReturnObject
```

Methods:

- <code title="post /api/returns">client.returns.<a href="./src/modern_treasury/resources/returns.py">create</a>(\*\*<a href="src/modern_treasury/types/return_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/return_object.py">ReturnObject</a></code>
- <code title="get /api/returns/{id}">client.returns.<a href="./src/modern_treasury/resources/returns.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/return_object.py">ReturnObject</a></code>
- <code title="get /api/returns">client.returns.<a href="./src/modern_treasury/resources/returns.py">list</a>(\*\*<a href="src/modern_treasury/types/return_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/return_object.py">SyncPage[ReturnObject]</a></code>

# Transactions

Types:

```python
from modern_treasury.types import Transaction
```

Methods:

- <code title="get /api/transactions/{id}">client.transactions.<a href="./src/modern_treasury/resources/transactions/transactions.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/transaction.py">Transaction</a></code>
- <code title="patch /api/transactions/{id}">client.transactions.<a href="./src/modern_treasury/resources/transactions/transactions.py">update</a>(id, \*\*<a href="src/modern_treasury/types/transaction_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/transaction.py">Transaction</a></code>
- <code title="get /api/transactions">client.transactions.<a href="./src/modern_treasury/resources/transactions/transactions.py">list</a>(\*\*<a href="src/modern_treasury/types/transaction_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/transaction.py">SyncPage[Transaction]</a></code>

## LineItems

Types:

```python
from modern_treasury.types.transactions import TransactionLineItem
```

Methods:

- <code title="get /api/transactions/{transaction_id}/line_items">client.transactions.line_items.<a href="./src/modern_treasury/resources/transactions/line_items.py">list</a>(transaction_id, \*\*<a href="src/modern_treasury/types/transactions/line_item_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/transactions/transaction_line_item.py">SyncPage[TransactionLineItem]</a></code>

# Validations

Types:

```python
from modern_treasury.types import RoutingNumberLookupRequest
```

Methods:

- <code title="get /api/validations/routing_numbers">client.validations.<a href="./src/modern_treasury/resources/validations.py">validate_routing_number</a>(\*\*<a href="src/modern_treasury/types/validation_validate_routing_number_params.py">params</a>) -> <a href="./src/modern_treasury/types/routing_number_lookup_request.py">RoutingNumberLookupRequest</a></code>

# PaperItems

Types:

```python
from modern_treasury.types import PaperItem
```

Methods:

- <code title="get /api/paper_items/{id}">client.paper_items.<a href="./src/modern_treasury/resources/paper_items.py">retrieve</a>(id) -> <a href="./src/modern_treasury/types/paper_item.py">PaperItem</a></code>
- <code title="get /api/paper_items">client.paper_items.<a href="./src/modern_treasury/resources/paper_items.py">list</a>(\*\*<a href="src/modern_treasury/types/paper_item_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/paper_item.py">SyncPage[PaperItem]</a></code>

# Webhooks

Custom Methods:

- `get_signature`
- `validate_signature`

# VirtualAccounts

Types:

```python
from modern_treasury.types import VirtualAccount
```

Methods:

- <code title="post /api/virtual_accounts">client.virtual_accounts.<a href="./src/modern_treasury/resources/virtual_accounts.py">create</a>(\*\*<a href="src/modern_treasury/types/virtual_account_create_params.py">params</a>) -> <a href="./src/modern_treasury/types/virtual_account.py">VirtualAccount</a></code>
- <code title="get /api/virtual_accounts/{id}">client.virtual_accounts.<a href="./src/modern_treasury/resources/virtual_accounts.py">retrieve</a>(id) -> None</code>
- <code title="patch /api/virtual_accounts/{id}">client.virtual_accounts.<a href="./src/modern_treasury/resources/virtual_accounts.py">update</a>(id, \*\*<a href="src/modern_treasury/types/virtual_account_update_params.py">params</a>) -> <a href="./src/modern_treasury/types/virtual_account.py">VirtualAccount</a></code>
- <code title="get /api/virtual_accounts">client.virtual_accounts.<a href="./src/modern_treasury/resources/virtual_accounts.py">list</a>(\*\*<a href="src/modern_treasury/types/virtual_account_list_params.py">params</a>) -> <a href="./src/modern_treasury/types/virtual_account.py">SyncPage[VirtualAccount]</a></code>
- <code title="delete /api/virtual_accounts/{id}">client.virtual_accounts.<a href="./src/modern_treasury/resources/virtual_accounts.py">delete</a>(id) -> <a href="./src/modern_treasury/types/virtual_account.py">VirtualAccount</a></code>