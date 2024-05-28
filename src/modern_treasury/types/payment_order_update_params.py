# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import date, datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.currency import Currency
from .payment_order_type import PaymentOrderType
from .external_account_type import ExternalAccountType
from .payment_order_subtype import PaymentOrderSubtype
from .shared.transaction_direction import TransactionDirection

__all__ = [
    "PaymentOrderUpdateParams",
    "Accounting",
    "LineItems",
    "LineItem",
    "ReceivingAccount",
    "ReceivingAccountAccountDetails",
    "ReceivingAccountAccountDetail",
    "ReceivingAccountContactDetails",
    "ReceivingAccountContactDetail",
    "ReceivingAccountLedgerAccount",
    "ReceivingAccountPartyAddress",
    "ReceivingAccountRoutingDetails",
    "ReceivingAccountRoutingDetail",
]


class PaymentOrderUpdateParams(TypedDict, total=False):
    accounting: Accounting

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

    line_items: Iterable[LineItem]
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
    "InstrForDbtrAgt" field in the ISO20022 file. For `eft`, this field is the 3
    digit CPA Code that will be attached to the payment.
    """

    receiving_account: ReceivingAccount
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


class Accounting(TypedDict, total=False):
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


class LineItem(TypedDict, total=False):
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


LineItems = LineItem
"""This type is deprecated and will be removed in a future release.

Please use LineItem instead.
"""


class ReceivingAccountAccountDetail(TypedDict, total=False):
    account_number: Required[str]

    account_number_type: Literal["iban", "hk_number", "clabe", "nz_number", "wallet_address", "pan", "other"]


ReceivingAccountAccountDetails = ReceivingAccountAccountDetail
"""This type is deprecated and will be removed in a future release.

Please use ReceivingAccountAccountDetail instead.
"""


class ReceivingAccountContactDetail(TypedDict, total=False):
    contact_identifier: str

    contact_identifier_type: Literal["email", "phone_number", "website"]


ReceivingAccountContactDetails = ReceivingAccountContactDetail
"""This type is deprecated and will be removed in a future release.

Please use ReceivingAccountContactDetail instead.
"""


class ReceivingAccountLedgerAccount(TypedDict, total=False):
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

    ledgerable_type: Literal["counterparty", "external_account", "internal_account", "virtual_account"]
    """
    If the ledger account links to another object in Modern Treasury, the type will
    be populated here, otherwise null. The value is one of internal_account or
    external_account.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """


class ReceivingAccountPartyAddress(TypedDict, total=False):
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


class ReceivingAccountRoutingDetail(TypedDict, total=False):
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
            "za_national_clearing_code",
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
        "se_bankgirot",
        "sen",
        "sepa",
        "sg_giro",
        "sic",
        "signet",
        "sknbi",
        "wire",
        "zengin",
    ]


ReceivingAccountRoutingDetails = ReceivingAccountRoutingDetail
"""This type is deprecated and will be removed in a future release.

Please use ReceivingAccountRoutingDetail instead.
"""


class ReceivingAccount(TypedDict, total=False):
    account_details: Iterable[ReceivingAccountAccountDetail]

    account_type: ExternalAccountType
    """Can be `checking`, `savings` or `other`."""

    contact_details: Iterable[ReceivingAccountContactDetail]

    ledger_account: ReceivingAccountLedgerAccount
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

    party_address: ReceivingAccountPartyAddress
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

    routing_details: Iterable[ReceivingAccountRoutingDetail]
