# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from .extensible import Extensible
from .note_all_of import NoteAllOf


class Note(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Note - a model defined in OpenAPI

        type: The type of this Note.
        base_type: The base_type of this Note [Optional].
        schema_location: The schema_location of this Note [Optional].
        author: The author of this Note [Optional].
        date: The date of this Note [Optional].
        system: The system of this Note [Optional].
        text: The text of this Note [Optional].
    """

    type: str
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    author: Optional[str] = None
    date: Optional[datetime] = None
    system: Optional[str] = None
    text: Optional[str] = None

Note.update_forward_refs()
