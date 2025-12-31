import sys

print("=== Student Result Program ===")

if len(sys.argv) < 5:
    print("Usage: python student_g.py <name> <mark1> <mark2> <mark3>")
    sys.exit(1)

name = sys.argv[1]
marks = list(map(int, sys.argv[2:]))

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"Student Name: {name}")
print(f"Marks: {marks}")
print(f"Average: {average}")
print(f"Grade: {grade}")
