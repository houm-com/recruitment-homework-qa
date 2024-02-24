from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from src.api.schemas.visits import (
    Visits,
    VisitsCreate,
    VisitsPartialUpdate,
    VisitsStatus,
    VisitsUpdate,
)
from src.api.service import VisitsService
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


def validate_resolution_comment_on_finish(visit_update: VisitsUpdate | VisitsPartialUpdate):
    if visit_update.status in [
        VisitsStatus.COMPLETED.value,
    ] and not visit_update.check_fields_being_updated(include={"status", "resolution_comment"}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="resolution_comment is required when status is COMPLETED",
        )


def validate_visit_is_editable(
    visit_update: VisitsUpdate | VisitsPartialUpdate,
    current_visit_state: Visits,
):
    current_status = current_visit_state.status
    target_status = visit_update.status
    allowed_statuses = [VisitsStatus.PENDING.value, VisitsStatus.IN_PROGRESS.value]
    if (
        current_status in allowed_statuses
        and (target_status is None or target_status in allowed_statuses)
        and not visit_update.check_fields_being_updated(include={"resolution_comment"})
    ):
        return
    if visit_update.check_fields_being_updated(include={"resolution_comment"}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="resolution_comment is not editable in current status",
        )
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Visit is not editable in current status",
    )


def validate_on_update(
    visit_update: VisitsUpdate | VisitsPartialUpdate,
    current_visit_state: Visits,
):
    validate_resolution_comment_on_finish(visit_update=visit_update)
    validate_visit_is_editable(visit_update=visit_update, current_visit_state=current_visit_state)


@router.put("/{visit_id}", response_model=Visits)
def update_visit(
    visit_id: int,
    visit_update: VisitsUpdate,
    session: Session = Depends(get_db_session),
):
    service = VisitsService(session=session)
    current_visit_state = service.get_visit(visit_id=visit_id)
    validate_on_update(visit_update=visit_update, current_visit_state=current_visit_state)
    service.update_visit(visit_id=visit_id, visit=visit_update)
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
