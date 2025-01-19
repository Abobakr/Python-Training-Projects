# Get the student's grade from the user
grade = float(input("Enter the student's grade (0-100): "))
# Check if the grade is within the valid range
if grade < 0 or grade > 100:
    print("Invalid grade, please enter a number between 0 and 100.")
# Check if the student has passed or failed
elif grade > 60:
    print("The student has passed.")
else:
    print("The student has failed.")
