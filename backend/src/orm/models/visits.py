"""Audit mixin to use in the models."""
from datetime import datetime

# This is since there is a bug in mypy with SQLAlchemy
# mypy: disable-error-code="assignment"
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import Mapped

from src.orm.config import Base
from src.orm.models.audit_mixin import AuditMixin


class Visits(Base, AuditMixin):
    """List model."""

    __tablename__ = "visits"

    id: Mapped[int] = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )
    address: Mapped[str] = Column(String, nullable=True)
    houmer_name: Mapped[str] = Column(String, nullable=True)
    visitor_name: Mapped[str] = Column(String, nullable=True)
    scheduled_at: Mapped[datetime] = Column(DateTime, nullable=True)
    status: Mapped[str] = Column(String, nullable=True)
    resolution_comment: Mapped[str] = Column(String, nullable=True)
