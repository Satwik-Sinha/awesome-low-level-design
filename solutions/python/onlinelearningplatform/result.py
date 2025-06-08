class Result:
    def __init__(self, result_id: str, user_id: str, course_id: str, quiz_id: str, score: int):
        self.result_id = result_id
        self.user_id = user_id
        self.course_id = course_id
        self.quiz_id = quiz_id
        self.score = score
