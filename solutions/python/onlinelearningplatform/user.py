from typing import List

from course import Course
from payment import Payment
from result import Result


class User:
    def __init__(self, user_id: str, name: str, email: str, password: str, type_: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.type = type_
        self.enrolled_courses: List[Course] = []
        self.payments: List[Payment] = []
        self.results: List[Result] = []

    def enroll_in_course(self, course: Course) -> None:
        self.enrolled_courses.append(course)
        course.add_student(self)

    def make_payment(self, payment: Payment) -> None:
        self.payments.append(payment)

    def add_result(self, result: Result) -> None:
        self.results.append(result)

    def get_user_id(self) -> str:
        return self.user_id

    def get_name(self) -> str:
        return self.name
