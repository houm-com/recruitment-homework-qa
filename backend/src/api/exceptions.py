from fastapi import HTTPException
from fastapi import status as request_status


class VisitDoesNotExistError(Exception):
    ...


class VisitNotEditableError(HTTPException):
    def __init__(self, visit_id: int):
        super().__init__(
            status_code=request_status.HTTP_400_BAD_REQUEST,
            detail=f"Visit with id {visit_id} is not editable",
        )


class ResolutionCommentRequiredError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=request_status.HTTP_400_BAD_REQUEST,
            detail="resolution_comment is required to finish the visit",
        )


class ResolutionCommentNotEditableError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=request_status.HTTP_400_BAD_REQUEST,
            detail="resolution_comment is not editable in current status",
        )


class InvalidStatusTransition(HTTPException):
    def __init__(self, current_status: str, target_status: str):
        super().__init__(
            status_code=request_status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status transition from {current_status} to {target_status}",
        )


class FieldsNotEditableError(HTTPException):
    def __init__(self, fields: set[str]):
        super().__init__(
            status_code=request_status.HTTP_400_BAD_REQUEST,
            detail=f"{fields} are not editable in current status",
        )


class OnlyFieldsEditableInSpecificStatusError(HTTPException):
    def __init__(self, fields: set[str], status: str):
        super().__init__(
            status_code=request_status.HTTP_400_BAD_REQUEST,
            detail=(
                f"{fields} are the only editable fields when "
                f"transitioning to the {status} status"
            ),
        )


class InvalidStatusError(HTTPException):
    def __init__(self, status: str, available_statuses: list[str]):
        super().__init__(
            status_code=request_status.HTTP_400_BAD_REQUEST,
            detail=(f"{status} is not a valid status. Available statuses are {available_statuses}"),
        )
