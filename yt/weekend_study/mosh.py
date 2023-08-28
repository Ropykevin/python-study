#we check in a patient named john smith
# he is 20years old and is a new patient
# soluion
full_name="john smith"
age=20
is_new=True

# getting input
name=input('whats your name? ')
print("Hi "+ name)#Hi name

#ask two questions:1.persons name and favourite color.
#then print a message like"ropy likes blue
#solution
favourite_color=input('what is your favourite color? ')
print(name + " likes " + favourite_color)
#type conversion
# str to int(int())
# str to float(float())
#str to boolean(bool())

# question
# ask a user their weight(in pounds),convert it to kilograms
#and print on the terminal
# solution
weight_lbs=input('what is your weight(lbs)? ')
weight_kg = int(weight_lbs)*0.45
print(weight_kg)
# formated strings
# use of prefix "f" and calibraces for place holders{}
#operators question
x = (2+3)*10-3
print(x)
# built in function
# round() convetrs to the next int
#abs() returns positive representation

# use of math module
import math
x=2.9
print(math.ceil(x))#3 ceil shows the upper interger
print(math.ceil(x))#2 floor show the lower interger

# if statement
# question
#if its hot
#   it's  a hot day
#   Drink plenty of water
#otherwise if its a cold day 
#   it's a cold day 
#   wear warm clothes
#otherwise 
#   it's a lovely day
#  solution
is_hot=True
is_cold=False
if is_hot:
    print("it's a hot day")
    print("drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm cloths")
else:
    print("it's a lovely day")

# excersice on if statements
#price of a house is $1M
#if buyer has good credit 
#   they need to put down 10%
#otherwise
#   they need to put down 20%
#print the down payment
house_price=1000000
good_credit=True
if good_credit:
    down_payment= house_price*0.1
else :
    down_payment=house_price*0.2
print(f"down payment is ${round(down_payment)}")


# logical operators
#if loan aplicant has high income and good credit 
#   Eligible for loan
#solution
# and all =True
has_high_income =True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print('not Eligible')

#if loan aplicant has high income or good credit 
#   Eligible for loan
# solution
# or one to be true
has_high_income =False
has_good_credit = True
if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print('not Eligible')

# NOT inverts the condition
has_high_income =False
has_good_credit = True
if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print('not Eligible')

#if loan aplicant has high income , good credit  and doesn't have a cri,inal record
has_high_income =True
has_good_credit = True
criminal_record=False
if (has_high_income and has_good_credit) and not criminal_record:
    print("Eligible for loan")
else:
    print('not Eligible')

# comparison operator
# if temperature is greater than 30
#   its a hot day
#otherwise
#   its a cold day
# otherwise
#   it's neither hot nor cold
#solition
temperature =0
if temperature>30:
    print("it`s warm")
    print("Drink water")
elif temperature>20:
    print("its nice")
else:
    print("its cold")
print("Done")

# exercise
# if name is less than 3 characters long
#   name must be at least 3 characters
# otherwise if its more than 50 charcters long 
#   name can be a maximum of 50 characters
# otherwise
#   name looks good
# solution
full_name= input("whats your name? ")
if len(full_name) < 3:
    print("full name must be atleast 3 characters")
elif len(full_name) > 50:
    print("full name must be a maximum of 50 characters")
else :
    print("full name looks good!")

# Project weight converter
weight =int(input("weight: "))
unit = input('(L)bs or (K)g: ')
if unit.upper()=="L":
    converted = weight*0.45
    print(f"you are {converted}kilos")
else:
    converted=weight/0.45
    print(f"you are {converted} pounds")

# while loops
# while condition :
i=1
while i <=5:
    print(i)
    i = i+1
print("done")
# use  of asterics *
i=int(input("i: "))
while i <=5:
    print("*" * i)
    i = i + 1
print("done")

# guessing game
secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input("Guess: "))
    guess_count +=1
    if guess==secret_number:
        print("you won")
        break
else:
    print("sorry you failed")
    # car game
# car game
# help
# start
# stop
# quit
# "idon t understand that "
command=""
started=False
while True !="quit":
    command=input("> ").lower()
    if command=="start":
        if started:
            print(" car is already started")
        else:
            started=True
            print("car started...")
    elif command=="help":
        print("""
start-to start the car
stop-to stop the car
quit-to quit the game           
        """)
    elif command=="stop":
        if not started:
            print(" car already stopped")
        else:
            started=False
            print("car stopped.")
    elif command=="quit":
        print("quit successfuly")
        break
    else:
        print("I don't understand you")

# for loops
#items of a collection
#for item in 'python':
for item in range(100):
    print(item)
# prints numbers from 1 to 100 vertically

# exercise
prices=[10,20,30]
total=0
for price in prices:
    total+=price
print(f"Total: {total}")

# Nested loops(adding one loop to another)
# list of quardinates
# (x,y)
# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,0)
# (1,2)
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

# nested loop excecise
numbers=[5,2,5,2,2]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output+='x'
    print(output)

# lists
# use of index to access
# write a program to find the largest number in a list 
numbers=[1,2,3,4,5,6,7,8,9]
max=numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#2D list 
# 2 dimensional list
# a 2 dimensional list is where each item in that list is another list
matrix =[
     [1,2,3],
     [4,5,6],
     [7,8,9]
 ]
# to access
print(matrix[0][1])
# to modify
matrix[0][1]=20
print(matrix[0][1])

# using nested loops
for row in matrix:
    for item in row:
        print(item)

# list methods/functions 
# write a program to remove the duplicates in a list
numbers=[2,2,2,4,5,6,6]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# tuples
numbers=(1,2,3,)
# can notbe modified

