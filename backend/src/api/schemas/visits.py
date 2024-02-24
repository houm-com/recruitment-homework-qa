from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class VisitsStatus(Enum):
    """Possible tatuses for the visits."""

    PENDING = "PENDING"
    DELAY = "DELAY"
    IN_PROGRESS = "IN_PROGRESS"
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

    def check_fields_being_updated(self, include: list[str]):
        """Check if all fields except the ones in exclude are being updated."""
        if not include:
            return all(self.dict().values())
        return all(self.dict(include=include).values())


class VisitsPartialUpdate(VisitsUpdate):
    created_at: datetime | None = None
    updated_at: datetime | None = None
    address: str | None = None
    houmer_name: str | None = None
    visitor_name: str | None = None
    scheduled_at: datetime | None = None
    status: str | None = None
    resolution_comment: str | None = None
