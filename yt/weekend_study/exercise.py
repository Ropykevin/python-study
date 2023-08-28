from utils import find_max
numbers = [10,50,6,2]
maximum=find_max(numbers)
print(maximum)
#list exercise
# write a program to find the largest number in a list 
numbers=[1,2,3,4,5,6,7,8,9]
maximum=numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
# list methods/functions 
# write a program to remove the duplicates in a list
numbers=[2,2,2,4,5,6,6]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# dictionaries excercise
# when a number is inputed it converts it to words
phone =input("phone: ")
digits_mapping = {
    "0":"zero,",
    "1":"one,",
    "2":"two,",
    "3":"three,",
    "4":"four,",
    "5":"five,",
    "6":"six,",
    "7":"seven,",
    "8":"eight,",
    "9":"nine,"
}
output =""
for character in phone:
    digits_mapping.get(character, "!")
    output+=digits_mapping.get(character, "!")
print(output)
#  dice exercise using random module
import random
class Dice():
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second
dice=Dice()
print(dice.roll())

