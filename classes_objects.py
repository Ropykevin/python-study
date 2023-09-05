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

class Person():
  name=""
  gender=""
  emails=""
  phone=""
  details=[]
  #constructor-A special methodused
  #to instanstiate initial values
  def __init__(self,n,g,e,p):
    self.name=n
    self.gender=g
    self.emails=e
    self.phone=p
  def add (self):
    self.details.append(self.name)
    self.details.append(self.gender)
    self.details.append(self.emails)
    self.details.append(self.phone)
p1=Person("ropy","male","ropykevin@gmail.com",+254742670714)
print(p1.emails)
print(p1.name)
print(p1.gender)
print(p1.phone)

p1.add()
print(p1.details)
p2=Person(input("enter name: "),
          input("enter gender: "),
          input("enter email: "),
          input("enter phone-number: "))
p2.add()
print(p2.details)