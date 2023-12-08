# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .shared import TransactionDirection

__all__ = ["CounterpartyCollectAccountParams"]


class CounterpartyCollectAccountParams(TypedDict, total=False):
    direction: Required[TransactionDirection]
    """One of `credit` or `debit`.

    Use `credit` when you want to pay a counterparty. Use `debit` when you need to
    charge a counterparty. This field helps us send a more tailored email to your
    counterparties."
    """

    custom_redirect: str
    """The URL you want your customer to visit upon filling out the form.

    By default, they will be sent to a Modern Treasury landing page. This must be a
    valid HTTPS URL if set.
    """

    fields: List[
        Literal[
            "name",
            "nameOnAccount",
            "taxpayerIdentifier",
            "accountType",
            "accountNumber",
            "ibanNumber",
            "clabeNumber",
            "walletAddress",
            "panNumber",
            "routingNumber",
            "abaWireRoutingNumber",
            "swiftCode",
            "auBsb",
            "caCpa",
            "cnaps",
            "gbSortCode",
            "inIfsc",
            "myBranchCode",
            "brCodigo",
            "routingNumberType",
            "address",
            "jp_zengin_code",
            "se_bankgiro_clearing_code",
            "nz_national_clearing_code",
            "hk_interbank_clearing_code",
            "hu_interbank_clearing_code",
            "dk_interbank_clearing_code",
            "id_sknbi_code",
        ]
    ]
    """The list of fields you want on the form.

    This field is optional and if it is not set, will default to [\"nameOnAccount\",
    \"accountType\", \"accountNumber\", \"routingNumber\", \"address\"]. The full
    list of options is [\"name\", \"nameOnAccount\", \"taxpayerIdentifier\",
    \"accountType\", \"accountNumber\", \"routingNumber\", \"address\",
    \"ibanNumber\", \"swiftCode\"].
    """

    send_email: bool
    """
    By default, Modern Treasury will send an email to your counterparty that
    includes a link to the form they must fill out. However, if you would like to
    send the counterparty the link, you can set this parameter to `false`. The JSON
    body will include the link to the secure Modern Treasury form.
    """
