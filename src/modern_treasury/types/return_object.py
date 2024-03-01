# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .shared import Currency
from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["ReturnObject", "ReferenceNumbers", "ReferenceNumber"]


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
            "R14",
            "R15",
            "R16",
            "R17",
            "R20",
            "R21",
            "R22",
            "R23",
            "R24",
            "R29",
            "R31",
            "R33",
            "R37",
            "R38",
            "R39",
            "R51",
            "R52",
            "R53",
            "currencycloud",
        ]
    ] = None
    """The return code. For ACH returns, this is the required ACH return code."""

    created_at: datetime

    currency: Optional[Currency] = None
    """Currency that this transaction is denominated in."""

    current_return: Optional[ReturnObject] = None
    """
    If the return's status is `returned`, this will include the return object's data
    that is returning this return.
    """

    date_of_death: Optional[date] = None
    """
    If the return code is `R14` or `R15` this is the date the deceased counterparty
    passed away.
    """

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


if PYDANTIC_V2:
    ReturnObject.model_rebuild()
    ReferenceNumber.model_rebuild()
else:
    ReturnObject.update_forward_refs()  # type: ignore
    ReferenceNumber.update_forward_refs()  # type: ignore
