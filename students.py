class StudentNotFoundError(LookupError):
    """Raised when a student ID is missing from the gradebook."""


def get_student(students, student_id):
    try:
        return students[student_id]
    except KeyError:
        raise StudentNotFoundError(
            f"No student found with ID {student_id}."
        ) from None


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, subject, score):
        self.grades.append((subject, score))

    def get_average(self):
        if not self.grades:
            return 0
        return sum(score for _, score in self.grades) / len(self.grades)

    def __str__(self):
        return f"Student Name: {self.name}, ID: {self.student_id}"
