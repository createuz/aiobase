from datetime import datetime
from typing import Any

from pydantic import BaseModel as _BaseModel
from pydantic import ConfigDict, PrivateAttr
from sqlalchemy import BigInteger, DateTime, Integer, SmallInteger, String
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.orm import DeclarativeBase, registry

from aiobase.utils.custom_types import DictStrAny, Int16, Int32, Int64


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            Int16: SmallInteger(),
            Int32: Integer(),
            Int64: BigInteger(),
            DictStrAny: JSON(),
            list[str]: ARRAY(String()),
            datetime: DateTime(timezone=True),
        }
    )


class PydanticModel(_BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        from_attributes=True,
        populate_by_name=True,
    )


class ActiveRecordModel(PydanticModel):
    __updated: dict[str, Any] = PrivateAttr(default_factory=dict)

    @property
    def model_state(self) -> dict[str, Any]:
        return self.__updated

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)
        self.__updated[name] = value
