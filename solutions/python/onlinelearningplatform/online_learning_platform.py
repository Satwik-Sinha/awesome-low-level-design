from datetime import datetime

from user import User
from course import Course
from payment import Payment
from quiz import Quiz
from result import Result


def main() -> None:
    user1 = User("U1", "Alice", "alice@example.com", "password123", "student")
    course1 = Course("C1", "Java Programming", "Programming", "Learn Java from scratch")

    user1.enroll_in_course(course1)

    payment1 = Payment("P1", user1.get_user_id(), 99.99, "Credit Card", datetime.now())
    user1.make_payment(payment1)

    quiz1 = Quiz("Q1", course1.get_course_id(), "Java Basics", "Basic Java quiz", 50)
    course1.add_quiz(quiz1)

    result1 = Result("R1", user1.get_user_id(), course1.get_course_id(), quiz1.get_quiz_id(), 45)
    user1.add_result(result1)

    print(f"{user1.get_name()} has enrolled in {course1.get_name()}")


if __name__ == "__main__":
    main()
