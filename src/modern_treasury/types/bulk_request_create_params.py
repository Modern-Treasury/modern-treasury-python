# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .shared import Currency, TransactionDirection
from .._utils import PropertyInfo
from .payment_order_type import PaymentOrderType
from .expected_payment_type import ExpectedPaymentType
from .external_account_type import ExternalAccountType
from .payment_order_subtype import PaymentOrderSubtype

__all__ = [
    "BulkRequestCreateParams",
    "Resources",
    "Resource",
    "ResourcesPaymentOrderAsyncCreateRequest",
    "ResourcePaymentOrderAsyncCreateRequest",
    "ResourcesPaymentOrderAsyncCreateRequestAccounting",
    "ResourcePaymentOrderAsyncCreateRequestAccounting",
    "ResourcesPaymentOrderAsyncCreateRequestLedgerTransaction",
    "ResourcePaymentOrderAsyncCreateRequestLedgerTransaction",
    "ResourcesPaymentOrderAsyncCreateRequestLedgerTransactionLedgerEntries",
    "ResourcePaymentOrderAsyncCreateRequestLedgerTransactionLedgerEntry",
    "ResourcesPaymentOrderAsyncCreateRequestLineItems",
    "ResourcePaymentOrderAsyncCreateRequestLineItem",
    "ResourcesPaymentOrderAsyncCreateRequestReceivingAccount",
    "ResourcePaymentOrderAsyncCreateRequestReceivingAccount",
    "ResourcesPaymentOrderAsyncCreateRequestReceivingAccountAccountDetails",
    "ResourcePaymentOrderAsyncCreateRequestReceivingAccountAccountDetail",
    "ResourcesPaymentOrderAsyncCreateRequestReceivingAccountContactDetails",
    "ResourcePaymentOrderAsyncCreateRequestReceivingAccountContactDetail",
    "ResourcesPaymentOrderAsyncCreateRequestReceivingAccountLedgerAccount",
    "ResourcePaymentOrderAsyncCreateRequestReceivingAccountLedgerAccount",
    "ResourcesPaymentOrderAsyncCreateRequestReceivingAccountPartyAddress",
    "ResourcePaymentOrderAsyncCreateRequestReceivingAccountPartyAddress",
    "ResourcesPaymentOrderAsyncCreateRequestReceivingAccountRoutingDetails",
    "ResourcePaymentOrderAsyncCreateRequestReceivingAccountRoutingDetail",
    "ResourcesExpectedPaymentCreateRequest",
    "ResourceExpectedPaymentCreateRequest",
    "ResourcesExpectedPaymentCreateRequestLedgerTransaction",
    "ResourceExpectedPaymentCreateRequestLedgerTransaction",
    "ResourcesExpectedPaymentCreateRequestLedgerTransactionLedgerEntries",
    "ResourceExpectedPaymentCreateRequestLedgerTransactionLedgerEntry",
    "ResourcesExpectedPaymentCreateRequestLineItems",
    "ResourceExpectedPaymentCreateRequestLineItem",
    "ResourcesLedgerTransactionCreateRequest",
    "ResourceLedgerTransactionCreateRequest",
    "ResourcesLedgerTransactionCreateRequestLedgerEntries",
    "ResourceLedgerTransactionCreateRequestLedgerEntry",
    "ResourcesPaymentOrderUpdateRequestWithID",
    "ResourcePaymentOrderUpdateRequestWithID",
    "ResourcesPaymentOrderUpdateRequestWithIDAccounting",
    "ResourcePaymentOrderUpdateRequestWithIDAccounting",
    "ResourcesPaymentOrderUpdateRequestWithIDLineItems",
    "ResourcePaymentOrderUpdateRequestWithIDLineItem",
    "ResourcesPaymentOrderUpdateRequestWithIDReceivingAccount",
    "ResourcePaymentOrderUpdateRequestWithIDReceivingAccount",
    "ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountAccountDetails",
    "ResourcePaymentOrderUpdateRequestWithIDReceivingAccountAccountDetail",
    "ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountContactDetails",
    "ResourcePaymentOrderUpdateRequestWithIDReceivingAccountContactDetail",
    "ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountLedgerAccount",
    "ResourcePaymentOrderUpdateRequestWithIDReceivingAccountLedgerAccount",
    "ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountPartyAddress",
    "ResourcePaymentOrderUpdateRequestWithIDReceivingAccountPartyAddress",
    "ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountRoutingDetails",
    "ResourcePaymentOrderUpdateRequestWithIDReceivingAccountRoutingDetail",
    "ResourcesExpectedPaymentUpdateRequestWithID",
    "ResourceExpectedPaymentUpdateRequestWithID",
    "ResourcesLedgerTransactionUpdateRequestWithID",
    "ResourceLedgerTransactionUpdateRequestWithID",
    "ResourcesLedgerTransactionUpdateRequestWithIDLedgerEntries",
    "ResourceLedgerTransactionUpdateRequestWithIDLedgerEntry",
]


class BulkRequestCreateParams(TypedDict, total=False):
    action_type: Required[Literal["create", "update"]]
    """One of create, or update."""

    resource_type: Required[Literal["payment_order", "ledger_transaction", "expected_payment"]]
    """One of payment_order, expected_payment, or ledger_transaction."""

    resources: Required[Iterable[Resource]]
    """
    An array of objects where each object contains the input params for a single
    `action_type` request on a `resource_type` resource
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class ResourcePaymentOrderAsyncCreateRequestAccounting(TypedDict, total=False):
    account_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    class_id: Optional[str]
    """The ID of one of the class objects in your accounting system.

    Class objects track segments of your business independent of client or project.
    Note that these will only be accessible if your accounting system has been
    connected.
    """


ResourcesPaymentOrderAsyncCreateRequestAccounting = ResourcePaymentOrderAsyncCreateRequestAccounting
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestAccounting instead.
"""


