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
from .service_ref import ServiceRef
from .service_relationship import ServiceRelationship
from .service_specification_ref import ServiceSpecificationRef
from .service_state_type import ServiceStateType


class ServiceCreateAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceCreateAllOf - a model defined in OpenAPI

        category: The category of this ServiceCreateAllOf [Optional].
        description: The description of this ServiceCreateAllOf [Optional].
        mef_service_configuration: The mef_service_configuration of this ServiceCreateAllOf [Optional].
        note: The note of this ServiceCreateAllOf [Optional].
        place: The place of this ServiceCreateAllOf [Optional].
        related_party: The related_party of this ServiceCreateAllOf [Optional].
        service_relationship: The service_relationship of this ServiceCreateAllOf [Optional].
        service_specification: The service_specification of this ServiceCreateAllOf [Optional].
        service_type: The service_type of this ServiceCreateAllOf [Optional].
        state: The state of this ServiceCreateAllOf [Optional].
        supporting_resource: The supporting_resource of this ServiceCreateAllOf [Optional].
        supporting_service: The supporting_service of this ServiceCreateAllOf [Optional].
    """

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

ServiceCreateAllOf.update_forward_refs()
