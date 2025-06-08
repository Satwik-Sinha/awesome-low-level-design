from datetime import datetime


class Enrollment:
    def __init__(self, enrollment_id: str, user_id: str, course_id: str, enrollment_date: datetime, completion_status: str):
        self.enrollment_id = enrollment_id
        self.user_id = user_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date
        self.completion_status = completion_status
