from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.api.schemas.visits import (
    Visits,
    VisitsCreate,
    VisitsPartialUpdate,
    VisitsStatus,
)
from src.api.service import VisitsService
from src.api.validations import validate_on_update
from src.orm.config import get_db_session

router = APIRouter(
    tags=["visits"],
    prefix="/visits",
)


@router.get("/status/options", response_model=list[str])
def get_visits_statuses():
    """Get all possible visit statuses."""
    return [status.value for status in VisitsStatus]


@router.post("/", response_model=Visits)
def create_visit(
    visit: VisitsCreate,
    response: Response,
    session: Session = Depends(get_db_session),
):
    """Create a new visit."""
    service = VisitsService(session=session)
    visit = service.create_visit(visit=visit)
    response.status_code = status.HTTP_201_CREATED
    return visit


@router.get("/", response_model=list[Visits])
def get_visits(session: Session = Depends(get_db_session)):
    """Get all lists."""
    service = VisitsService(session=session)
    return service.get_visits()


@router.get("/{visit_id}", response_model=Visits)
def get_visit(visit_id: int, session: Session = Depends(get_db_session)):
    """Get a list by its id."""
    service = VisitsService(session=session)
    return service.get_visit(visit_id=visit_id)


@router.patch("/{visit_id}", response_model=Visits)
def partial_update_visit(
    visit_id: int,
    visit_update: VisitsPartialUpdate,
    session: Session = Depends(get_db_session),
):
    service = VisitsService(session=session)
    current_visit_state = service.get_visit(visit_id=visit_id)
    validate_on_update(visit_update=visit_update, current_visit_state=current_visit_state)
    service.partial_update_visit(visit_id=visit_id, visit=visit_update)
    return service.get_visit(visit_id=visit_id)


@router.delete("/{visit_id}")
def delete_visit(visit_id: int, response: Response, session: Session = Depends(get_db_session)):
    """Delete a list."""
    service = VisitsService(session=session)
    service.delete_visit(visit_id=visit_id)
    response.status_code = status.HTTP_204_NO_CONTENT
