# Copyright 2023 Canonical
# See LICENSE file for licensing details.
"""This file defines the schema for the provider side of the smtp interface.

It exposes one interfaces.schema_base.DataBagSchema subclass called:
- ProviderSchema

Examples:
    ProviderSchema:
        unit: <empty>
        app: {"smtp":
                 {
                    "host": "example.smtp",
                    "port": "25",
                    "user": "example_user",
                    "password_id": "01548499c9233d4612352c989162d940f6a9e6f6d5cc058dfcf66f51575e09c2",
                    "auth_type": "plain",
                    "transport_security": "tls",
                    "domain": "domain",
                }
             }
"""
from enum import Enum
from interface_tester.schema_base import DataBagSchema
from pydantic import BaseModel, Field
from typing import Optional


class TransportSecurity(str, Enum):
    """Represent the transport security values.

    Attributes:
        NONE: none
        STARTTLS: starttls
        TLS: tls
    """

    NONE = "none"
    STARTTLS = "starttls"
    TLS = "tls"


class AuthType(str, Enum):
    """Represent the auth type values.

    Attributes:
        NONE: none
        NOT_PROVIDED: not_provided
        PLAIN: plain
    """

    NONE = "none"
    NOT_PROVIDED = "not_provided"
    PLAIN = "plain"

class SmtpProviderData(BaseModel):
    host: str = Field(
        ...,
        min_length=1,
        description="SMTP host.",
        title="Host",
        examples=["example.smtp"],
    )
    port: int = Field(None,
        ge=1,
        le=65536,
        description="SMTP port.",
        title="Port",
        examples=[25],
    )
    user: Optional[str] = Field(
        description="SMTP user.",
        title="User",
        examples=["some_user"],
    )
    password_id: Optional[str] = Field(
        description="Secret ID for the SMTP password.",
        title="Password ID",
        examples=["01548499c9233d4612352c989162d940f6a9e6f6d5cc058dfcf66f51575e09c2"],
    )
    auth_type: AuthType = Field(
        description="The type used to authenticate with the SMTP relay.",
        title="Auth type",
        examples=[AuthType.NONE],
    )
    transport_security: TransportSecurity = Field(
        description="The security protocol to use for the outgoing SMTP relay.",
        title="Transport security",
        examples=[TransportSecurity.NONE],
    )
    domain: Optional[str] = Field(
        description="The domain used by the sent emails from SMTP relay.",
        title="Domain",
        examples=["domain"],
    )


class ProviderSchema(DataBagSchema):
    """Provider schema for SMTP."""
    app: SmtpProviderData

class RequirerSchema(DataBagSchema):
    """Requirer schema for SMTP."""