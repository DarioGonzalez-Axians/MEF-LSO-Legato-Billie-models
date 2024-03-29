# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from .referenceable import Referenceable
from .service_order_ref_all_of import ServiceOrderRefAllOf


class ServiceOrderRef(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceOrderRef - a model defined in OpenAPI

        type: The type of this ServiceOrderRef.
        base_type: The base_type of this ServiceOrderRef [Optional].
        schema_location: The schema_location of this ServiceOrderRef [Optional].
        id: The id of this ServiceOrderRef.
        href: The href of this ServiceOrderRef [Optional].
        name: The name of this ServiceOrderRef [Optional].
        referred_type: The referred_type of this ServiceOrderRef.
    """

    type: str
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    id: str
    href: Optional[AnyUrl] = None
    name: Optional[str] = None
    referred_type: str

ServiceOrderRef.update_forward_refs()
