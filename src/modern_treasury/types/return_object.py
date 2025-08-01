# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import builtins
from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.currency import Currency

__all__ = ["ReturnObject", "Corrections", "ReferenceNumbers", "ReferenceNumber"]


class Corrections(BaseModel):
    account_number: Optional[str] = None
    """
    The updated account number that should replace the one originally used on the
    outgoing payment.
    """

    company_id: Optional[str] = None
    """
    The updated company ID that should replace the one originally used on the
    outgoing payment.
    """

    company_name: Optional[str] = None
    """
    The updated company name that should replace the one originally used on the
    outgoing payment.
    """

    individual_identification_number: Optional[str] = None
    """
    The updated individual identification number that should replace the one
    originally used on the outgoing payment.
    """

    routing_number: Optional[str] = None
    """
    The updated routing number that should replace the one originally used on the
    outgoing payment.
    """

    transaction_code: Optional[str] = None
    """
    The updated account type code that should replace the one originally used on the
    outgoing payment.
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
        "brale_transfer_id",
        "bridge_destination_transaction_hash",
        "bridge_source_transaction_hash",
        "bridge_transfer_id",
        "check_number",
        "citibank_reference_number",
        "citibank_worldlink_clearing_system_reference_number",
        "column_fx_quote_id",
        "column_reversal_pair_transfer_id",
        "column_transfer_id",
        "cross_river_core_transaction_id",
        "cross_river_fed_batch_id",
        "cross_river_payment_id",
        "cross_river_service_message",
        "cross_river_transaction_id",
        "currencycloud_conversion_id",
        "currencycloud_payment_id",
        "dc_bank_transaction_id",
        "eft_trace_number",
        "evolve_core_batch",
        "evolve_core_file_key",
        "evolve_core_seq",
        "evolve_transaction_id",
        "fake_vendor_payment_id",
        "fedwire_imad",
        "fedwire_omad",
        "first_republic_internal_id",
        "goldman_sachs_collection_request_id",
        "goldman_sachs_end_to_end_id",
        "goldman_sachs_payment_request_id",
        "goldman_sachs_request_id",
        "goldman_sachs_unique_payment_id",
        "hifi_offramp_id",
        "hifi_transfer_id",
        "interac_message_id",
        "jpmc_ccn",
        "jpmc_clearing_system_reference",
        "jpmc_customer_reference_id",
        "jpmc_end_to_end_id",
        "jpmc_firm_root_id",
        "jpmc_fx_trn_id",
        "jpmc_p3_id",
        "jpmc_payment_batch_id",
        "jpmc_payment_information_id",
        "jpmc_payment_returned_datetime",
        "jpmc_transaction_reference_number",
        "lob_check_id",
        "other",
        "partial_swift_mir",
        "pnc_clearing_reference",
        "pnc_instruction_id",
        "pnc_multipayment_id",
        "pnc_payment_trace_id",
        "pnc_request_for_payment_id",
        "pnc_transaction_reference_number",
        "rbc_wire_reference_id",
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
        "usbank_payment_application_reference_id",
        "usbank_payment_id",
        "usbank_pending_rtp_payment_id",
        "usbank_posted_rtp_payment_id",
        "wells_fargo_end_to_end_id",
        "wells_fargo_payment_id",
        "wells_fargo_trace_number",
        "wells_fargo_uetr",
        "western_alliance_payment_id",
        "western_alliance_transaction_id",
        "western_alliance_wire_confirmation_number",
    ]
    """The type of the reference number. Referring to the vendor payment id."""

    updated_at: datetime


ReferenceNumbers = ReferenceNumber
"""This type is deprecated and will be removed in a future release.

