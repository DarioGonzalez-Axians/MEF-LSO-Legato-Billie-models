# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from .action_type import ActionType
from .service_create import ServiceCreate
from .service_order_item_relationship import ServiceOrderItemRelationship
from .service_order_state_type import ServiceOrderStateType


class ServiceOrderItemAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceOrderItemAllOf - a model defined in OpenAPI

        id: The id of this ServiceOrderItemAllOf.
        action: The action of this ServiceOrderItemAllOf [Optional].
        service: The service of this ServiceOrderItemAllOf.
        state: The state of this ServiceOrderItemAllOf [Optional].
        order_item_relationship: The order_item_relationship of this ServiceOrderItemAllOf [Optional].
    """

    id: str
    action: Optional[ActionType] = None
    service: ServiceCreate
    state: Optional[ServiceOrderStateType] = None
    order_item_relationship: Optional[List[ServiceOrderItemRelationship]] = None

ServiceOrderItemAllOf.update_forward_refs()