import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from students import Student

DATA_FILE = Path(__file__).resolve().parent / "data" / "gradebook.json"


def load_students(path=DATA_FILE):
    try:
        with path.open(encoding="utf-8") as data_file:
            records = json.load(data_file)
    except FileNotFoundError:
        return {}

    if not isinstance(records, list):
        raise TypeError("Expected a list of student records.")

    students = {}
    for record in records:
        if not isinstance(record, dict):
            raise TypeError("Invalid student record.")

        student_id = record.get("id")
        name = record.get("name")
        grades = record.get("grades")
        if (
            not isinstance(student_id, str)
            or not student_id.strip()
            or student_id in students
            or not isinstance(name, str)
            or not name.strip()
            or not isinstance(grades, list)
        ):
            raise ValueError("Invalid student record or duplicate ID.")

        student = Student(name=name, student_id=student_id)
        for grade in grades:
            if not isinstance(grade, list) or len(grade) != 2:
                raise ValueError(f"Invalid grade for student ID {student_id}.")
            subject, score = grade
            if (
                not isinstance(subject, str)
                or not subject.strip()
                or type(score) not in (int, float)
                or not 0 <= score <= 100
            ):
                raise ValueError(f"Invalid grade for student ID {student_id}.")
            student.add_grade(subject, score)
        students[student_id] = student

    return students


def save_students(students, path=DATA_FILE):
    records = [
        {
            "id": student.student_id,
            "name": student.name,
            "grades": student.grades,
        }
        for student in students.values()
    ]

    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=".gradebook-",
        suffix=".tmp",
        delete=False,
    ) as data_file:
        temporary_path = Path(data_file.name)
        try:
            json.dump(
                records, data_file, ensure_ascii=False,
                indent=2, allow_nan=False,
            )
            data_file.write("\n")
            data_file.close()
            temporary_path.replace(path)
        finally:
            temporary_path.unlink(missing_ok=True)
