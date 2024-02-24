from typing import Any

from pydantic import parse_obj_as

from src.api.exceptions import VisitDoesNotExistError
from src.api.schemas.visits import Visits, VisitsCreate, VisitsPartialUpdate, VisitsUpdate
from src.orm.models.visits import Visits as VisitsORM


class VisitsService:
    def __init__(self, session: Any):
        self.session = session

    def get_visit(self, visit_id: int) -> Visits:
        visit = self.session.query(VisitsORM).filter(VisitsORM.id == visit_id).first()
        if not visit:
            raise VisitDoesNotExistError
        return Visits.from_orm(visit)

    def get_visits(self) -> list[Visits]:
        visits = self.session.query(VisitsORM).all()
        return parse_obj_as(list[Visits], visits)

    def create_visit(self, visit: VisitsCreate) -> Visits:
        visit_orm = VisitsORM(**visit.dict())
        self.session.add(visit_orm)
        self.session.commit()
        self.session.refresh(visit_orm)
        return Visits.from_orm(visit_orm)

    def update_visit(self, visit_id: int, visit: VisitsUpdate) -> None:
        visit_data = visit.dict()
        self.session.query(VisitsORM).filter(VisitsORM.id == visit_id).update(visit_data)
        self.session.commit()

    def partial_update_visit(self, visit_id: int, visit: VisitsPartialUpdate) -> None:
        visit_data = visit.dict(exclude_unset=True)
        self.session.query(VisitsORM).filter(VisitsORM.id == visit_id).update(visit_data)
        self.session.commit()

    def delete_visit(self, visit_id: int) -> None:
        self.session.query(VisitsORM).filter(VisitsORM.id == visit_id).delete()
        self.session.commit()
