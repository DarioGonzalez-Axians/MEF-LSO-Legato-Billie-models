# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class ServiceRefAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceRefAllOf - a model defined in OpenAPI

        type: The type of this ServiceRefAllOf [Optional].
    """

    type: Optional[str] = None

ServiceRefAllOf.update_forward_refs()
