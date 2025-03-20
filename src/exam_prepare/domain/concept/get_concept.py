from __future__ import annotations

from typing import Tuple

from infra.llm_service import OpenAISearchInput
from infra.llm_service import OpenAISearchService
from shared.base import BaseModel
from shared.base import BaseService
from shared.logging import get_logger
from shared.models import Language
from shared.models import LevelClass
from shared.models import SubjectTypeVi

from .prompts import VI_SYSTEM_PROMPT
from .prompts import VI_USER_PROMPT

logger = get_logger(__name__)


class ContentSynthesizerInput(BaseModel):
    lst_chapters: list[str]
    subject: SubjectTypeVi
    level_class: LevelClass
    lang: Language


class ContentSynthesizerOutput(BaseModel):
    content: str


class ContentSynthesizerService(BaseService):
    llm_service: OpenAISearchService

    def process(self, inputs: ContentSynthesizerInput) -> ContentSynthesizerOutput:
        user_prompt, system_prompt = self._generate_content_prompt(
            subject=inputs.subject,
            lst_chapters=inputs.lst_chapters,
            level_class=inputs.level_class,
            lang=inputs.lang,
        )
        content = self._generate_content(
            user_prompt=user_prompt,
            system_prompt=system_prompt,
        )
        return ContentSynthesizerOutput(content=content)

    def _generate_content_prompt(
        self,
        subject: SubjectTypeVi,
        lst_chapters: list[str],
        level_class: LevelClass,
        lang: Language,
    ) -> Tuple[str, str]:
        user_prompt = VI_USER_PROMPT.format(
            subject=subject.value,
            level_class=level_class.value,
            lst_chapter='\n'.join(lst_chapters) + '\n',
            # Add newline character at the end of each chapter for better formatting in the output Markdown table.
        )
        system_prompt = VI_SYSTEM_PROMPT
        return user_prompt, system_prompt

    def _generate_content(self, user_prompt: str, system_prompt: str) -> str:
        inputs = OpenAISearchInput(
            user_prompt=user_prompt,
            system_prompt=system_prompt,
        )
        output = self.llm_service.process(inputs=inputs)
        return str(output.response)
