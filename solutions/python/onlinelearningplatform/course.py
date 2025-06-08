from typing import List

from user import User
from course_content import CourseContent
from quiz import Quiz


class Course:
    def __init__(self, course_id: str, name: str, type_: str, description: str):
        self.course_id = course_id
        self.name = name
        self.type = type_
        self.description = description
        self.students: List[User] = []
        self.course_contents: List[CourseContent] = []
        self.quizzes: List[Quiz] = []

    def add_student(self, user: User) -> None:
        self.students.append(user)

    def add_content(self, content: CourseContent) -> None:
        self.course_contents.append(content)

    def add_quiz(self, quiz: Quiz) -> None:
        self.quizzes.append(quiz)

    def get_course_id(self) -> str:
        return self.course_id

    def get_name(self) -> str:
        return self.name
