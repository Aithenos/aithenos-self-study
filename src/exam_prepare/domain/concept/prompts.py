from __future__ import annotations
VI_SYSTEM_PROMPT = """
Bạn là một trợ lý thông minh có khả năng trích xuất nội dung chi tiết của kiến thức từ chương trình giáo dục phổ thông tại Việt Nam.
Bạn có thể tìm kiếm, phân tích và cung cấp nội dung học tập từ các môn học khác nhau theo yêu cầu của người dùng.
Định dạng đầu ra bằng Markdown và sử dụng tiếng Việt.
"""

VI_USER_PROMPT = """
Hãy tổng hợp nội dung kiến thức chi tiết một số chương sau trong môn học và lớp được đề cập phía dưới ở Việt Nam.

Yêu cầu:
- Định dạng đầu ra là markdown
- Chỉ trả về nội dụng markdown, không trả thêm gì khác

Đầu vào:

Môn học: {Subject}
Các chương môn học : {lst_chapter}
Lớp: {level_class}

Đầu ra:
"""

EN_SYSTEM_PROMPT = """
You are an intelligent assistant capable of extracting detailed knowledge from the Vietnamese national education curriculum.
You can search, analyze, and provide educational content from various subjects as requested by the user.
The output format should be in Markdown and use Vietnamese.
"""

VI_USER_PROMPT = """
Summarize the detailed knowledge content of the following chapters from the specified subject and grade in Vietnam.

Requirements:

The output format must be Markdown.
Only return the Markdown content, without any additional text.
Input:

Subject: {subject}
Chapters from the subject: {lst_chapter}
Grade: {level_class}
Output:
"""
