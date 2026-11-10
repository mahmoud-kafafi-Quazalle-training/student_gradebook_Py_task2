from students import Student


def main():
    students = {}

    while True:
        print("Welcome to the Student Gradebook!")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Please select an option: ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
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


if __name__ == "__main__":
    main()
