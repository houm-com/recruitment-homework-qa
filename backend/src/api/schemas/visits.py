from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class VisitsStatus(Enum):
    """Possible tatuses for the visits."""

    PENDING = "PENDING"
    DELAYED = "DELAYED"
    IN_PROGRESS = "IN_PROGRESS"
    CANCELED = "CANCELED"
    COMPLETED = "COMPLETED"


class VisitsBase(BaseModel):
    address: str
    houmer_name: str
    visitor_name: str
    scheduled_at: datetime
    status: str


class VisitsCreate(VisitsBase):
    address: str
    houmer_name: str | None = None
    visitor_name: str | None = None
    scheduled_at: datetime | None = None
    status: str | None = VisitsStatus.PENDING.value


class Visits(VisitsBase):
    created_at: datetime
    updated_at: datetime
    id: int
    address: str | None = None
    houmer_name: str | None = None
    visitor_name: str | None = None
    scheduled_at: datetime | None = None
    status: str | None = None
    resolution_comment: str | None = None

    class Config:
        orm_mode = True


class VisitsUpdate(BaseModel):
    address: str | None
    houmer_name: str | None
    visitor_name: str | None
    scheduled_at: datetime | None
    status: str | None
    resolution_comment: str | None

    def strict_check_fields_being_updated(
        self,
        include: list[str] = None,
        exclude: list[str] = None,
    ):
        """Check if all fields except the ones in exclude are being updated."""
        include = include or []
        exclude = exclude or []
        if include and exclude:
            msg = "Cannot use both include and exclude at the same time."
            raise ValueError(msg)
        if include:
            return all(self.dict(include=include).values()) and not any(
                self.dict(exclude=include).values(),
            )
        if exclude:
            return all(self.dict(exclude=exclude).values()) and not any(
                self.dict(include=exclude).values(),
            )
        return all(self.dict().values())


class VisitsPartialUpdate(VisitsUpdate):
    created_at: datetime | None = None
    updated_at: datetime | None = None
    address: str | None = None
    houmer_name: str | None = None
    visitor_name: str | None = None
    scheduled_at: datetime | None = None
    status: str | None = None
    resolution_comment: str | None = None
