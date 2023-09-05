# Using Python or PHP or Java or Ruby or JavaScriptImplement
# a program that takes 3 form inputs
# or from the terminal,and stores them in three letiables. 
# Return the largest of the three.
# Do this without using the the inbuilt max () function!The goal of this exercise is to think
# about some internals that programs normally take care of for us. 
num1=int(input("enter number 1:  "))
num2=int(input("enter number 2:  "))
num3=int(input("enter number 3:  "))
def find_largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"{num1} is largest"
    elif num2 > num1 and num2 > num3:
        return f"{num2} is largest"
    else:
        return f"{num3} is largest"

result = find_largest(num1, num2, num3)
print(result)