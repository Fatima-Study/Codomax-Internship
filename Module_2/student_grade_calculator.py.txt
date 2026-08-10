# Student Grade Calculator
# Codomax Digital Solutions Internship

print("================================")
print("     STUDENT GRADE CALCULATOR")
print("================================")

name = input("Enter student name: ")

english = float(input("Enter English marks: "))
mathematics = float(input("Enter Mathematics marks: "))
python_marks = float(input("Enter Python marks: "))
ai = float(input("Enter AI marks: "))
cybersecurity = float(input("Enter Cybersecurity marks: "))

total = english + mathematics + python_marks + ai + cybersecurity
percentage = (total / 500) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n================================")
print("          RESULT")
print("================================")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("================================")