# unparking
coordinates=(1,2,3)
x= coordinates[0]
y= coordinates[1]
z=coordinates[2]
#  using unparking
x,y,z =(coordinates)
# x=1
# y=2
# z=3
#unparking can also be used in lists
coordinates=[1,2,3]
x,y,z =[1,2,3]
# x=1
# y=2
# z=3

# dictionaries
# key value pairs
# name= "ropy kevin"
# email= "ropy kevin@gmail.com"
# phone = "0742670714"
#keys must be unique
# case sensitive
customer ={
    "name":"ropy kevin",
    "age":30,
    "is_verified":True
}
# we can access each item using []
customer[name]#"ropy kevin"
# use of get method displays none if the key is not defined
print(customer.get("birthdate","may 16 1999")) #jan 1 1990 because it is default since key birth date is not defined
# update value
customer["name"]= "kevin ropy"
print(customer)#name wi be updated to"kevin ropy"
# adding key values
customer["birth_date"]= "may 16 1999"
print(customer)#bith data with its value will have been added

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

# emoji converter with dictionaries
message = input(">")
words = message.split(" ")
emojis ={
    ":)":"happy emoji",
    ":(":"sad emoji"
}
output = ""
for word in words :
    output += emojis.get(word,word)+" "
print(output)

# functions
# use of meaningfull and discriptive words
# use of underscore  and lowercase letters
# called after defining
#we use def
# fuction name
#parentesis()
def greet():
    print("Hi there")
    print("welcome aboard")
greet()#calling

# parameters
# arguments
# how to cast inputs/parameters
def greet(first_name,last_name):#argument
    # first_name,last_name are parameters
    # when calling we must suply all the arguments
    print(f"Hi {first_name} {last_name}")
    print("welcome aboard")
greet("ropy","kevin")
# "ropy","kevin" are positional arguments
# type of functions
# first_name,last_name are parameters

# key arguments(mostly used when dealing with functions that TAKE NUMERICAL VALUES)
#should alway come after positional arguments
def greet(firstname,lastname):
    print(f"Hi there{firstname}, {lastname}")
    print("welcome aboard")
greet(lastname="kevin",firstname="ropy")#calling
# lastname="kevin",firstname="ropy" are keyword arguments

# another examble
def calc_cost(total=50,shipping=5,discount=0.1):
    print(f"the total is{total}, {shipping}, {discount}")

# functions that return values
def square(number):
    return number*number
result=square(4)
print(result)

# creating reusable functions
def emoji_converter(message):
    words = message.split(" ")
    emojis ={
        ":)":"happy emoji",
        ":(":"sad emoji"
    }
    output = ""
    for word in words :
        output += emojis.get(word,word)+" "
    return output
message =input(">")
result=emoji_converter(message)
print(result)

# exceptions (how to handle errors)
#0 success
#1 error
# look at type error
#use of try to handle exceptions with except
# ValueError only picks errors of non_numerical_value to an interger
try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid Value")
# ZeroDivisionError
try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print("Invalid Value")

#comments
# use of (#)
# use for why and hows

#   Classes
# pascal naming convention
# capitalize the first letter of every word
# used to define new types
# these types can have methods that we define in the body of the class and they can also have
# attributes that we can set anywhere in our programs
class Point :
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point1 =Point
point1.x=10
point1.y=20
print(point1.x) 
Point.draw()
# point 2 is different from the first object
point2=Point()
point2.x=1
print(point2.x)

# constructors
# this is a function that gets called at the time of creating an object
class Point :
    def __init__(self,x,y):#constructor
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point = Point(10,20)
print(point.x)#

# another example
class Person :
    def __init__(self,name):#constructor
        self.name=name
    def talk(self):
        print(f"hi, I am  {self.name} ")

ropy = Person("ropy kevin")
ropy.talk()
bob =Person("Bob smith")
bob.talk()

#  inheritance
# reuse of code
# avoids repetation
class Dog:
    def walk(self):
        print("walk")
class cat:
    def walk(self):
        print("walk")
# thats repetition instead we should creat one for both

class Mammal:
    def walk(self):
        print("walk")
# dog inheriting mammal
class Dog(Mammal):
    def bark(self):
        print("bark")

dog1=Dog()
dog1.bark

# cat inheriting mammal
class Cat(Mammal):
    def be_annoying(self):
        print("annoying")
cat1=Cat()
cat1.be_annoying

#   Modules
# a file with some python code
# 
import converters
from converters import kg_to_lbs
kg_to_lbs(100)
print(converters.kg_to_lbs(70))
#  we can put the above functions on one module call converters so that we can use frequently

# packages
# how to create and use packages
# first approach(entire module)
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
# second approach
from ecommerce.shipping import calc_shipping
calc_shipping()
calc_shipping()
calc_shipping()
# third option
from ecommerce import shipping
shipping.calc_shipping()

# generating random values in python
# usin random module 
import random
for i in range(3):
    print(random.random())#generates a random value from 0 to 1

for i in range(3):
    print(random.randint(10,20))#random values btw 10 and 20

members=["ropy","ken","ivy","kim","mike"]
leader=random.choice(members)#picks a random character in the list
# dice excercise
import random
class Dice():
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second
dice=Dice()
print(dice.roll())

# files and directories
# examples
from pathlib import Path

# ways
#Absolute path
#c:\program files\microsoft
#Relative path
path=Path("ecomerce")
print(path.exists())#returns a boolean
#mkdir() used to create a directory
#rmdir() used to remove directory
path=Path()
print(path.glob("*"))#all files and all directories
# (*.*) all files (*.py)generator objects
path=Path()
for file in path.glob("*.py"):
    print(file)

#Pypi and Pip(Huh?)












