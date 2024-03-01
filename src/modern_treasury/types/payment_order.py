# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .shared import Currency
from .._compat import PYDANTIC_V2
from .._models import BaseModel
from .virtual_account import VirtualAccount
from .internal_account import InternalAccount
from .payment_order_type import PaymentOrderType
from .payment_order_subtype import PaymentOrderSubtype

__all__ = [
    "PaymentOrder",
    "Accounting",
    "ForeignExchangeRate",
    "ReferenceNumbers",
    "ReferenceNumber",
    "UltimateOriginatingAccount",
]


class Accounting(BaseModel):
    account_id: Optional[str] = None
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    class_id: Optional[str] = None
    """The ID of one of the class objects in your accounting system.

    Class objects track segments of your business independent of client or project.
    Note that these will only be accessible if your accounting system has been
    connected.
    """


class ForeignExchangeRate(BaseModel):
    base_amount: int
    """
    Amount in the lowest denomination of the `base_currency` to convert, often
    called the "sell" amount.
    """

    base_currency: Optional[Currency] = None
    """Currency to convert, often called the "sell" currency."""

    exponent: int
    """The exponent component of the rate.

    The decimal is calculated as `value` / (10 ^ `exponent`).
    """

    rate_string: str
    """A string representation of the rate."""

    target_amount: int
    """
    Amount in the lowest denomination of the `target_currency`, often called the
    "buy" amount.
    """

    target_currency: Optional[Currency] = None
    """Currency to convert the `base_currency` to, often called the "buy" currency."""

    value: int
    """The whole number component of the rate.

    The decimal is calculated as `value` / (10 ^ `exponent`).
    """


class ReferenceNumber(BaseModel):
    id: str

    created_at: datetime

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    reference_number: str
    """The vendor reference number."""

    reference_number_type: Literal[
        "ach_original_trace_number",
        "ach_trace_number",
        "bankprov_payment_activity_date",
        "bankprov_payment_id",
        "bnk_dev_prenotification_id",
        "bnk_dev_transfer_id",
        "bofa_end_to_end_id",
        "bofa_transaction_id",
        "check_number",
        "column_fx_quote_id",
        "column_reversal_pair_transfer_id",
        "column_transfer_id",
        "cross_river_payment_id",
        "cross_river_service_message",
        "cross_river_transaction_id",
        "currencycloud_conversion_id",
        "currencycloud_payment_id",
        "dc_bank_transaction_id",
        "dwolla_transaction_id",
        "eft_trace_number",
        "evolve_transaction_id",
        "fedwire_imad",
        "fedwire_omad",
        "first_republic_internal_id",
        "goldman_sachs_collection_request_id",
        "goldman_sachs_end_to_end_id",
        "goldman_sachs_payment_request_id",
        "goldman_sachs_request_id",
        "goldman_sachs_unique_payment_id",
        "interac_message_id",
        "jpmc_ccn",
        "jpmc_clearing_system_reference",
        "jpmc_customer_reference_id",
        "jpmc_end_to_end_id",
        "jpmc_firm_root_id",
        "jpmc_p3_id",
        "jpmc_payment_batch_id",
        "jpmc_payment_information_id",
        "jpmc_payment_returned_datetime",
        "lob_check_id",
        "other",
        "partial_swift_mir",
        "pnc_clearing_reference",
        "pnc_instruction_id",
        "pnc_multipayment_id",
        "pnc_payment_trace_id",
        "rspec_vendor_payment_id",
        "rtp_instruction_id",
        "signet_api_reference_id",
        "signet_confirmation_id",
        "signet_request_id",
        "silvergate_payment_id",
        "svb_end_to_end_id",
        "svb_payment_id",
        "svb_transaction_cleared_for_sanctions_review",
        "svb_transaction_held_for_sanctions_review",
        "swift_mir",
        "swift_uetr",
        "umb_product_partner_account_number",
        "usbank_payment_id",
        "wells_fargo_payment_id",
        "wells_fargo_trace_number",
    ]
    """The type of the reference number. Referring to the vendor payment id."""

    updated_at: datetime


ReferenceNumbers = ReferenceNumber
"""This type is deprecated and will be removed in a future release.

Please use ReferenceNumber instead.
"""

UltimateOriginatingAccount = Union[VirtualAccount, InternalAccount, None]


