from functools import cached_property

from shared.settings import load_settings
from shared.settings import Settings

from domain.question_gen import QuestionGenInput
from domain.question_gen import QuestionGenService

from domain.concept import ContentSynthesizerInput
from domain.concept import ContentSynthesizerService

from infra.llm_service import OpenAISearchService

from shared.base import BaseModel
from shared.base import BaseService
from shared.models import Language

from shared.models import ExamType
from shared.models import LevelClass
from shared.models import SubjectTypeVi


class ExamGeneratorInput(BaseModel):
    exam_type: ExamType
    number_multiplechoice: int
    number_essay: int
    subject: SubjectTypeVi
    level_class: LevelClass
    chapters: list[str]
    lang: Language


class ExamGeneratorOutput(BaseModel):
    exam_question: dict


class ExamGeneratorService(BaseService):
    @cached_property
    def settings(self) -> Settings:
        """
        Load settings configuration.

        Returns:
            Settings: The application settings.
        """
        return load_settings()

    @cached_property
    def openai_search(self) -> OpenAISearchService:
        """
        Create a OpenAISearchService instance.
        """
        return OpenAISearchService(settings=self.settings.openai)

    @cached_property
    def content_synthesizer(self) -> ContentSynthesizerService:
        """
        Create a ContentSynthesizerService instance.
        """

        return ContentSynthesizerService(llm_service=self.openai_search)

    @cached_property
    def question_gen(self) -> QuestionGenService:
        """
        Create a QuestionGenService instance.
        """
        return QuestionGenService(openai_search=self.openai_search)

    def process(self, inputs: ExamGeneratorInput) -> ExamGeneratorOutput:
        # Content
        content_synthesizer_input = ContentSynthesizerInput(
            subject=inputs.subject,
            lst_chapters=inputs.chapters,
            level_class=inputs.level_class,
            lang=inputs.lang,
        )
        content = self.content_synthesizer.process(content_synthesizer_input).content
        # Generate multiple-choice questions
        multiple_choice_questions = self.question_gen.process(
            QuestionGenInput(
                content=content,
                exam_type=inputs.exam_type,
                number_multiplechoice=inputs.number_multiplechoice,
                number_essay=inputs.number_essay,
                subject=inputs.subject,
                level_class=inputs.level_class,
                chapters=inputs.chapters,
            )
        )
        return ExamGeneratorOutput(exam_question=multiple_choice_questions.questions)
