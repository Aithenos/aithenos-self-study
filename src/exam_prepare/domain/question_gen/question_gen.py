from infra.llm_service import OpenAISearchInput
from infra.llm_service import OpenAISearchService

from .prompts import SYSTEM_PROMPT
from .prompts import USER_PROMPT

from shared.base import BaseModel
from shared.base import BaseService

from shared.models import ExamType
from shared.models import LevelClass
from shared.models import SubjectTypeVi


class QuestionGenInput(BaseModel):
    content: str
    exam_type: ExamType
    number_multiplechoice: int
    number_essay: int
    subject: SubjectTypeVi
    level_class: LevelClass
    chapters: list[str]


class QuestionGenOutput(BaseModel):
    questions: dict


class QuestionGenService(BaseService):
    openai_search: OpenAISearchService

    def process(self, inputs: QuestionGenInput) -> QuestionGenOutput:
        questions = self._generate_questions(
            content=inputs.content,
            exam_type=inputs.exam_type,
            number_multiplechoice=inputs.number_multiplechoice,
            number_essay=inputs.number_essay,
            subject=inputs.subject,
            level_class=inputs.level_class,
            chapters=inputs.chapters,
        )
        return QuestionGenOutput(questions=questions)

    def _generate_questions(
        self,
        content: str,
        exam_type: ExamType,
        number_multiplechoice: int,
        number_essay: int,
        subject: SubjectTypeVi,
        level_class: LevelClass,
        chapters: list[str],
    ) -> dict:
        user_prompt = USER_PROMPT.format(
            content=content,
            exam_type=exam_type.value,
            number_multiplechoice=number_multiplechoice,
            number_essay=number_essay,
            subject=subject.value,
            level_class=level_class.value,
            chapter="\n".join(chapters) + "\n",
        )
        system_prompt = SYSTEM_PROMPT
        response = self.openai_search.process(
            inputs=OpenAISearchInput(
                user_prompt=user_prompt,
                system_prompt=system_prompt,
                json_mode=True,
            )
        )
        return response.response  # type: ignore
