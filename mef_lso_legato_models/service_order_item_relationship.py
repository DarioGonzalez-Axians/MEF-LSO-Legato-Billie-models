# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from .order_item_relationship_type import OrderItemRelationshipType
from .service_order_item_ref import ServiceOrderItemRef


class ServiceOrderItemRelationship(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceOrderItemRelationship - a model defined in OpenAPI

        relationship_type: The relationship_type of this ServiceOrderItemRelationship.
        service_order: The service_order of this ServiceOrderItemRelationship.
    """

    relationship_type: OrderItemRelationshipType
    service_order: ServiceOrderItemRef

ServiceOrderItemRelationship.update_forward_refs()
