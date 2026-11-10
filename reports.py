def letter_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def print_student_report(student):
    print(f"\nStudent report for {student.name} ({student.student_id})")
    if not student.grades:
        print("No grades recorded.")
        return

    subject_width = max(len("Subject"), *(len(subject) for subject, _ in student.grades))
    print(f"{'Subject':<{subject_width}}  {'Score':>5}")
    for subject, score in student.grades:
        print(f"{subject:<{subject_width}}  {score:>5.1f}")

    average = student.get_average()
    print(f"Average: {average:.1f}")
    print(f"Letter grade: {letter_grade(average)}")
