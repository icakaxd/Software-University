def input_to_list(lines_count):
    return [input() for _ in range(int(lines_count))]


def count_students_marks(values):
    student_marks = {}

    for value in values:
        (student, mark) = value.split()
        if student not in student_marks:
            student_marks[student] = []
        student_marks[student].append(mark)

    return student_marks


def avrg(values):
    return sum(values) / len(values)


def print_result(values_marks):
    for (student, marks) in values_marks.items():
        avg = avrg([float(mark) for mark in marks])
        print(f'{student} -> {" ".join([f"{float(mark):.2f}" for mark in marks])} (avg: {avg:.2f})')


print_result(count_students_marks(input_to_list(input())))
