# /*Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. 
# The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  50 to 59, D - 40 to 49, E - less 40
# *
def student_marks():
    while True:
        try:
            marks = int(input("Enter student marks (0-100): "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks should be in the range 0-100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if 80 <= marks <= 100:
        grade = "Grade: A"
    elif 60 <= marks <= 79:
        grade = "Grade: B"
    elif 50 <= marks <= 59:
        grade = "Grade: C"
    elif 40 <= marks <= 49:
        grade = "Grade: D"
    else:
        grade = "Grade: E"

    return grade

Grade = student_marks()
print(Grade)
