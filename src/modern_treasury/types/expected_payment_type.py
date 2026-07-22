# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from typing_extensions import Literal, TypeAliasType, TypeAlias

__all__ = ["ExpectedPaymentType"]

ExpectedPaymentType: TypeAlias = Optional[Literal["ach", "au_becs", "bacs", "book", "card", "chats", "check", "cross_border", "dk_nets", "eft", "gb_fps", "masav", "mx_ccen", "neft", "nics", "nz_becs", "pl_elixir", "rtp", "se_bankgirot", "sepa", "sg_giro", "sic", "stablecoin", "wire", "zengin"]]