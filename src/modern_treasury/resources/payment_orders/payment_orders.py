# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Mapping, Optional, cast
from typing_extensions import Literal

from ...types import (
    payment_order_create_params,
    payment_order_update_params,
    payment_order_create_async_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import extract_files, deepcopy_minimal
from .reversals import Reversals, AsyncReversals
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.payment_order import PaymentOrder

if TYPE_CHECKING:
    from ..._client import ModernTreasury, AsyncModernTreasury

__all__ = ["PaymentOrders", "AsyncPaymentOrders"]


class PaymentOrders(SyncAPIResource):
    reversals: Reversals

    def __init__(self, client: ModernTreasury) -> None:
        super().__init__(client)
        self.reversals = Reversals(client)

    def create(
        self,
        *,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ],
        subtype: Optional[Literal["CCD", "CIE", "CTX", "IAT", "PPD", "TEL", "WEB", "neft"]] | NotGiven = NOT_GIVEN,
        amount: int,
        direction: Literal["credit", "debit"],
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        originating_account_id: str,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        accounting: payment_order_create_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        expires_at: Optional[str] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_create_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        ledger_transaction: payment_order_create_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        line_items: List[payment_order_create_params.LineItems] | NotGiven = NOT_GIVEN,
        transaction_monitoring_enabled: bool | NotGiven = NOT_GIVEN,
        documents: List[payment_order_create_params.Documents] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PaymentOrder:
        """
        Create a new Payment Order

        Args:
          type: One of `ach`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`, `bacs`,
              `au_becs`, `interac`, `signet`, `provexchange`.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          originating_account_id: The ID of one of your organization's internal accounts.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          currency: Defaults to the currency of the originating account.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          description: An optional description for internal use.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          ultimate_originating_party_name: Name of the ultimate originator of the payment order.

          ultimate_originating_party_identifier: Identifier of the ultimate originator of the payment order.

          ultimate_receiving_party_name: Name of the ultimate funds recipient.

          ultimate_receiving_party_identifier: Identifier of the ultimate funds recipient.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          ledger_transaction: Specifies a ledger transaction object that will be created with the payment
              order. If the ledger transaction cannot be created, then the payment order
              creation will fail. The resulting ledger transaction will mirror the status of
              the payment order.

          line_items: An array of line items that must sum up to the amount of the payment order.

          transaction_monitoring_enabled: A flag that determines whether a payment order should go through transaction
              monitoring.

          documents: An array of documents to be attached to the payment order. Note that if you
              attach documents, the request's content type must be `multipart/form-data`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        body = deepcopy_minimal(
            {
                "type": type,
                "subtype": subtype,
                "amount": amount,
                "direction": direction,
                "priority": priority,
                "originating_account_id": originating_account_id,
                "receiving_account_id": receiving_account_id,
                "accounting": accounting,
                "accounting_category_id": accounting_category_id,
                "accounting_ledger_class_id": accounting_ledger_class_id,
                "currency": currency,
                "effective_date": effective_date,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "remittance_information": remittance_information,
                "purpose": purpose,
                "metadata": metadata,
                "charge_bearer": charge_bearer,
                "foreign_exchange_indicator": foreign_exchange_indicator,
                "foreign_exchange_contract": foreign_exchange_contract,
                "nsf_protected": nsf_protected,
                "originating_party_name": originating_party_name,
                "ultimate_originating_party_name": ultimate_originating_party_name,
                "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                "ultimate_receiving_party_name": ultimate_receiving_party_name,
                "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                "send_remittance_advice": send_remittance_advice,
                "expires_at": expires_at,
                "fallback_type": fallback_type,
                "receiving_account": receiving_account,
                "ledger_transaction": ledger_transaction,
                "line_items": line_items,
                "transaction_monitoring_enabled": transaction_monitoring_enabled,
                "documents": documents,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["documents", "<array>", "file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return self._post(
            "/api/payment_orders",
            body=body,
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PaymentOrder,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PaymentOrder:
        """Get details on a single payment order"""
        return self._get(
            f"/api/payment_orders/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PaymentOrder,
        )

    def update(
        self,
        id: str,
        *,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
        | NotGiven = NOT_GIVEN,
        subtype: Optional[Literal["CCD", "CIE", "CTX", "IAT", "PPD", "TEL", "WEB", "neft"]] | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        accounting: payment_order_update_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        expires_at: Optional[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_update_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        line_items: List[payment_order_update_params.LineItems] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PaymentOrder:
        """
        Update a payment order

        Args:
          type: One of `ach`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`, `bacs`,
              `au_becs`, `interac`, `signet`, `provexchange`.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          originating_account_id: The ID of one of your organization's internal accounts.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          currency: Defaults to the currency of the originating account.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          description: An optional description for internal use.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          ultimate_originating_party_name: This represents the name of the person that the payment is on behalf of when
              using the CIE subtype for ACH payments. Only the first 15 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_originating_party_identifier: This represents the identifier by which the person is known to the receiver when
              using the CIE subtype for ACH payments. Only the first 22 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_receiving_party_name: This represents the identifier by which the merchant is known to the person
              initiating an ACH payment with CIE subtype. Only the first 15 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_receiving_party_identifier: This represents the name of the merchant that the payment is being sent to when
              using the CIE subtype for ACH payments. Only the first 22 characters of this
              string will be used. Any additional characters will be truncated.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          status: To cancel a payment order, use `cancelled`. To redraft a returned payment order,
              use `approved`. To undo approval on a denied or approved payment order, use
              `needs_approval`.

          counterparty_id: Required when receiving_account_id is passed the ID of an external account.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          line_items: An array of line items that must sum up to the amount of the payment order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/api/payment_orders/{id}",
            body={
                "type": type,
                "subtype": subtype,
                "amount": amount,
                "direction": direction,
                "priority": priority,
                "originating_account_id": originating_account_id,
                "receiving_account_id": receiving_account_id,
                "accounting": accounting,
                "accounting_category_id": accounting_category_id,
                "accounting_ledger_class_id": accounting_ledger_class_id,
                "currency": currency,
                "effective_date": effective_date,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "remittance_information": remittance_information,
                "purpose": purpose,
                "metadata": metadata,
                "charge_bearer": charge_bearer,
                "foreign_exchange_indicator": foreign_exchange_indicator,
                "foreign_exchange_contract": foreign_exchange_contract,
                "nsf_protected": nsf_protected,
                "originating_party_name": originating_party_name,
                "ultimate_originating_party_name": ultimate_originating_party_name,
                "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                "ultimate_receiving_party_name": ultimate_receiving_party_name,
                "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                "send_remittance_advice": send_remittance_advice,
                "expires_at": expires_at,
                "status": status,
                "counterparty_id": counterparty_id,
                "fallback_type": fallback_type,
                "receiving_account": receiving_account,
                "line_items": line_items,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PaymentOrder,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
        | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        reference_number: str | NotGiven = NOT_GIVEN,
        effective_date_start: str | NotGiven = NOT_GIVEN,
        effective_date_end: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[PaymentOrder]:
        """Get a list of all payment orders

        Args:
          priority: Either `normal` or `high`.

        For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          transaction_id: The ID of a transaction that the payment order has been reconciled to.

          reference_number: Query for records with the provided reference number

          effective_date_start: An inclusive lower bound for searching effective_date

          effective_date_end: An inclusive upper bound for searching effective_date

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/payment_orders",
            page=SyncPage[PaymentOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "type": type,
                    "priority": priority,
                    "counterparty_id": counterparty_id,
                    "originating_account_id": originating_account_id,
                    "transaction_id": transaction_id,
                    "status": status,
                    "direction": direction,
                    "reference_number": reference_number,
                    "effective_date_start": effective_date_start,
                    "effective_date_end": effective_date_end,
                    "metadata": metadata,
                },
            ),
            model=PaymentOrder,
        )

    def create_async(
        self,
        *,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ],
        subtype: Optional[Literal["CCD", "CIE", "CTX", "IAT", "PPD", "TEL", "WEB", "neft"]] | NotGiven = NOT_GIVEN,
        amount: int,
        direction: Literal["credit", "debit"],
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        originating_account_id: str,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        accounting: payment_order_create_async_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        expires_at: Optional[str] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_create_async_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        ledger_transaction: payment_order_create_async_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        line_items: List[payment_order_create_async_params.LineItems] | NotGiven = NOT_GIVEN,
        transaction_monitoring_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Create a new payment order asynchronously

        Args:
          type: One of `ach`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`, `bacs`,
              `au_becs`, `interac`, `signet`, `provexchange`.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          originating_account_id: The ID of one of your organization's internal accounts.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          currency: Defaults to the currency of the originating account.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          description: An optional description for internal use.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          ultimate_originating_party_name: Name of the ultimate originator of the payment order.

          ultimate_originating_party_identifier: Identifier of the ultimate originator of the payment order.

          ultimate_receiving_party_name: Name of the ultimate funds recipient.

          ultimate_receiving_party_identifier: Identifier of the ultimate funds recipient.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          ledger_transaction: Specifies a ledger transaction object that will be created with the payment
              order. If the ledger transaction cannot be created, then the payment order
              creation will fail. The resulting ledger transaction will mirror the status of
              the payment order.

          line_items: An array of line items that must sum up to the amount of the payment order.

          transaction_monitoring_enabled: A flag that determines whether a payment order should go through transaction
              monitoring.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/api/payment_orders/create_async",
            body={
                "type": type,
                "subtype": subtype,
                "amount": amount,
                "direction": direction,
                "priority": priority,
                "originating_account_id": originating_account_id,
                "receiving_account_id": receiving_account_id,
                "accounting": accounting,
                "accounting_category_id": accounting_category_id,
                "accounting_ledger_class_id": accounting_ledger_class_id,
                "currency": currency,
                "effective_date": effective_date,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "remittance_information": remittance_information,
                "purpose": purpose,
                "metadata": metadata,
                "charge_bearer": charge_bearer,
                "foreign_exchange_indicator": foreign_exchange_indicator,
                "foreign_exchange_contract": foreign_exchange_contract,
                "nsf_protected": nsf_protected,
                "originating_party_name": originating_party_name,
                "ultimate_originating_party_name": ultimate_originating_party_name,
                "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                "ultimate_receiving_party_name": ultimate_receiving_party_name,
                "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                "send_remittance_advice": send_remittance_advice,
                "expires_at": expires_at,
                "fallback_type": fallback_type,
                "receiving_account": receiving_account,
                "ledger_transaction": ledger_transaction,
                "line_items": line_items,
                "transaction_monitoring_enabled": transaction_monitoring_enabled,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )


class AsyncPaymentOrders(AsyncAPIResource):
    reversals: AsyncReversals

    def __init__(self, client: AsyncModernTreasury) -> None:
        super().__init__(client)
        self.reversals = AsyncReversals(client)

    async def create(
        self,
        *,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ],
        subtype: Optional[Literal["CCD", "CIE", "CTX", "IAT", "PPD", "TEL", "WEB", "neft"]] | NotGiven = NOT_GIVEN,
        amount: int,
        direction: Literal["credit", "debit"],
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        originating_account_id: str,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        accounting: payment_order_create_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        expires_at: Optional[str] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_create_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        ledger_transaction: payment_order_create_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        line_items: List[payment_order_create_params.LineItems] | NotGiven = NOT_GIVEN,
        transaction_monitoring_enabled: bool | NotGiven = NOT_GIVEN,
        documents: List[payment_order_create_params.Documents] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PaymentOrder:
        """
        Create a new Payment Order

        Args:
          type: One of `ach`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`, `bacs`,
              `au_becs`, `interac`, `signet`, `provexchange`.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          originating_account_id: The ID of one of your organization's internal accounts.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          currency: Defaults to the currency of the originating account.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          description: An optional description for internal use.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          ultimate_originating_party_name: Name of the ultimate originator of the payment order.

          ultimate_originating_party_identifier: Identifier of the ultimate originator of the payment order.

          ultimate_receiving_party_name: Name of the ultimate funds recipient.

          ultimate_receiving_party_identifier: Identifier of the ultimate funds recipient.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          ledger_transaction: Specifies a ledger transaction object that will be created with the payment
              order. If the ledger transaction cannot be created, then the payment order
              creation will fail. The resulting ledger transaction will mirror the status of
              the payment order.

          line_items: An array of line items that must sum up to the amount of the payment order.

          transaction_monitoring_enabled: A flag that determines whether a payment order should go through transaction
              monitoring.

          documents: An array of documents to be attached to the payment order. Note that if you
              attach documents, the request's content type must be `multipart/form-data`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        body = deepcopy_minimal(
            {
                "type": type,
                "subtype": subtype,
                "amount": amount,
                "direction": direction,
                "priority": priority,
                "originating_account_id": originating_account_id,
                "receiving_account_id": receiving_account_id,
                "accounting": accounting,
                "accounting_category_id": accounting_category_id,
                "accounting_ledger_class_id": accounting_ledger_class_id,
                "currency": currency,
                "effective_date": effective_date,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "remittance_information": remittance_information,
                "purpose": purpose,
                "metadata": metadata,
                "charge_bearer": charge_bearer,
                "foreign_exchange_indicator": foreign_exchange_indicator,
                "foreign_exchange_contract": foreign_exchange_contract,
                "nsf_protected": nsf_protected,
                "originating_party_name": originating_party_name,
                "ultimate_originating_party_name": ultimate_originating_party_name,
                "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                "ultimate_receiving_party_name": ultimate_receiving_party_name,
                "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                "send_remittance_advice": send_remittance_advice,
                "expires_at": expires_at,
                "fallback_type": fallback_type,
                "receiving_account": receiving_account,
                "ledger_transaction": ledger_transaction,
                "line_items": line_items,
                "transaction_monitoring_enabled": transaction_monitoring_enabled,
                "documents": documents,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["documents", "<array>", "file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}

        return await self._post(
            "/api/payment_orders",
            body=body,
            files=files,
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PaymentOrder,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PaymentOrder:
        """Get details on a single payment order"""
        return await self._get(
            f"/api/payment_orders/{id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PaymentOrder,
        )

    async def update(
        self,
        id: str,
        *,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
        | NotGiven = NOT_GIVEN,
        subtype: Optional[Literal["CCD", "CIE", "CTX", "IAT", "PPD", "TEL", "WEB", "neft"]] | NotGiven = NOT_GIVEN,
        amount: int | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        accounting: payment_order_update_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        expires_at: Optional[str] | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        counterparty_id: Optional[str] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_update_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        line_items: List[payment_order_update_params.LineItems] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> PaymentOrder:
        """
        Update a payment order

        Args:
          type: One of `ach`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`, `bacs`,
              `au_becs`, `interac`, `signet`, `provexchange`.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          originating_account_id: The ID of one of your organization's internal accounts.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          currency: Defaults to the currency of the originating account.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          description: An optional description for internal use.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          ultimate_originating_party_name: This represents the name of the person that the payment is on behalf of when
              using the CIE subtype for ACH payments. Only the first 15 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_originating_party_identifier: This represents the identifier by which the person is known to the receiver when
              using the CIE subtype for ACH payments. Only the first 22 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_receiving_party_name: This represents the identifier by which the merchant is known to the person
              initiating an ACH payment with CIE subtype. Only the first 15 characters of this
              string will be used. Any additional characters will be truncated.

          ultimate_receiving_party_identifier: This represents the name of the merchant that the payment is being sent to when
              using the CIE subtype for ACH payments. Only the first 22 characters of this
              string will be used. Any additional characters will be truncated.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          status: To cancel a payment order, use `cancelled`. To redraft a returned payment order,
              use `approved`. To undo approval on a denied or approved payment order, use
              `needs_approval`.

          counterparty_id: Required when receiving_account_id is passed the ID of an external account.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          line_items: An array of line items that must sum up to the amount of the payment order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/api/payment_orders/{id}",
            body={
                "type": type,
                "subtype": subtype,
                "amount": amount,
                "direction": direction,
                "priority": priority,
                "originating_account_id": originating_account_id,
                "receiving_account_id": receiving_account_id,
                "accounting": accounting,
                "accounting_category_id": accounting_category_id,
                "accounting_ledger_class_id": accounting_ledger_class_id,
                "currency": currency,
                "effective_date": effective_date,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "remittance_information": remittance_information,
                "purpose": purpose,
                "metadata": metadata,
                "charge_bearer": charge_bearer,
                "foreign_exchange_indicator": foreign_exchange_indicator,
                "foreign_exchange_contract": foreign_exchange_contract,
                "nsf_protected": nsf_protected,
                "originating_party_name": originating_party_name,
                "ultimate_originating_party_name": ultimate_originating_party_name,
                "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                "ultimate_receiving_party_name": ultimate_receiving_party_name,
                "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                "send_remittance_advice": send_remittance_advice,
                "expires_at": expires_at,
                "status": status,
                "counterparty_id": counterparty_id,
                "fallback_type": fallback_type,
                "receiving_account": receiving_account,
                "line_items": line_items,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=PaymentOrder,
        )

    def list(
        self,
        *,
        after_cursor: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ]
        | NotGiven = NOT_GIVEN,
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        counterparty_id: str | NotGiven = NOT_GIVEN,
        originating_account_id: str | NotGiven = NOT_GIVEN,
        transaction_id: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        direction: Literal["credit", "debit"] | NotGiven = NOT_GIVEN,
        reference_number: str | NotGiven = NOT_GIVEN,
        effective_date_start: str | NotGiven = NOT_GIVEN,
        effective_date_end: str | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[PaymentOrder, AsyncPage[PaymentOrder]]:
        """Get a list of all payment orders

        Args:
          priority: Either `normal` or `high`.

        For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          transaction_id: The ID of a transaction that the payment order has been reconciled to.

          reference_number: Query for records with the provided reference number

          effective_date_start: An inclusive lower bound for searching effective_date

          effective_date_end: An inclusive upper bound for searching effective_date

          metadata: For example, if you want to query for records with metadata key `Type` and value
              `Loan`, the query would be `metadata%5BType%5D=Loan`. This encodes the query
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/api/payment_orders",
            page=AsyncPage[PaymentOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "after_cursor": after_cursor,
                    "per_page": per_page,
                    "type": type,
                    "priority": priority,
                    "counterparty_id": counterparty_id,
                    "originating_account_id": originating_account_id,
                    "transaction_id": transaction_id,
                    "status": status,
                    "direction": direction,
                    "reference_number": reference_number,
                    "effective_date_start": effective_date_start,
                    "effective_date_end": effective_date_end,
                    "metadata": metadata,
                },
            ),
            model=PaymentOrder,
        )

    async def create_async(
        self,
        *,
        type: Literal[
            "ach",
            "au_becs",
            "bacs",
            "book",
            "card",
            "check",
            "cross_border",
            "eft",
            "interac",
            "provxchange",
            "rtp",
            "sen",
            "sepa",
            "signet",
            "wire",
        ],
        subtype: Optional[Literal["CCD", "CIE", "CTX", "IAT", "PPD", "TEL", "WEB", "neft"]] | NotGiven = NOT_GIVEN,
        amount: int,
        direction: Literal["credit", "debit"],
        priority: Literal["high", "normal"] | NotGiven = NOT_GIVEN,
        originating_account_id: str,
        receiving_account_id: str | NotGiven = NOT_GIVEN,
        accounting: payment_order_create_async_params.Accounting | NotGiven = NOT_GIVEN,
        accounting_category_id: Optional[str] | NotGiven = NOT_GIVEN,
        accounting_ledger_class_id: Optional[str] | NotGiven = NOT_GIVEN,
        currency: Optional[
            Literal[
                "AED",
                "AFN",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "AUD",
                "AWG",
                "AZN",
                "BAM",
                "BBD",
                "BCH",
                "BDT",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BRL",
                "BSD",
                "BTC",
                "BTN",
                "BWP",
                "BYN",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNH",
                "CNY",
                "COP",
                "CRC",
                "CUC",
                "CUP",
                "CVE",
                "CZK",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ETB",
                "EUR",
                "FJD",
                "FKP",
                "GBP",
                "GBX",
                "GEL",
                "GGP",
                "GHS",
                "GIP",
                "GMD",
                "GNF",
                "GTQ",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "ILS",
                "IMP",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "JEP",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGA",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MRU",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MYR",
                "MZN",
                "NAD",
                "NGN",
                "NIO",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PYG",
                "QAR",
                "RON",
                "RSD",
                "RUB",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDG",
                "SEK",
                "SGD",
                "SHP",
                "SKK",
                "SLL",
                "SOS",
                "SRD",
                "SSP",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJS",
                "TMM",
                "TMT",
                "TND",
                "TOP",
                "TRY",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEF",
                "VES",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XAG",
                "XAU",
                "XBA",
                "XBB",
                "XBC",
                "XBD",
                "XCD",
                "XDR",
                "XFU",
                "XOF",
                "XPD",
                "XPF",
                "XPT",
                "XTS",
                "YER",
                "ZAR",
                "ZMK",
                "ZMW",
                "ZWD",
                "ZWL",
                "ZWN",
                "ZWR",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        effective_date: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        statement_descriptor: Optional[str] | NotGiven = NOT_GIVEN,
        remittance_information: Optional[str] | NotGiven = NOT_GIVEN,
        purpose: Optional[str] | NotGiven = NOT_GIVEN,
        metadata: Dict[str, str] | NotGiven = NOT_GIVEN,
        charge_bearer: Optional[Literal["shared", "sender", "receiver"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_indicator: Optional[Literal["fixed_to_variable", "variable_to_fixed"]] | NotGiven = NOT_GIVEN,
        foreign_exchange_contract: Optional[str] | NotGiven = NOT_GIVEN,
        nsf_protected: bool | NotGiven = NOT_GIVEN,
        originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_originating_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_name: Optional[str] | NotGiven = NOT_GIVEN,
        ultimate_receiving_party_identifier: Optional[str] | NotGiven = NOT_GIVEN,
        send_remittance_advice: Optional[bool] | NotGiven = NOT_GIVEN,
        expires_at: Optional[str] | NotGiven = NOT_GIVEN,
        fallback_type: Literal["ach"] | NotGiven = NOT_GIVEN,
        receiving_account: payment_order_create_async_params.ReceivingAccount | NotGiven = NOT_GIVEN,
        ledger_transaction: payment_order_create_async_params.LedgerTransaction | NotGiven = NOT_GIVEN,
        line_items: List[payment_order_create_async_params.LineItems] | NotGiven = NOT_GIVEN,
        transaction_monitoring_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Create a new payment order asynchronously

        Args:
          type: One of `ach`, `eft`, `wire`, `check`, `sen`, `book`, `rtp`, `sepa`, `bacs`,
              `au_becs`, `interac`, `signet`, `provexchange`.

          subtype: An additional layer of classification for the type of payment order you are
              doing. This field is only used for `ach` payment orders currently. For `ach`
              payment orders, the `subtype` represents the SEC code. We currently support
              `CCD`, `PPD`, `IAT`, `CTX`, `WEB`, `CIE`, and `TEL`.

          amount: Value in specified currency's smallest unit. e.g. $10 would be represented as
              1000 (cents). For RTP, the maximum amount allowed by the network is $100,000.

          direction: One of `credit`, `debit`. Describes the direction money is flowing in the
              transaction. A `credit` moves money from your account to someone else's. A
              `debit` pulls money from someone else's account to your own. Note that wire,
              rtp, and check payments will always be `credit`.

          priority: Either `normal` or `high`. For ACH and EFT payments, `high` represents a
              same-day ACH or EFT transfer, respectively. For check payments, `high` can mean
              an overnight check rather than standard mail.

          originating_account_id: The ID of one of your organization's internal accounts.

          receiving_account_id: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          accounting_category_id: The ID of one of your accounting categories. Note that these will only be
              accessible if your accounting system has been connected.

          accounting_ledger_class_id: The ID of one of your accounting ledger classes. Note that these will only be
              accessible if your accounting system has been connected.

          currency: Defaults to the currency of the originating account.

          effective_date: Date transactions are to be posted to the participants' account. Defaults to the
              current business day or the next business day if the current day is a bank
              holiday or weekend. Format: yyyy-mm-dd.

          description: An optional description for internal use.

          statement_descriptor: An optional descriptor which will appear in the receiver's statement. For
              `check` payments this field will be used as the memo line. For `ach` the maximum
              length is 10 characters. Note that for ACH payments, the name on your bank
              account will be included automatically by the bank, so you can use the
              characters for other useful information. For `eft` the maximum length is 15
              characters.

          remittance_information: For `ach`, this field will be passed through on an addenda record. For `wire`
              payments the field will be passed through as the "Originator to Beneficiary
              Information", also known as OBI or Fedwire tag 6000.

          purpose: For `wire`, this is usually the purpose which is transmitted via the
              "InstrForDbtrAgt" field in the ISO20022 file. If you are using Currencycloud,
              this is the `payment.purpose_code` field. For `eft`, this field is the 3 digit
              CPA Code that will be attached to the payment.

          metadata: Additional data represented as key-value pairs. Both the key and value must be
              strings.

          charge_bearer: The party that will pay the fees for the payment order. Only applies to wire
              payment orders. Can be one of shared, sender, or receiver, which correspond
              respectively with the SWIFT 71A values `SHA`, `OUR`, `BEN`.

          foreign_exchange_indicator: Indicates the type of FX transfer to initiate, can be either
              `variable_to_fixed`, `fixed_to_variable`, or `null` if the payment order
              currency matches the originating account currency.

          foreign_exchange_contract: If present, indicates a specific foreign exchange contract number that has been
              generated by your financial institution.

          nsf_protected: A boolean to determine if NSF Protection is enabled for this payment order. Note
              that this setting must also be turned on in your organization settings page.

          originating_party_name: If present, this will replace your default company name on receiver's bank
              statement. This field can only be used for ACH payments currently. For ACH, only
              the first 16 characters of this string will be used. Any additional characters
              will be truncated.

          ultimate_originating_party_name: Name of the ultimate originator of the payment order.

          ultimate_originating_party_identifier: Identifier of the ultimate originator of the payment order.

          ultimate_receiving_party_name: Name of the ultimate funds recipient.

          ultimate_receiving_party_identifier: Identifier of the ultimate funds recipient.

          send_remittance_advice: Send an email to the counterparty when the payment order is sent to the bank. If
              `null`, `send_remittance_advice` on the Counterparty is used.

          expires_at: RFP payments require an expires_at. This value must be past the effective_date.

          fallback_type: A payment type to fallback to if the original type is not valid for the
              receiving account. Currently, this only supports falling back from RTP to ACH
              (type=rtp and fallback_type=ach)

          receiving_account: Either `receiving_account` or `receiving_account_id` must be present. When using
              `receiving_account_id`, you may pass the id of an external account or an
              internal account.

          ledger_transaction: Specifies a ledger transaction object that will be created with the payment
              order. If the ledger transaction cannot be created, then the payment order
              creation will fail. The resulting ledger transaction will mirror the status of
              the payment order.

          line_items: An array of line items that must sum up to the amount of the payment order.

          transaction_monitoring_enabled: A flag that determines whether a payment order should go through transaction
              monitoring.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/api/payment_orders/create_async",
            body={
                "type": type,
                "subtype": subtype,
                "amount": amount,
                "direction": direction,
                "priority": priority,
                "originating_account_id": originating_account_id,
                "receiving_account_id": receiving_account_id,
                "accounting": accounting,
                "accounting_category_id": accounting_category_id,
                "accounting_ledger_class_id": accounting_ledger_class_id,
                "currency": currency,
                "effective_date": effective_date,
                "description": description,
                "statement_descriptor": statement_descriptor,
                "remittance_information": remittance_information,
                "purpose": purpose,
                "metadata": metadata,
                "charge_bearer": charge_bearer,
                "foreign_exchange_indicator": foreign_exchange_indicator,
                "foreign_exchange_contract": foreign_exchange_contract,
                "nsf_protected": nsf_protected,
                "originating_party_name": originating_party_name,
                "ultimate_originating_party_name": ultimate_originating_party_name,
                "ultimate_originating_party_identifier": ultimate_originating_party_identifier,
                "ultimate_receiving_party_name": ultimate_receiving_party_name,
                "ultimate_receiving_party_identifier": ultimate_receiving_party_identifier,
                "send_remittance_advice": send_remittance_advice,
                "expires_at": expires_at,
                "fallback_type": fallback_type,
                "receiving_account": receiving_account,
                "ledger_transaction": ledger_transaction,
                "line_items": line_items,
                "transaction_monitoring_enabled": transaction_monitoring_enabled,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )
