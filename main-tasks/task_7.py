# /*Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. 
# The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  50 to 59, D - 40 to 49, E - less 40
# *
marks = int(input(f"Enter student marks {range(0,100)}: "))
grade=""
if (marks >= 70 and marks<=100) :
   grade= "Grade: A"
elif (marks >= 60 and marks<=79) :
   grade= "Grade: B"
elif (marks >= 50 and marks<=59):
   grade= "Grade: C"
elif (marks >=40 and marks<=49):
   grade= "Grade: D"
elif (marks >= 0 and marks<=40):
   grade= "Grade: E"
else :
   grade="invalid marks"
print(grade)
