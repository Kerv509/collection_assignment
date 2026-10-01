def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

#student's name
student_name = input("Please enter student name: ")

#student"s grades
grade1 = int(input("please enter grade 1: "))
grade2 = int(input("please enter grade 2: "))
grade3 = int(input("Please enter grade 3: "))
grade4 = int(input("Please enter grade 4: "))
grade5 = int(input("Please enter grade 5: "))

#grade list
grades = [grade1, grade2, grade3, grade4, grade5]

#average
average = sum(grades) / len(grades)

#get letter grade
letter_grade = get_letter_grade(average)

#results
print(student_name)
print(f"average: {average:g}")
print("Letter grade: ")
print(letter_grade)