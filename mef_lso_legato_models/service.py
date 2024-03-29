# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from .mef_service_configuration import MefServiceConfiguration
from .note import Note
from .place import Place
from .related_party_ref import RelatedPartyRef
from .resource_ref import ResourceRef
from .service_all_of import ServiceAllOf
from .service_create import ServiceCreate
from .service_order_ref import ServiceOrderRef
from .service_ref import ServiceRef
from .service_relationship import ServiceRelationship
from .service_specification_ref import ServiceSpecificationRef
from .service_state_type import ServiceStateType


class Service(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Service - a model defined in OpenAPI

        type: The type of this Service.
        base_type: The base_type of this Service [Optional].
        schema_location: The schema_location of this Service [Optional].
        category: The category of this Service [Optional].
        description: The description of this Service [Optional].
        mef_service_configuration: The mef_service_configuration of this Service [Optional].
        note: The note of this Service [Optional].
        place: The place of this Service [Optional].
        related_party: The related_party of this Service [Optional].
        service_relationship: The service_relationship of this Service [Optional].
        service_specification: The service_specification of this Service [Optional].
        service_type: The service_type of this Service [Optional].
        state: The state of this Service [Optional].
        supporting_resource: The supporting_resource of this Service [Optional].
        supporting_service: The supporting_service of this Service [Optional].
        end_date: The end_date of this Service [Optional].
        has_started: The has_started of this Service [Optional].
        is_service_enabled: The is_service_enabled of this Service [Optional].
        is_stateful: The is_stateful of this Service [Optional].
        service_date: The service_date of this Service [Optional].
        service_order: The service_order of this Service [Optional].
        start_date: The start_date of this Service [Optional].
        start_mode: The start_mode of this Service [Optional].
    """

    type: str
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    category: Optional[str] = None
    description: Optional[str] = None
    mef_service_configuration: Optional[MefServiceConfiguration] = None
    note: Optional[List[Note]] = None
    place: Optional[List[Place]] = None
    related_party: Optional[List[RelatedPartyRef]] = None
    service_relationship: Optional[List[ServiceRelationship]] = None
    service_specification: Optional[ServiceSpecificationRef] = None
    service_type: Optional[str] = None
    state: Optional[ServiceStateType] = None
    supporting_resource: Optional[List[ResourceRef]] = None
    supporting_service: Optional[List[ServiceRef]] = None
    end_date: Optional[datetime] = None
    has_started: Optional[bool] = None
    is_service_enabled: Optional[bool] = None
    is_stateful: Optional[bool] = None
    service_date: Optional[str] = None
    service_order: Optional[List[ServiceOrderRef]] = None
    start_date: Optional[datetime] = None
    start_mode: Optional[str] = None

Service.update_forward_refs()
