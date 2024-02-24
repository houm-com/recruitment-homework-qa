"""Audit mixin to use in the models."""
from datetime import datetime

# This is since there is a bug in mypy with SQLAlchemy
# mypy: disable-error-code="assignment"
import pytz
from sqlalchemy import TIMESTAMP, Column
from sqlalchemy.orm import Mapped


class AuditMixin:
    """Audit mixin to use in the models."""

    created_at: Mapped[datetime] = Column(TIMESTAMP, default=lambda: datetime.now(tz=pytz.UTC))
    updated_at: Mapped[datetime] = Column(
        TIMESTAMP,
        default=lambda: datetime.now(tz=pytz.UTC),
        onupdate=lambda: datetime.now(tz=pytz.UTC),
    )
