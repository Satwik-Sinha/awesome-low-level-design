class Quiz:
    def __init__(self, quiz_id: str, course_id: str, name: str, description: str, marks: int):
        self.quiz_id = quiz_id
        self.course_id = course_id
        self.name = name
        self.description = description
        self.marks = marks

    def get_quiz_id(self) -> str:
        return self.quiz_id
