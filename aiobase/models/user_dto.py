from datetime import datetime
from typing import Optional


from aiobase.models.base import ActiveRecordModel
from aiobase.utils.custom_types import Int64


class UserDto(ActiveRecordModel):
    id: int
    user_id: Optional[Int64]
    username: Optional[str]
    first_name: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

