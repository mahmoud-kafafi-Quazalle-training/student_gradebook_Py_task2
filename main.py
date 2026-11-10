from reports import print_class_summary, print_student_report
from students import Student, StudentNotFoundError, get_student


def main():
    students = {}

    while True:
        print("Welcome to the Student Gradebook!")
        print("1. Add Student")
        print("2. View Students")
        print("3. Remove Student")
        print("5. Record Grade")
        print("6. Student Report")
        print("7. Class Summary")
        print("4. Exit")

        choice = input("Please select an option: ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            remove_student(students)
        elif choice == '5':
            record_grade(students)
        elif choice == '6':
            show_student_report(students)
        elif choice == '7':
            print_class_summary(students)
        elif choice == '4':
            print("Exiting the Gradebook. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


def add_student(students):
    student_id = input("Student ID: ").strip()
    name = input("Student name: ").strip()

    if not student_id or not name:
        print("Student ID and name are required.")
        return

    if student_id in students:
        print("A student with this ID already exists.")
        return

    students[student_id] = Student(name=name, student_id=student_id)
    print("Student added.")


def view_students(students):
    if not students:
        print("No students found.")
        return

    for student in students.values():
        print(student)


def remove_student(students):
    student_id = input("Student ID to remove: ").strip()

    if not student_id:
        print("Student ID is required.")
        return

    if student_id not in students:
        print("No student found with that ID.")
        return

    del students[student_id]
    print("Student removed.")


def record_grade(students):
    student_id = input("Student ID: ").strip()
    try:
        student = get_student(students, student_id)
    except StudentNotFoundError as error:
        print(error)
        return

    subject = input("Subject: ").strip()
    if not subject:
        print("Subject is required.")
        return

    try:
        score = float(input("Score (0 to 100): "))
    except ValueError:
        print("Enter a numeric score from 0 to 100.")
        return

    if not 0 <= score <= 100:
        print("Score must be between 0 and 100.")
        return

    student.add_grade(subject, score)
    print("Grade recorded.")


def show_student_report(students):
    student_id = input("Student ID: ").strip()
    try:
        student = get_student(students, student_id)
    except StudentNotFoundError as error:
        print(error)
        return

    print_student_report(student)


if __name__ == "__main__":
    main()
