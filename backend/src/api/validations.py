from src.api.exceptions import (
    InvalidStatusError,
    OnlyFieldsEditableInSpecificStatusError,
    ResolutionCommentNotEditableError,
    ResolutionCommentRequiredError,
    VisitNotEditableError,
)
from src.api.schemas.visits import (
    Visits,
    VisitsPartialUpdate,
    VisitsStatus,
    VisitsUpdate,
)


class UpdateValidator:
    def __init__(
        self,
        current_visit_state: Visits,
        target_state: VisitsUpdate | VisitsPartialUpdate,
    ):
        self.current_state = current_visit_state
        self.target_state = target_state

    def validate(self):
        self.target_state.status = self.target_state.status or self.current_state.status
        self._validate_status(self.target_state.status)
        if self.target_state.status == VisitsStatus.PENDING.value:
            return self.validate_pending()
        if self.target_state.status == VisitsStatus.IN_PROGRESS.value:
            return self.validate_in_progress()
        if self.target_state.status == VisitsStatus.COMPLETED.value:
            return self.validate_completed()
        if self.target_state.status == VisitsStatus.DELAYED.value:
            return self.validate_delayed()
        if self.target_state.status == VisitsStatus.CANCELED.value:
            return self.validate_canceled()
        raise NotImplementedError

    def validate_pending(self) -> None:
        self._validate_editable()
        if self.target_state.resolution_comment:
            raise ResolutionCommentNotEditableError
        self.target_state.resolution_comment = None

    def validate_in_progress(self) -> None:
        self._validate_editable()
        if self.target_state.resolution_comment:
            raise ResolutionCommentNotEditableError
        self.target_state.resolution_comment = None

    def validate_completed(self) -> None:
        editable_fields = {"status", "resolution_comment"}
        if not self.target_state.resolution_comment:
            raise ResolutionCommentRequiredError
        if not self.target_state.strict_check_fields_being_updated(include=editable_fields):
            raise OnlyFieldsEditableInSpecificStatusError(
                fields=editable_fields,
                status=VisitsStatus.COMPLETED.value,
            )

    def validate_delayed(self) -> None:
        self._validate_editable()
        if self.target_state.resolution_comment:
            raise ResolutionCommentNotEditableError
        self.target_state.resolution_comment = None

    def validate_canceled(self) -> None:
        editable_fields = {"status", "resolution_comment"}
        if not self.target_state.resolution_comment:
            raise ResolutionCommentRequiredError
        if not self.target_state.strict_check_fields_being_updated(include=editable_fields):
            raise OnlyFieldsEditableInSpecificStatusError(
                fields=editable_fields,
                status=VisitsStatus.CANCELED.value,
            )

    def _validate_editable(self) -> None:
        fully_enabled_edit_statuses = [
            VisitsStatus.PENDING.value,
            VisitsStatus.IN_PROGRESS.value,
            VisitsStatus.DELAYED.value,
        ]
        if self.target_state.status in fully_enabled_edit_statuses:
            return
        raise VisitNotEditableError(visit_id=self.current_state.id)

    def _validate_status(self, status: str) -> None:
        available_statuses = [member.value for member in VisitsStatus]

        if status not in available_statuses:
            raise InvalidStatusError(status=status, available_statuses=available_statuses)


def validate_on_update(
    visit_update: VisitsUpdate | VisitsPartialUpdate,
    current_visit_state: Visits,
):
    UpdateValidator(
        current_visit_state=current_visit_state,
        target_state=visit_update,
    ).validate()
