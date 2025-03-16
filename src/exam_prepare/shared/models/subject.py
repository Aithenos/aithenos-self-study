from __future__ import annotations
from enum import Enum


class Language(str, Enum):
    """
    Enum representing supported languages.
    """

    VI = "vi"  # Vietnamese
    EN = "en"  # English


class SubjectTypeVi(str, Enum):
    """
    Enum representing school subjects in Vietnamese.
    """

    TOAN = "Toán"
    VAN = "Ngữ Văn"  # Ngữ Văn
    ANH = "Tiếng Anh"  # Tiếng Anh
    LY = "Vật Lý"  # Vật Lý
    HOA = "Hóa Học"  # Hóa Học
    SINH = "Sinh Học"  # Sinh Học
    SU = "Lịch Sử"  # Lịch Sử
    DIA = "Địa Lý"  # Địa Lý
    GDCD = "Giáo Dục Công Dân"  # Giáo Dục Công Dân
    CNTT = "Công Nghệ Thông Tin"  # Công Nghệ Thông Tin
    THE_DUC = "Thể Dục"  # Thể Dục
    QUOC_PHONG = "Quốc Phòng"  # Quốc Phòng


class SubjectTypeEn(str, Enum):
    """
    Enum representing school subjects in English.
    """

    MATH = "math"  # Mathematics
    LITERATURE = "literature"  # Literature
    ENGLISH = "english"  # English
    PHYSICS = "physics"  # Physics
    CHEMISTRY = "chemistry"  # Chemistry
    BIOLOGY = "biology"  # Biology
    HISTORY = "history"  # History
    GEOGRAPHY = "geography"  # Geography
    CIVIC_EDUCATION = "civic_education"  # Civic Education
    IT = "it"  # Information Technology
    PHYSICAL_EDUCATION = "physical_education"  # Physical Education
    NATIONAL_DEFENSE = "national_defense"  # National Defense
