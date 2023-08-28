# fuctions
#we use def
# fuction name
#parentesis()
def greet():
    print("Hi there")
    print("welcome aboard")
greet()
# arguments
# how to cast inputs/parameters
def greet(first_name,last_name):#argument
    print(f"Hi {first_name} {last_name}")
    print("welcome aboard")
greet("ropy","kevin")#parameters
# type of functions
def greet_me(name):
    print(f"hi{name}")
greet_me("ropy")
# there are two types of functions in python
# 1.function that perfoms a task(print,greet)
# 2.functions that returns a value(calculates and returns)
def get_greeting(name):
    return f"hi {name}"

message =get_greeting("ropy")

def increment(number,by):
    return number + by

print(increment(2,by=1))#key word argument

# default arguments(comes as the last argument)
def increment(number,by=1):
    return number + by
print(increment(2))#3
print(increment(2,5))#7

# args,wait,what
#use of asterics
#plural arguments
