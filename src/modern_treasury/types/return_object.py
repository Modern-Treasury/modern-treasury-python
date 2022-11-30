# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..types import shared
from .._models import BaseModel

__all__ = ["ReferenceNumbers", "ReturnObject"]


class ReferenceNumbers(BaseModel):
    created_at: str

    id: str

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
        "bankprov_payment_id",
        "bnk_dev_prenotification_id",
        "bnk_dev_transfer_id",
        "bofa_end_to_end_id",
        "bofa_transaction_id",
        "check_number",
        "cross_river_payment_id",
        "cross_river_transaction_id",
        "currencycloud_conversion_id",
        "currencycloud_payment_id",
        "dc_bank_transaction_id",
        "dwolla_transaction_id",
        "eft_trace_number",
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
        "jpmc_end_to_end_id",
        "jpmc_firm_root_id",
        "jpmc_p3_id",
        "jpmc_payment_batch_id",
        "jpmc_payment_information_id",
        "lob_check_id",
        "other",
        "partial_swift_mir",
        "pnc_clearing_reference",
        "pnc_instruction_id",
        "pnc_multipayment_id",
        "pnc_payment_trace_id",
        "rtp_instruction_id",
        "signet_api_reference_id",
        "signet_confirmation_id",
        "signet_request_id",
        "silvergate_payment_id",
        "swift_mir",
        "swift_uetr",
        "usbank_payment_id",
        "wells_fargo_payment_id",
        "wells_fargo_trace_number",
    ]
    """The type of the reference number. Referring to the vendor payment id."""

    updated_at: str


class ReturnObject(BaseModel):
    additional_information: Optional[str]
    """Some returns may include additional information from the bank.

    In these cases, this string will be present.
    """

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
    ]
    """The return code. For ACH returns, this is the required ACH return code."""

    created_at: str

    currency: Optional[shared.Currency]
    """Currency that this transaction is denominated in."""

    date_of_death: Optional[str]
    """
    If the return code is `R14` or `R15` this is the date the deceased counterparty
    passed away.
    """

    failure_reason: Optional[str]
    """
    If an originating return failed to be processed by the bank, a description of
    the failure reason will be available.
    """

    id: str

    internal_account_id: Optional[str]
    """The ID of the relevant Internal Account."""

    ledger_transaction_id: Optional[str]
    """The ID of the ledger transaction linked to the return."""

    live_mode: bool
    """
    This field will be true if this object exists in the live environment or false
    if it exists in the test environment.
    """

    object: str

    reason: Optional[str]
    """
    Often the bank will provide an explanation for the return, which is a short
    human readable string.
    """

    reference_numbers: List[ReferenceNumbers]
    """An array of Payment Reference objects."""

    returnable_id: Optional[str]
    """The ID of the object being returned or `null`."""

    returnable_type: Optional[Literal["incoming_payment_detail", "paper_item", "payment_order", "reversal"]]
    """The type of object being returned or `null`."""

    role: Literal["originating", "receiving"]
    """The role of the return, can be `originating` or `receiving`."""

    status: Literal["completed", "failed", "pending", "processing", "sent"]
    """The current status of the return."""

    transaction_id: Optional[str]
    """The ID of the relevant Transaction or `null`."""

    transaction_line_item_id: Optional[str]
    """The ID of the relevant Transaction Line Item or `null`."""

    type: Literal["ach", "ach_noc", "au_becs", "bacs", "eft", "interac", "manual", "paper_item", "sepa", "wire"]
    """The type of return.

    Can be one of: `ach`, `ach_noc`, `au_becs`, `bacs`, `eft`, `interac`, `manual`,
    `paper_item`, `wire`.
    """

    updated_at: str
