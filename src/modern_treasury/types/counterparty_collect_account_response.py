# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["CounterpartyCollectAccountResponse"]


class CounterpartyCollectAccountResponse(BaseModel):
    id: str
    """The id of the existing counterparty."""

    form_link: str
    """This is the link to the secure Modern Treasury form.

    By default, Modern Treasury will send an email to your counterparty that
    includes a link to this form. However, if `send_email` is passed as `false` in
    the body then Modern Treasury will not send the email and you can send it to the
    counterparty directly.
    """

    is_resend: bool
    """
    This field will be `true` if an email requesting account details has already
    been sent to this counterparty.
    """
