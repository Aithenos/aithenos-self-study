from __future__ import annotations

from enum import Enum


class ExamType(str, Enum):
    SHORT_TEST = "short_test"  # Meaning oral test
    TEST_15M = "test_15m"  # Meaning 15 minute test
    TEST_45M = "test_45m"  # Meaning 45 minute test