Please use ReferenceNumber instead.
"""


class ReturnObject(BaseModel):
    id: str

    amount: int
    """Value in specified currency's smallest unit.

    e.g. $10 would be represented as 1000.
    """

    code: Optional[
        Literal[
            "901",
            "902",
            "903",
            "904",
            "905",
            "907",
            "908",
            "909",
            "910",
            "911",
            "912",
            "914",
            "C01",
            "C02",
            "C03",
            "C05",
            "C06",
            "C07",
            "C08",
            "C09",
            "C13",
            "C14",
            "R01",
            "R02",
            "R03",
            "R04",
            "R05",
            "R06",
            "R07",
            "R08",
            "R09",
            "R10",
            "R11",
            "R12",
            "R13",
            "R14",
            "R15",
            "R16",
            "R17",
            "R18",
            "R19",
            "R20",
            "R21",
            "R22",
            "R23",
            "R24",
            "R25",
            "R26",
            "R27",
            "R28",
            "R29",
            "R30",
            "R31",
            "R32",
            "R33",
            "R34",
            "R35",
            "R36",
            "R37",
            "R38",
            "R39",
            "R40",
            "R41",
            "R42",
            "R43",
            "R44",
            "R45",
            "R46",
            "R47",
            "R50",
            "R51",
            "R52",
            "R53",
            "R61",
            "R62",
            "R67",
            "R68",
            "R69",
            "R70",
            "R71",
            "R72",
            "R73",
            "R74",
            "R75",
            "R76",
            "R77",
            "R80",
            "R81",
            "R82",
            "R83",
            "R84",
            "R85",
            "currencycloud",
        ]
    ] = None
    """The return code. For ACH returns, this is the required ACH return code."""

    corrections: Optional[Corrections] = None
    """Only relevant for ACH NOC returns.

    This is an object containing all of the new and corrected information provided
    by the bank that was previously incorrect on the original outgoing payment.
    """

    created_at: datetime

    currency: Currency
    """Currency that this transaction is denominated in."""

    current_return: Optional["ReturnObject"] = None
    """
    If the return's status is `returned`, this will include the return object's data
    that is returning this return.
    """

    date_of_death: Optional[date] = None
    """
    If the return code is `R14` or `R15` this is the date the deceased counterparty
    passed away.
    """

    discarded_at: Optional[datetime] = None

    failure_reason: Optional[str] = None
    """
    If an originating return failed to be processed by the bank, a description of
    the failure reason will be available.
    """

    internal_account_id: Optional[str] = None
    """The ID of the relevant Internal Account."""

    ledger_transaction_id: Optional[str] = None
    """The ID of the ledger transaction linked to the return."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    reason: Optional[str] = None
    """
    Often the bank will provide an explanation for the return, which is a short
    human readable string.
    """

    reference_numbers: List[ReferenceNumber]
    """An array of Payment Reference objects."""

    returnable_id: Optional[str] = None
    """The ID of the object being returned or `null`."""

    returnable_type: Optional[
        Literal["incoming_payment_detail", "paper_item", "payment_order", "return", "reversal"]
    ] = None
    """The type of object being returned or `null`."""

    role: Literal["originating", "receiving"]
    """The role of the return, can be `originating` or `receiving`."""

    status: Literal["completed", "failed", "pending", "processing", "returned", "sent"]
    """The current status of the return."""

    transaction_id: Optional[str] = None
    """The ID of the relevant Transaction or `null`."""

    transaction_line_item_id: Optional[str] = None
    """The ID of the relevant Transaction Line Item or `null`."""

    type: Literal[
        "ach",
        "ach_noc",
        "au_becs",
        "bacs",
        "book",
        "check",
        "cross_border",
        "eft",
        "interac",
        "manual",
        "paper_item",
        "sepa",
        "wire",
    ]
    """The type of return.

    Can be one of: `ach`, `ach_noc`, `au_becs`, `bacs`, `eft`, `interac`, `manual`,
    `paper_item`, `wire`.
    """

    updated_at: datetime

    additional_information: Optional[str] = None
    """Some returns may include additional information from the bank.

    In these cases, this string will be present.
    """

    data: Optional[builtins.object] = None
    """The raw data from the return file that we get from the bank."""