class PaymentOrder(BaseModel):
    id: str

    accounting: Accounting

    accounting_category_id: Optional[str] = None
    """The ID of one of your accounting categories.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    accounting_ledger_class_id: Optional[str] = None
    """The ID of one of your accounting ledger classes.

    Note that these will only be accessible if your accounting system has been
    connected.
    """

    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000 (cents). For RTP, the maximum amount
    allowed by the network is $100,000.
    """

    charge_bearer: Optional[Literal["shared", "sender", "receiver"]] = None
    """The party that will pay the fees for the payment order.

    Only applies to wire payment orders. Can be one of shared, sender, or receiver,
    which correspond respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.
    """

    compliance_rule_metadata: Optional[Dict[str, object]] = None
    """Custom key-value pair for usage in compliance rules.

    Please contact support before making changes to this field.
    """

    counterparty_id: Optional[str] = None
    """
    If the payment order is tied to a specific Counterparty, their id will appear,
    otherwise `null`.
    """

    created_at: datetime

    currency: Optional[Currency] = None
    """Defaults to the currency of the originating account."""

    current_return: Optional["ReturnObject"] = None
    """
    If the payment order's status is `returned`, this will include the return
    object's data.
    """

    decision_id: Optional[str] = None
    """
    The ID of the compliance decision for the payment order, if transaction
    monitoring is enabled.
    """

    description: Optional[str] = None
    """An optional description for internal use."""

    direction: Literal["credit", "debit"]
    """One of `credit`, `debit`.

    Describes the direction money is flowing in the transaction. A `credit` moves
    money from your account to someone else's. A `debit` pulls money from someone
    else's account to your own. Note that wire, rtp, and check payments will always
    be `credit`.
    """

    effective_date: date
    """Date transactions are to be posted to the participants' account.

    Defaults to the current business day or the next business day if the current day
    is a bank holiday or weekend. Format: yyyy-mm-dd.
    """

    expires_at: Optional[datetime] = None
    """RFP payments require an expires_at. This value must be past the effective_date."""

    foreign_exchange_contract: Optional[str] = None
    """
    If present, indicates a specific foreign exchange contract number that has been
    generated by your financial institution.
    """

    foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] = None
    """
    Indicates the type of FX transfer to initiate, can be either
    `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
    currency matches the originating account currency.
    """

    foreign_exchange_rate: Optional[ForeignExchangeRate] = None
    """Associated serialized foreign exchange rate information."""

    ledger_transaction_id: Optional[str] = None
    """The ID of the ledger transaction linked to the payment order."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    metadata: Dict[str, str]
    """Additional data represented as key-value pairs.

    Both the key and value must be strings.
    """

    nsf_protected: bool
    """A boolean to determine if NSF Protection is enabled for this payment order.

    Note that this setting must also be turned on in your organization settings
    page.
    """

    object: str

    originating_account_id: str
    """The ID of one of your organization's internal accounts."""

    originating_party_name: Optional[str] = None
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

    process_after: Optional[datetime] = None
    """If present, Modern Treasury will not process the payment until after this time.

    If `process_after` is past the cutoff for `effective_date`, `process_after` will
    take precedence and `effective_date` will automatically update to reflect the
    earliest possible sending date after `process_after`. Format is ISO8601
    timestamp.
    """

    purpose: Optional[str] = None
    """
    For `wire`, this is usually the purpose which is transmitted via the
    "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
    this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
    CPA Code that will be attached to the payment.
    """

    receiving_account_id: str
    """The receiving account ID. Can be an `external_account` or `internal_account`."""

    receiving_account_type: Literal["internal_account", "external_account"]

    reference_numbers: List[ReferenceNumber]

    remittance_information: Optional[str] = None
    """For `ach`, this field will be passed through on an addenda record.

    For `wire` payments the field will be passed through as the "Originator to
    Beneficiary Information", also known as OBI or Fedwire tag 6000.
    """

    send_remittance_advice: Optional[bool] = None
    """Send an email to the counterparty when the payment order is sent to the bank.

    If `null`, `send_remittance_advice` on the Counterparty is used.
    """

    statement_descriptor: Optional[str] = None
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
    """The current status of the payment order."""

    subtype: Optional[PaymentOrderSubtype] = None
    """
    An additional layer of classification for the type of payment order you are
    doing. This field is only used for `ach` payment orders currently. For `ach`
    payment orders, the `subtype` represents the SEC code. We currently support
    `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.
    """

    transaction_ids: List[str]
    """The IDs of all the transactions associated to this payment order.

    Usually, you will only have a single transaction ID. However, if a payment order
    initially results in a Return, but gets redrafted and is later successfully
    completed, it can have many transactions.
    """

    transaction_monitoring_enabled: bool
    """
    A flag that determines whether a payment order should go through transaction
    monitoring.
    """

    type: PaymentOrderType
    """
    One of `ach`, `bankgirot`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`,
    `bacs`, `au_becs`, `interac`, `neft`, `nics`, `nz_national_clearing_code`,
    `sic`, `signet`, `provexchange`, `zengin`.
    """

    ultimate_originating_account: Optional[UltimateOriginatingAccount] = None
    """The account to which the originating of this payment should be attributed to.

    Can be a `virtual_account` or `internal_account`.
    """

    ultimate_originating_account_id: Optional[str] = None
    """The ultimate originating account ID.

    Can be a `virtual_account` or `internal_account`.
    """

    ultimate_originating_account_type: Optional[Literal["internal_account", "virtual_account"]] = None

    ultimate_originating_party_identifier: Optional[str] = None
    """Identifier of the ultimate originator of the payment order."""

    ultimate_originating_party_name: Optional[str] = None
    """Name of the ultimate originator of the payment order."""

    ultimate_receiving_party_identifier: Optional[str] = None

    ultimate_receiving_party_name: Optional[str] = None

    updated_at: datetime

    vendor_failure_reason: Optional[str] = None
    """This field will be populated if a vendor (e.g.

    Currencycloud) failure occurs. Logic shouldn't be built on its value as it is
    free-form.
    """


from .return_object import ReturnObject

if PYDANTIC_V2:
    PaymentOrder.model_rebuild()
    Accounting.model_rebuild()
    ForeignExchangeRate.model_rebuild()
    ReferenceNumber.model_rebuild()
else:
    PaymentOrder.update_forward_refs()  # type: ignore
    Accounting.update_forward_refs()  # type: ignore
    ForeignExchangeRate.update_forward_refs()  # type: ignore
    ReferenceNumber.update_forward_refs()  # type: ignore
