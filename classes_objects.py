#classes are a collection of functions and variables
# that are realted and manipulate each other 
#a function inside a class is called a method
#a variable inside a class is called a property
#representation of something in nthe real world 
#example student
#here you have all values and poperty
#related to a student e.g create_student(),email 

#ERB
class MyClass:
    x=5
# object

x1=MyClass()
print(x1.x)

# __init__()function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The __str__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
# object methods

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()