class ResourcePaymentOrderAsyncCreateRequestLedgerTransactionLedgerEntry(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    direction: Required[TransactionDirection]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    ledger_account_id: Required[str]
    """The ledger account that this ledger entry is associated with."""

    available_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s available balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    lock_version: Optional[int]
    """Lock version of the ledger account.

    This can be passed when creating a ledger transaction to only succeed if no
    ledger transactions have posted since the given version. See our post about
    Designing the Ledgers API with Optimistic Locking for more details.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    pending_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s pending balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    posted_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s posted balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    show_resulting_ledger_account_balances: Optional[bool]
    """
    If true, response will include the balance of the associated ledger account for
    the entry.
    """


ResourcesPaymentOrderAsyncCreateRequestLedgerTransactionLedgerEntries = (
    ResourcePaymentOrderAsyncCreateRequestLedgerTransactionLedgerEntry
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestLedgerTransactionLedgerEntry instead.
"""


class ResourcePaymentOrderAsyncCreateRequestLedgerTransaction(TypedDict, total=False):
    ledger_entries: Required[Iterable[ResourcePaymentOrderAsyncCreateRequestLedgerTransactionLedgerEntry]]
    """An array of ledger entry objects."""

    description: Optional[str]
    """An optional description for internal use."""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
    purposes.
    """

    external_id: str
    """A unique string to represent the ledger transaction.

    Only one pending or posted ledger transaction may have this ID in the ledger.
    """

    ledgerable_id: str
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the id will be populated here, otherwise null.
    """

    ledgerable_type: Literal[
        "counterparty",
        "expected_payment",
        "incoming_payment_detail",
        "internal_account",
        "line_item",
        "paper_item",
        "payment_order",
        "payment_order_attempt",
        "return",
        "reversal",
    ]
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the type will be populated here, otherwise null. This can be one of
    payment_order, incoming_payment_detail, expected_payment, return, or reversal.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    status: Literal["archived", "pending", "posted"]
    """To post a ledger transaction at creation, use `posted`."""


ResourcesPaymentOrderAsyncCreateRequestLedgerTransaction = ResourcePaymentOrderAsyncCreateRequestLedgerTransaction
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestLedgerTransaction instead.
"""


class ResourcePaymentOrderAsyncCreateRequestLineItem(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    accounting_category_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    description: Optional[str]
    """A free-form description of the line item."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


ResourcesPaymentOrderAsyncCreateRequestLineItems = ResourcePaymentOrderAsyncCreateRequestLineItem
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestLineItem instead.
"""


class ResourcePaymentOrderAsyncCreateRequestReceivingAccountAccountDetail(TypedDict, total=False):
    account_number: Required[str]

    account_number_type: Literal["iban", "hk_number", "clabe", "wallet_address", "pan", "other"]


ResourcesPaymentOrderAsyncCreateRequestReceivingAccountAccountDetails = (
    ResourcePaymentOrderAsyncCreateRequestReceivingAccountAccountDetail
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestReceivingAccountAccountDetail instead.
"""


class ResourcePaymentOrderAsyncCreateRequestReceivingAccountContactDetail(TypedDict, total=False):
    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number", "website"]


ResourcesPaymentOrderAsyncCreateRequestReceivingAccountContactDetails = (
    ResourcePaymentOrderAsyncCreateRequestReceivingAccountContactDetail
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestReceivingAccountContactDetail instead.
"""


class ResourcePaymentOrderAsyncCreateRequestReceivingAccountLedgerAccount(TypedDict, total=False):
    currency: Required[str]
    """The currency of the ledger account."""

    ledger_id: Required[str]
    """The id of the ledger that this account belongs to."""

    name: Required[str]
    """The name of the ledger account."""

    normal_balance: Required[TransactionDirection]
    """The normal balance of the ledger account."""

    currency_exponent: Optional[int]
    """The currency exponent of the ledger account."""

    description: Optional[str]
    """The description of the ledger account."""

    ledger_account_category_ids: List[str]
    """
    The array of ledger account category ids that this ledger account should be a
    child of.
    """

    ledgerable_id: str
    """
    If the ledger account links to another object in Modern Treasury, the id will be
    populated here, otherwise null.
    """

    ledgerable_type: Literal["external_account", "internal_account", "virtual_account"]
    """
    If the ledger account links to another object in Modern Treasury, the type will
    be populated here, otherwise null. The value is one of internal_account or
    external_account.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


ResourcesPaymentOrderAsyncCreateRequestReceivingAccountLedgerAccount = (
    ResourcePaymentOrderAsyncCreateRequestReceivingAccountLedgerAccount
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestReceivingAccountLedgerAccount instead.
"""


class ResourcePaymentOrderAsyncCreateRequestReceivingAccountPartyAddress(TypedDict, total=False):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str]

    line2: Optional[str]

    locality: Optional[str]
    """Locality or City."""

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State."""


ResourcesPaymentOrderAsyncCreateRequestReceivingAccountPartyAddress = (
    ResourcePaymentOrderAsyncCreateRequestReceivingAccountPartyAddress
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestReceivingAccountPartyAddress instead.
"""


class ResourcePaymentOrderAsyncCreateRequestReceivingAccountRoutingDetail(TypedDict, total=False):
    routing_number: Required[str]

    routing_number_type: Required[
        Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "dk_interbank_clearing_code",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "hu_interbank_clearing_code",
            "id_sknbi_code",
            "in_ifsc",
            "jp_zengin_code",
            "my_branch_code",
            "mx_bank_identifier",
            "nz_national_clearing_code",
            "pl_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ]
    ]

    payment_type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "chats",
        "check",
        "cross_border",
        "dk_nets",
        "eft",
        "hu_ics",
        "interac",
        "masav",
        "mx_ccen",
        "neft",
        "nics",
        "nz_becs",
        "pl_elixir",
        "provxchange",
        "ro_sent",
        "rtp",
        "sg_giro",
        "se_bankgirot",
        "sen",
        "sepa",
        "sic",
        "signet",
        "sknbi",
        "wire",
        "zengin",
    ]


ResourcesPaymentOrderAsyncCreateRequestReceivingAccountRoutingDetails = (
    ResourcePaymentOrderAsyncCreateRequestReceivingAccountRoutingDetail
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestReceivingAccountRoutingDetail instead.
"""


class ResourcePaymentOrderAsyncCreateRequestReceivingAccount(TypedDict, total=False):
    account_details: Iterable[ResourcePaymentOrderAsyncCreateRequestReceivingAccountAccountDetail]

    account_type: ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    contact_details: Iterable[ResourcePaymentOrderAsyncCreateRequestReceivingAccountContactDetail]

    ledger_account: ResourcePaymentOrderAsyncCreateRequestReceivingAccountLedgerAccount
    """Specifies a ledger account object that will be created with the external
    account.

    The resulting ledger account is linked to the external account for
    auto-ledgering Payment objects. See
    https://docs.moderntreasury.com/docs/linking-to-other-modern-treasury-objects
    for more details.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str]
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    party_address: ResourcePaymentOrderAsyncCreateRequestReceivingAccountPartyAddress
    """Required if receiving wire payments."""

    party_identifier: str

    party_name: str
    """
    If this value isn't provided, it will be inherited from the counterparty's name.
    """

    party_type: Optional[Literal["business", "individual"]]
    """Either `individual` or `business`."""

    plaid_processor_token: str
    """
    If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
    you can pass the processor token in this field.
    """

    routing_details: Iterable[ResourcePaymentOrderAsyncCreateRequestReceivingAccountRoutingDetail]


ResourcesPaymentOrderAsyncCreateRequestReceivingAccount = ResourcePaymentOrderAsyncCreateRequestReceivingAccount
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequestReceivingAccount instead.
"""


class ResourcePaymentOrderAsyncCreateRequest(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000 (cents). For RTP, the maximum amount
    allowed by the network is $100,000.
    """

    direction: Required[Literal["credit", "debit"]]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    originating_account_id: Required[str]
    """The ID of one of your organization's internal accounts."""

    type: Required[PaymentOrderType]
    """
    One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
    `bacs`, `au_becs`, `interac`, `neft`, `nics`, `nz_national_clearing_code`,
    `sic`, `signet`, `provexchange`, `zengin`.
    """

    accounting: ResourcePaymentOrderAsyncCreateRequestAccounting

    accounting_category_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    accounting_ledger_class_id: Optional[str]
    """The ID of one of your accounting ledger classes.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    charge_bearer: Optional[Literal["shared", "sender", "receiver"]]
    """The party that will pay the fees for the payment order.

    Only applies to wire payment orders. Can be one of shared, sender, or receiver,
    which correspond respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.
    """

    currency: Optional[Currency]
    """Defaults to the currency of the originating account."""

    description: Optional[str]
    """An optional description for internal use."""

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date transactions are to be posted to the participants' account.

    Defaults to the current business day or the next business day if the current day
    is a bank holiday or weekend. Format: yyyy-mm-dd.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """RFP payments require an expires_at. This value must be past the effective_date."""

    fallback_type: Literal["ach"]
    """
    A payment type to fallback to if the original type is not valid for the
    receiving account. Currently, this only supports falling back from RTP to ACH
    (type=rtp and fallback_type=ach)
    """

    foreign_exchange_contract: Optional[str]
    """
    If present, indicates a specific foreign exchange contract number that has been
    generated by your financial institution.
    """

    foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]]
    """
    Indicates the type of FX transfer to initiate, can be either
    `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
    currency matches the originating account currency.
    """

    ledger_transaction: ResourcePaymentOrderAsyncCreateRequestLedgerTransaction
    """
    Specifies a ledger transaction object that will be created with the payment
    order. If the ledger transaction cannot be created, then the payment order
    creation will fail. The resulting ledger transaction will mirror the status of
    the payment order.
    """

    ledger_transaction_id: str
    """Either ledger_transaction or ledger_transaction_id can be provided.

    Only a pending ledger transaction can be attached upon payment order creation.
    Once the payment order is created, the status of the ledger transaction tracks
    the payment order automatically.
    """

    line_items: Iterable[ResourcePaymentOrderAsyncCreateRequestLineItem]
    """An array of line items that must sum up to the amount of the payment order."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    nsf_protected: bool
    """A boolean to determine if NSF Protection is enabled for this payment order.

    Note that this setting must also be turned on in your organization settings
    page.
    """

    originating_party_name: Optional[str]
    """
    If present, this will replace your default company name on receiver's bank
    statement. This field can only be used for ACH payments currently. For ACH, only
    the first 16 characters of this string will be used. Any additional characters
    will be truncated.
    """

    priority: Literal["high", "normal"]
    """Either `normal` or `high`.

    For ACH and EFT payments, `high` represents a same-day ACH or EFT transfer,
    respectively. For check payments, `high` can mean an overnight check rather than
    standard mail.
    """

    process_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """If present, Modern Treasury will not process the payment until after this time.

    If `process_after` is past the cutoff for `effective_date`, `process_after` will
    take precedence and `effective_date` will automatically update to reflect the
    earliest possible sending date after `process_after`. Format is ISO8601
    timestamp.
    """

    purpose: Optional[str]
    """
    For `wire`, this is usually the purpose which is transmitted via the
    "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
    this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
    CPA Code that will be attached to the payment.
    """

    receiving_account: ResourcePaymentOrderAsyncCreateRequestReceivingAccount
    """Either `receiving_account` or `receiving_account_id` must be present.

    When using `receiving_account_id`, you may pass the id of an external account or
    an internal account.
    """

    receiving_account_id: str
    """Either `receiving_account` or `receiving_account_id` must be present.

    When using `receiving_account_id`, you may pass the id of an external account or
    an internal account.
    """

    remittance_information: Optional[str]
    """For `ach`, this field will be passed through on an addenda record.

    For `wire` payments the field will be passed through as the "Originator to
    Beneficiary Information", also known as OBI or Fedwire tag 6000.
    """

    send_remittance_advice: Optional[bool]
    """Send an email to the counterparty when the payment order is sent to the bank.

    If `null`, `send_remittance_advice` on the Counterparty is used.
    """

    statement_descriptor: Optional[str]
    """An optional descriptor which will appear in the receiver's statement.

    For `check` payments this field will be used as the memo line. For `ach` the
    maximum length is 10 characters. Note that for ACH payments, the name on your
    bank account will be included automatically by the bank, so you can use the
    characters for other useful information. For `eft` the maximum length is 15
    characters.
    """

    subtype: Optional[PaymentOrderSubtype]
    """
    An additional layer of classification for the type of payment order you are
    doing. This field is only used for `ach` payment orders currently. For `ach`
    payment orders, the `subtype` represents the SEC code. We currently support
    `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.
    """

    transaction_monitoring_enabled: bool
    """
    A flag that determines whether a payment order should go through transaction
    monitoring.
    """

    ultimate_originating_party_identifier: Optional[str]
    """Identifier of the ultimate originator of the payment order."""

    ultimate_originating_party_name: Optional[str]
    """Name of the ultimate originator of the payment order."""

    ultimate_receiving_party_identifier: Optional[str]
    """Identifier of the ultimate funds recipient."""

    ultimate_receiving_party_name: Optional[str]
    """Name of the ultimate funds recipient."""


ResourcesPaymentOrderAsyncCreateRequest = ResourcePaymentOrderAsyncCreateRequest
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderAsyncCreateRequest instead.
"""


class ResourceExpectedPaymentCreateRequestLedgerTransactionLedgerEntry(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    direction: Required[TransactionDirection]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    ledger_account_id: Required[str]
    """The ledger account that this ledger entry is associated with."""

    available_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s available balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    lock_version: Optional[int]
    """Lock version of the ledger account.

    This can be passed when creating a ledger transaction to only succeed if no
    ledger transactions have posted since the given version. See our post about
    Designing the Ledgers API with Optimistic Locking for more details.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    pending_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s pending balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    posted_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s posted balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    show_resulting_ledger_account_balances: Optional[bool]
    """
    If true, response will include the balance of the associated ledger account for
    the entry.
    """


ResourcesExpectedPaymentCreateRequestLedgerTransactionLedgerEntries = (
    ResourceExpectedPaymentCreateRequestLedgerTransactionLedgerEntry
)
"""This type is deprecated and will be removed in a future release.

Please use ResourceExpectedPaymentCreateRequestLedgerTransactionLedgerEntry instead.
"""


class ResourceExpectedPaymentCreateRequestLedgerTransaction(TypedDict, total=False):
    ledger_entries: Required[Iterable[ResourceExpectedPaymentCreateRequestLedgerTransactionLedgerEntry]]
    """An array of ledger entry objects."""

    description: Optional[str]
    """An optional description for internal use."""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
    purposes.
    """

    external_id: str
    """A unique string to represent the ledger transaction.

    Only one pending or posted ledger transaction may have this ID in the ledger.
    """

    ledgerable_id: str
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the id will be populated here, otherwise null.
    """

    ledgerable_type: Literal[
        "counterparty",
        "expected_payment",
        "incoming_payment_detail",
        "internal_account",
        "line_item",
        "paper_item",
        "payment_order",
        "payment_order_attempt",
        "return",
        "reversal",
    ]
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the type will be populated here, otherwise null. This can be one of
    payment_order, incoming_payment_detail, expected_payment, return, or reversal.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    status: Literal["archived", "pending", "posted"]
    """To post a ledger transaction at creation, use `posted`."""


ResourcesExpectedPaymentCreateRequestLedgerTransaction = ResourceExpectedPaymentCreateRequestLedgerTransaction
"""This type is deprecated and will be removed in a future release.

Please use ResourceExpectedPaymentCreateRequestLedgerTransaction instead.
"""


class ResourceExpectedPaymentCreateRequestLineItem(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    accounting_category_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    description: Optional[str]
    """A free-form description of the line item."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


ResourcesExpectedPaymentCreateRequestLineItems = ResourceExpectedPaymentCreateRequestLineItem
"""This type is deprecated and will be removed in a future release.

Please use ResourceExpectedPaymentCreateRequestLineItem instead.
"""


class ResourceExpectedPaymentCreateRequest(TypedDict, total=False):
    amount_lower_bound: Required[int]
    """The lowest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    amount_upper_bound: Required[int]
    """The highest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    direction: Required[TransactionDirection]
    """One of credit or debit.

    When you are receiving money, use credit. When you are being charged, use debit.
    """

    internal_account_id: Required[str]
    """The ID of the Internal Account for the expected payment."""

    counterparty_id: Optional[str]
    """The ID of the counterparty you expect for this payment."""

    currency: Optional[Currency]
    """Must conform to ISO 4217. Defaults to the currency of the internal account."""

    date_lower_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The earliest date the payment may come in. Format: yyyy-mm-dd"""

    date_upper_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The latest date the payment may come in. Format: yyyy-mm-dd"""

    description: Optional[str]
    """An optional description for internal use."""

    ledger_transaction: ResourceExpectedPaymentCreateRequestLedgerTransaction
    """
    Specifies a ledger transaction object that will be created with the expected
    payment. If the ledger transaction cannot be created, then the expected payment
    creation will fail. The resulting ledger transaction will mirror the status of
    the expected payment.
    """

    ledger_transaction_id: str
    """Either ledger_transaction or ledger_transaction_id can be provided.

    Only a pending ledger transaction can be attached upon expected payment
    creation. Once the expected payment is created, the status of the ledger
    transaction tracks the expected payment automatically.
    """

    line_items: Iterable[ResourceExpectedPaymentCreateRequestLineItem]

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    reconciliation_filters: Optional[object]
    """The reconciliation filters you have for this payment."""

    reconciliation_groups: Optional[object]
    """The reconciliation groups you have for this payment."""

    reconciliation_rule_variables: Optional[Iterable[object]]
    """An array of reconciliation rule variables for this payment."""

    remittance_information: Optional[str]
    """For `ach`, this field will be passed through on an addenda record.

    For `wire` payments the field will be passed through as the "Originator to
    Beneficiary Information", also known as OBI or Fedwire tag 6000.
    """

    statement_descriptor: Optional[str]
    """The statement description you expect to see on the transaction.

    For ACH payments, this will be the full line item passed from the bank. For wire
    payments, this will be the OBI field on the wire. For check payments, this will
    be the memo field.
    """

    type: Optional[ExpectedPaymentType]
    """
    One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
    sepa, signet, wire.
    """


ResourcesExpectedPaymentCreateRequest = ResourceExpectedPaymentCreateRequest
"""This type is deprecated and will be removed in a future release.

Please use ResourceExpectedPaymentCreateRequest instead.
"""


class ResourceLedgerTransactionCreateRequestLedgerEntry(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    direction: Required[TransactionDirection]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    ledger_account_id: Required[str]
    """The ledger account that this ledger entry is associated with."""

    available_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s available balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    lock_version: Optional[int]
    """Lock version of the ledger account.

    This can be passed when creating a ledger transaction to only succeed if no
    ledger transactions have posted since the given version. See our post about
    Designing the Ledgers API with Optimistic Locking for more details.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    pending_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s pending balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    posted_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s posted balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    show_resulting_ledger_account_balances: Optional[bool]
    """
    If true, response will include the balance of the associated ledger account for
    the entry.
    """


ResourcesLedgerTransactionCreateRequestLedgerEntries = ResourceLedgerTransactionCreateRequestLedgerEntry
"""This type is deprecated and will be removed in a future release.

Please use ResourceLedgerTransactionCreateRequestLedgerEntry instead.
"""


class ResourceLedgerTransactionCreateRequest(TypedDict, total=False):
    ledger_entries: Required[Iterable[ResourceLedgerTransactionCreateRequestLedgerEntry]]
    """An array of ledger entry objects."""

    description: Optional[str]
    """An optional description for internal use."""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The date (YYYY-MM-DD) on which the ledger transaction happened for reporting
    purposes.
    """

    external_id: str
    """A unique string to represent the ledger transaction.

    Only one pending or posted ledger transaction may have this ID in the ledger.
    """

    ledgerable_id: str
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the id will be populated here, otherwise null.
    """

    ledgerable_type: Literal[
        "counterparty",
        "expected_payment",
        "incoming_payment_detail",
        "internal_account",
        "line_item",
        "paper_item",
        "payment_order",
        "payment_order_attempt",
        "return",
        "reversal",
    ]
    """
    If the ledger transaction can be reconciled to another object in Modern
    Treasury, the type will be populated here, otherwise null. This can be one of
    payment_order, incoming_payment_detail, expected_payment, return, or reversal.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    status: Literal["archived", "pending", "posted"]
    """To post a ledger transaction at creation, use `posted`."""


ResourcesLedgerTransactionCreateRequest = ResourceLedgerTransactionCreateRequest
"""This type is deprecated and will be removed in a future release.

Please use ResourceLedgerTransactionCreateRequest instead.
"""


class ResourcePaymentOrderUpdateRequestWithIDAccounting(TypedDict, total=False):
    account_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    class_id: Optional[str]
    """The ID of one of the class objects in your accounting system.

    Class objects track segments of your business independent of client or project.
    Note that these will only be accessible if your accounting system has been
    connected.
    """


ResourcesPaymentOrderUpdateRequestWithIDAccounting = ResourcePaymentOrderUpdateRequestWithIDAccounting
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithIDAccounting instead.
"""


class ResourcePaymentOrderUpdateRequestWithIDLineItem(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    accounting_category_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    description: Optional[str]
    """A free-form description of the line item."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


ResourcesPaymentOrderUpdateRequestWithIDLineItems = ResourcePaymentOrderUpdateRequestWithIDLineItem
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithIDLineItem instead.
"""


class ResourcePaymentOrderUpdateRequestWithIDReceivingAccountAccountDetail(TypedDict, total=False):
    account_number: Required[str]

    account_number_type: Literal["iban", "hk_number", "clabe", "wallet_address", "pan", "other"]


ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountAccountDetails = (
    ResourcePaymentOrderUpdateRequestWithIDReceivingAccountAccountDetail
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithIDReceivingAccountAccountDetail instead.
"""


class ResourcePaymentOrderUpdateRequestWithIDReceivingAccountContactDetail(TypedDict, total=False):
    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number", "website"]


ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountContactDetails = (
    ResourcePaymentOrderUpdateRequestWithIDReceivingAccountContactDetail
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithIDReceivingAccountContactDetail instead.
"""


class ResourcePaymentOrderUpdateRequestWithIDReceivingAccountLedgerAccount(TypedDict, total=False):
    currency: Required[str]
    """The currency of the ledger account."""

    ledger_id: Required[str]
    """The id of the ledger that this account belongs to."""

    name: Required[str]
    """The name of the ledger account."""

    normal_balance: Required[TransactionDirection]
    """The normal balance of the ledger account."""

    currency_exponent: Optional[int]
    """The currency exponent of the ledger account."""

    description: Optional[str]
    """The description of the ledger account."""

    ledger_account_category_ids: List[str]
    """
    The array of ledger account category ids that this ledger account should be a
    child of.
    """

    ledgerable_id: str
    """
    If the ledger account links to another object in Modern Treasury, the id will be
    populated here, otherwise null.
    """

    ledgerable_type: Literal["external_account", "internal_account", "virtual_account"]
    """
    If the ledger account links to another object in Modern Treasury, the type will
    be populated here, otherwise null. The value is one of internal_account or
    external_account.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountLedgerAccount = (
    ResourcePaymentOrderUpdateRequestWithIDReceivingAccountLedgerAccount
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithIDReceivingAccountLedgerAccount instead.
"""


class ResourcePaymentOrderUpdateRequestWithIDReceivingAccountPartyAddress(TypedDict, total=False):
    country: Optional[str]
    """Country code conforms to [ISO 3166-1 alpha-2]"""

    line1: Optional[str]

    line2: Optional[str]

    locality: Optional[str]
    """Locality or City."""

    postal_code: Optional[str]
    """The postal code of the address."""

    region: Optional[str]
    """Region or State."""


ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountPartyAddress = (
    ResourcePaymentOrderUpdateRequestWithIDReceivingAccountPartyAddress
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithIDReceivingAccountPartyAddress instead.
"""


class ResourcePaymentOrderUpdateRequestWithIDReceivingAccountRoutingDetail(TypedDict, total=False):
    routing_number: Required[str]

    routing_number_type: Required[
        Literal[
            "aba",
            "au_bsb",
            "br_codigo",
            "ca_cpa",
            "chips",
            "cnaps",
            "dk_interbank_clearing_code",
            "gb_sort_code",
            "hk_interbank_clearing_code",
            "hu_interbank_clearing_code",
            "id_sknbi_code",
            "in_ifsc",
            "jp_zengin_code",
            "my_branch_code",
            "mx_bank_identifier",
            "nz_national_clearing_code",
            "pl_national_clearing_code",
            "se_bankgiro_clearing_code",
            "swift",
        ]
    ]

    payment_type: Literal[
        "ach",
        "au_becs",
        "bacs",
        "book",
        "card",
        "chats",
        "check",
        "cross_border",
        "dk_nets",
        "eft",
        "hu_ics",
        "interac",
        "masav",
        "mx_ccen",
        "neft",
        "nics",
        "nz_becs",
        "pl_elixir",
        "provxchange",
        "ro_sent",
        "rtp",
        "sg_giro",
        "se_bankgirot",
        "sen",
        "sepa",
        "sic",
        "signet",
        "sknbi",
        "wire",
        "zengin",
    ]


ResourcesPaymentOrderUpdateRequestWithIDReceivingAccountRoutingDetails = (
    ResourcePaymentOrderUpdateRequestWithIDReceivingAccountRoutingDetail
)
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithIDReceivingAccountRoutingDetail instead.
"""


class ResourcePaymentOrderUpdateRequestWithIDReceivingAccount(TypedDict, total=False):
    account_details: Iterable[ResourcePaymentOrderUpdateRequestWithIDReceivingAccountAccountDetail]

    account_type: ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    contact_details: Iterable[ResourcePaymentOrderUpdateRequestWithIDReceivingAccountContactDetail]

    ledger_account: ResourcePaymentOrderUpdateRequestWithIDReceivingAccountLedgerAccount
    """Specifies a ledger account object that will be created with the external
    account.

    The resulting ledger account is linked to the external account for
    auto-ledgering Payment objects. See
    https://docs.moderntreasury.com/docs/linking-to-other-modern-treasury-objects
    for more details.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    name: Optional[str]
    """A nickname for the external account.

    This is only for internal usage and won't affect any payments
    """

    party_address: ResourcePaymentOrderUpdateRequestWithIDReceivingAccountPartyAddress
    """Required if receiving wire payments."""

    party_identifier: str

    party_name: str
    """
    If this value isn't provided, it will be inherited from the counterparty's name.
    """

    party_type: Optional[Literal["business", "individual"]]
    """Either `individual` or `business`."""

    plaid_processor_token: str
    """
    If you've enabled the Modern Treasury + Plaid integration in your Plaid account,
    you can pass the processor token in this field.
    """

    routing_details: Iterable[ResourcePaymentOrderUpdateRequestWithIDReceivingAccountRoutingDetail]


ResourcesPaymentOrderUpdateRequestWithIDReceivingAccount = ResourcePaymentOrderUpdateRequestWithIDReceivingAccount
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithIDReceivingAccount instead.
"""


class ResourcePaymentOrderUpdateRequestWithID(TypedDict, total=False):
    id: str

    accounting: ResourcePaymentOrderUpdateRequestWithIDAccounting

    accounting_category_id: Optional[str]
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    accounting_ledger_class_id: Optional[str]
    """The ID of one of your accounting ledger classes.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000 (cents). For RTP, the maximum amount
    allowed by the network is $100,000.
    """

    charge_bearer: Optional[Literal["shared", "sender", "receiver"]]
    """The party that will pay the fees for the payment order.

    Only applies to wire payment orders. Can be one of shared, sender, or receiver,
    which correspond respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.
    """

    counterparty_id: Optional[str]
    """Required when receiving_account_id is passed the ID of an external account."""

    currency: Optional[Currency]
    """Defaults to the currency of the originating account."""

    description: Optional[str]
    """An optional description for internal use."""

    direction: Literal["credit", "debit"]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    effective_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date transactions are to be posted to the participants' account.

    Defaults to the current business day or the next business day if the current day
    is a bank holiday or weekend. Format: yyyy-mm-dd.
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """RFP payments require an expires_at. This value must be past the effective_date."""

    fallback_type: Literal["ach"]
    """
    A payment type to fallback to if the original type is not valid for the
    receiving account. Currently, this only supports falling back from RTP to ACH
    (type=rtp and fallback_type=ach)
    """

    foreign_exchange_contract: Optional[str]
    """
    If present, indicates a specific foreign exchange contract number that has been
    generated by your financial institution.
    """

    foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]]
    """
    Indicates the type of FX transfer to initiate, can be either
    `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
    currency matches the originating account currency.
    """

    line_items: Iterable[ResourcePaymentOrderUpdateRequestWithIDLineItem]
    """An array of line items that must sum up to the amount of the payment order."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    nsf_protected: bool
    """A boolean to determine if NSF Protection is enabled for this payment order.

    Note that this setting must also be turned on in your organization settings
    page.
    """

    originating_account_id: str
    """The ID of one of your organization's internal accounts."""

    originating_party_name: Optional[str]
    """
    If present, this will replace your default company name on receiver's bank
    statement. This field can only be used for ACH payments currently. For ACH, only
    the first 16 characters of this string will be used. Any additional characters
    will be truncated.
    """

    priority: Literal["high", "normal"]
    """Either `normal` or `high`.

    For ACH and EFT payments, `high` represents a same-day ACH or EFT transfer,
    respectively. For check payments, `high` can mean an overnight check rather than
    standard mail.
    """

    process_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """If present, Modern Treasury will not process the payment until after this time.

    If `process_after` is past the cutoff for `effective_date`, `process_after` will
    take precedence and `effective_date` will automatically update to reflect the
    earliest possible sending date after `process_after`. Format is ISO8601
    timestamp.
    """

    purpose: Optional[str]
    """
    For `wire`, this is usually the purpose which is transmitted via the
    "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
    this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
    CPA Code that will be attached to the payment.
    """

    receiving_account: ResourcePaymentOrderUpdateRequestWithIDReceivingAccount
    """Either `receiving_account` or `receiving_account_id` must be present.

    When using `receiving_account_id`, you may pass the id of an external account or
    an internal account.
    """

    receiving_account_id: str
    """Either `receiving_account` or `receiving_account_id` must be present.

    When using `receiving_account_id`, you may pass the id of an external account or
    an internal account.
    """

    remittance_information: Optional[str]
    """For `ach`, this field will be passed through on an addenda record.

    For `wire` payments the field will be passed through as the "Originator to
    Beneficiary Information", also known as OBI or Fedwire tag 6000.
    """

    send_remittance_advice: Optional[bool]
    """Send an email to the counterparty when the payment order is sent to the bank.

    If `null`, `send_remittance_advice` on the Counterparty is used.
    """

    statement_descriptor: Optional[str]
    """An optional descriptor which will appear in the receiver's statement.

    For `check` payments this field will be used as the memo line. For `ach` the
    maximum length is 10 characters. Note that for ACH payments, the name on your
    bank account will be included automatically by the bank, so you can use the
    characters for other useful information. For `eft` the maximum length is 15
    characters.
    """

    status: Literal[
        "approved",
        "cancelled",
        "completed",
        "denied",
        "failed",
        "needs_approval",
        "pending",
        "processing",
        "returned",
        "reversed",
        "sent",
    ]
    """To cancel a payment order, use `cancelled`.

    To redraft a returned payment order, use `approved`. To undo approval on a
    denied or approved payment order, use `needs_approval`.
    """

    subtype: Optional[PaymentOrderSubtype]
    """
    An additional layer of classification for the type of payment order you are
    doing. This field is only used for `ach` payment orders currently. For `ach`
    payment orders, the `subtype` represents the SEC code. We currently support
    `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.
    """

    type: PaymentOrderType
    """
    One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
    `bacs`, `au_becs`, `interac`, `neft`, `nics`, `nz_national_clearing_code`,
    `sic`, `signet`, `provexchange`, `zengin`.
    """

    ultimate_originating_party_identifier: Optional[str]
    """
    This represents the identifier by which the person is known to the receiver when
    using the CIE subtype for ACH payments. Only the first 22 characters of this
    string will be used. Any additional characters will be truncated.
    """

    ultimate_originating_party_name: Optional[str]
    """
    This represents the name of the person that the payment is on behalf of when
    using the CIE subtype for ACH payments. Only the first 15 characters of this
    string will be used. Any additional characters will be truncated.
    """

    ultimate_receiving_party_identifier: Optional[str]
    """
    This represents the name of the merchant that the payment is being sent to when
    using the CIE subtype for ACH payments. Only the first 22 characters of this
    string will be used. Any additional characters will be truncated.
    """

    ultimate_receiving_party_name: Optional[str]
    """
    This represents the identifier by which the merchant is known to the person
    initiating an ACH payment with CIE subtype. Only the first 15 characters of this
    string will be used. Any additional characters will be truncated.
    """


ResourcesPaymentOrderUpdateRequestWithID = ResourcePaymentOrderUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourcePaymentOrderUpdateRequestWithID instead.
"""


class ResourceExpectedPaymentUpdateRequestWithID(TypedDict, total=False):
    id: str

    amount_lower_bound: int
    """The lowest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    amount_upper_bound: int
    """The highest amount this expected payment may be equal to.

    Value in specified currency's smallest unit. e.g. $10 would be represented
    as 1000.
    """

    counterparty_id: Optional[str]
    """The ID of the counterparty you expect for this payment."""

    currency: Optional[Currency]
    """Must conform to ISO 4217. Defaults to the currency of the internal account."""

    date_lower_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The earliest date the payment may come in. Format: yyyy-mm-dd"""

    date_upper_bound: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """The latest date the payment may come in. Format: yyyy-mm-dd"""

    description: Optional[str]
    """An optional description for internal use."""

    direction: TransactionDirection
    """One of credit or debit.

    When you are receiving money, use credit. When you are being charged, use debit.
    """

    internal_account_id: str
    """The ID of the Internal Account for the expected payment."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    reconciliation_filters: Optional[object]
    """The reconciliation filters you have for this payment."""

    reconciliation_groups: Optional[object]
    """The reconciliation groups you have for this payment."""

    reconciliation_rule_variables: Optional[Iterable[object]]
    """An array of reconciliation rule variables for this payment."""

    remittance_information: Optional[str]
    """For `ach`, this field will be passed through on an addenda record.

    For `wire` payments the field will be passed through as the "Originator to
    Beneficiary Information", also known as OBI or Fedwire tag 6000.
    """

    statement_descriptor: Optional[str]
    """The statement description you expect to see on the transaction.

    For ACH payments, this will be the full line item passed from the bank. For wire
    payments, this will be the OBI field on the wire. For check payments, this will
    be the memo field.
    """

    type: Optional[ExpectedPaymentType]
    """
    One of: ach, au_becs, bacs, book, check, eft, interac, provxchange, rtp, sen,
    sepa, signet, wire.
    """


ResourcesExpectedPaymentUpdateRequestWithID = ResourceExpectedPaymentUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourceExpectedPaymentUpdateRequestWithID instead.
"""


class ResourceLedgerTransactionUpdateRequestWithIDLedgerEntry(TypedDict, total=False):
    amount: Required[int]
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000. Can be any integer up to 36 digits.
    """

    direction: Required[TransactionDirection]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    ledger_account_id: Required[str]
    """The ledger account that this ledger entry is associated with."""

    available_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s available balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    lock_version: Optional[int]
    """Lock version of the ledger account.

    This can be passed when creating a ledger transaction to only succeed if no
    ledger transactions have posted since the given version. See our post about
    Designing the Ledgers API with Optimistic Locking for more details.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    pending_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s pending balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    posted_balance_amount: Optional[Dict[str, int]]
    """
    Use `gt` (>), `gte` (>=), `lt` (<), `lte` (<=), or `eq` (=) to lock on the
    account’s posted balance. If any of these conditions would be false after the
    transaction is created, the entire call will fail with error code 422.
    """

    show_resulting_ledger_account_balances: Optional[bool]
    """
    If true, response will include the balance of the associated ledger account for
    the entry.
    """


ResourcesLedgerTransactionUpdateRequestWithIDLedgerEntries = ResourceLedgerTransactionUpdateRequestWithIDLedgerEntry
"""This type is deprecated and will be removed in a future release.

Please use ResourceLedgerTransactionUpdateRequestWithIDLedgerEntry instead.
"""


class ResourceLedgerTransactionUpdateRequestWithID(TypedDict, total=False):
    id: str

    description: Optional[str]
    """An optional description for internal use."""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The timestamp (ISO8601 format) at which the ledger transaction happened for
    reporting purposes.
    """

    ledger_entries: Iterable[ResourceLedgerTransactionUpdateRequestWithIDLedgerEntry]
    """An array of ledger entry objects."""

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    status: Literal["archived", "pending", "posted"]
    """To post a ledger transaction at creation, use `posted`."""


ResourcesLedgerTransactionUpdateRequestWithID = ResourceLedgerTransactionUpdateRequestWithID
"""This type is deprecated and will be removed in a future release.

Please use ResourceLedgerTransactionUpdateRequestWithID instead.
"""

Resource = Union[
    ResourcePaymentOrderAsyncCreateRequest,
    ResourceExpectedPaymentCreateRequest,
    ResourceLedgerTransactionCreateRequest,
    ResourcePaymentOrderUpdateRequestWithID,
    ResourceExpectedPaymentUpdateRequestWithID,
    ResourceLedgerTransactionUpdateRequestWithID,
]

Resources = Resource
"""This type is deprecated and will be removed in a future release.

Please use Resource instead.
"""
