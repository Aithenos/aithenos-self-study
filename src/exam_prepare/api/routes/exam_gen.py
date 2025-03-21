from __future__ import annotations

from api.helpers.exception_handler import ExceptionHandler
from api.helpers.exception_handler import ResponseMessage
from application import ExamGeneratorInput
from application import ExamGeneratorService
from shared.models import Language
from shared.models import ExamType
from shared.models import LevelClass
from shared.models import SubjectTypeVi
from fastapi import APIRouter
from fastapi import status
from shared.logging import get_logger

exam_gen = APIRouter(prefix="/v1")
logger = get_logger(__name__)


@exam_gen.post(
    "/prompting_exam_generator",
    response_model=dict,
    tags=["prompting_exam_generator"],
    responses={
        status.HTTP_200_OK: {
            "content": {},
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: ExceptionHandler.create_response_message(  # type: ignore
            ResponseMessage.INTERNAL_SERVER_ERROR,
        ),
        status.HTTP_400_BAD_REQUEST: ExceptionHandler.create_response_message(
            ResponseMessage.BAD_REQUEST,
        ),
        status.HTTP_401_UNAUTHORIZED: ExceptionHandler.create_response_message(
            ResponseMessage.INVALID_API_KEY,
        ),
        status.HTTP_402_PAYMENT_REQUIRED: ExceptionHandler.create_response_message(  # type: ignore
            ResponseMessage.UNPROCESSABLE_ENTITY,
        ),
    },
)
async def send_questions_answer(
    exam_type: ExamType,
    number_multiplechoice: int,
    number_essay: int,
    subject: SubjectTypeVi,
    level_class: LevelClass,
    chapters: str,
    lang: Language,
):
    exception_handler = ExceptionHandler(
        logger=logger.bind(),
        service_name="prompting_exam_generator",
    )

    try:
        docs_sync_process = ExamGeneratorService()
        response = docs_sync_process.process(
            inputs=ExamGeneratorInput(
                exam_type=exam_type,
                number_multiplechoice=number_multiplechoice,
                number_essay=number_essay,
                subject=subject,
                level_class=level_class,
                chapters=chapters.split(","),
                lang=lang,
            ),
        )
        return response.exam_question

    except Exception:
        return exception_handler.handle_exception(
            message=ResponseMessage.INTERNAL_SERVER_ERROR,
            extra={"Check input against": "Inputs"},
        )


@exam_gen.get("/healthz", tags=["exam_gen"])
async def healthz():
    return {"status": "ok"}
