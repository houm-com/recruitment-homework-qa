from fastapi import HTTPException, status


class VisitDoesNotExistError(Exception):
    ...


class VisitNotEditableError(HTTPException):
    def __init__(self, visit_id: int):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Visit with id {visit_id} is not editable",
        )


class ResolutionCommentRequiredError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="resolution_comment is required to finish the visit",
        )


class ResolutionCommentNotEditableError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="resolution_comment is not editable in current status",
        )
