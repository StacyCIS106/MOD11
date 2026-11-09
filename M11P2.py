student_name = input("Enter the student's last name: ")
exam_one = float(input("Enter the score for exam one: "))
exam_two = float(input("Enter the score for exam two: "))
exam_three = float(input("Enter the score for exam three: "))

def calculate_average(exam_one, exam_two, exam_three):
    global total
    sum = exam_one + exam_two + exam_three
    total = sum
    return total / 3

average_score = calculate_average(exam_one, exam_two, exam_three)
print("Student Name:", student_name)
print("Average Score:", average_score)
print("Total Score:", total)