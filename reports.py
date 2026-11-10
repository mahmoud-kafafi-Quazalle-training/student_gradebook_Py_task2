from collections import Counter


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


def print_class_summary(students):
    graded_students = [student for student in students.values() if student.grades]
    if not graded_students:
        print("No grades recorded for the class.")
        return

    averages = {student.student_id: student.get_average() for student in graded_students}
    class_average = sum(averages.values()) / len(averages)
    top_score = max(averages.values())
    top_students = [
        f"{student.name} ({student.student_id})"
        for student in graded_students
        if averages[student.student_id] == top_score
    ]
    distribution = Counter(letter_grade(average) for average in averages.values())

    print(f"\nClass average: {class_average:.1f}")
    print(f"Top student(s): {', '.join(top_students)} ({top_score:.1f})")
    print("Letter grades:")
    for letter in "ABCDF":
        print(f"  {letter}: {distribution[letter]}")

    scores_by_subject = {}
    for student in graded_students:
        for subject, score in student.grades:
            scores_by_subject.setdefault(subject.casefold(), (subject, []))[1].append(score)

    print("Subject averages:")
    for subject, scores in sorted(scores_by_subject.values(), key=lambda item: item[0].casefold()):
        print(f"  {subject}: {sum(scores) / len(scores):.1f}")
