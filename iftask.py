# Simple Questions:
#  1.Given a variable temperature with a value of 25°C, write an if statement to check if the temperature is above 30°C using the greater than (>) operator.
#  2.	Create a dictionary called stock with items as keys and their quantities as values. Write an if-else statement to check if the quantity of "apples" is zero using the equality (==) operator. 
# 3.	Declare a list called even_numbers containing integers. Write an if statement to check if the first element of the
temperature = 25
if temperature >30:
    print('temperature is above 30°C')
else:
    print("temperature is below 30°C")

#  2.Create a dictionary called stock with items as keys and their quantities as values. Write an if-else statement to check if the quantity of "apples" is zero using the equality (==) operator. 
stock= {
    "apples":0,
    "mangoes":50,
    "oranges":70,
    "bananas":35
}

if stock["apples"]==0:
    print("apple quantity is 0")
else:
    print("apples quantity is greater than 0") 

# 3.Declare a list called even_numbers containing integers. Write an if statement to check if the first element of the
#  the list is an even number using the modulo (%) operator 

even_numbers=[1,2,3,4,5,5,6,7,7,8,9,]
if even_numbers[0]%2==0:
    print("number is even")
else:
    print("number is not even")

# 4. Given a list prices containing prices of products, write a code snippet using 
# if statements to check if any product's price is within the range $20 to $50 using the 
# logical and operator.

prices = [10, 25, 30, 40, 55, 60]
# if prices[:]>20 and prices[:]<50:
#     print("price btw 20 and 50")
# else:
#     print("uiyhgf")
for price in prices:
    if 20 <= price <= 50:
        print(f"{price} is within the range $20 to $50.")
    else:
        print(f"{price} is not within the range $20 to $50.")

# Imagine you have a list employees containing dictionaries with keys 
# "name", "hours_worked", and "hourly_rate". Write a code snippet using
# nested if statements to calculate the salary for an employee named "Alice" 
# based on her hours worked and hourly rate.
employees=[
    {'name':"kevin",
    "hours_worked":20,
    "hourly_rate":100
     },
    {'name':"alice",
    "hours_worked":20,
    "hourly_rate":100
     },
    {'name':"kevin",
    "hours_worked":20,
    "hourly_rate":100
     },
    {'name':"kevin",
    "hours_worked":20,
    "hourly_rate":100
     }
]
# name="alice"
# if employees[name]==True:
#     print("alice")
# else:
#     print("tttt")
salary = (employees["hours_worked"] * employees["hourly_rate"])
for employee in employees:
    if employee["name"] == "Alice" and employee["hours_worked"] >0:
        salary = employee["hours_worked"] * employee["hourly_rate"]
    else:
        salary = employee["hours_worked"] * employee["hourly_rate"]         
    print(f"{employee['name']}'s salary is {salary}.")

# 5.	Create a dictionary book_ratings with book titles as keys and their ratings as values. 
# Write an if-elif-else statement to find out if a book "The Adventure" 
# has a rating of 5 or is rated below 2.

book_ratings = {
    "The Adventure": 5,
    "The Mystery": 3,
    "The Romance": 4,
    "The Thriller": 2,
    "The Comedy": 1,
}
book = "The Adventure"
if book_ratings[book] == 5:
    print(f"{book} has a rating of 5.")
elif book_ratings[book] < 2:
    print(f"{book} is rated below 2.")
else:
    print(f"{book} has a rating of {book_ratings[book]}.")

# Suppose you have two sets: set_x and set_y.
# Write a code snippet using conditional statements to check 
# if the symmetric difference between the two sets is not empty, using the ^ 
# (symmetric difference) operator
set_x = {"apple", "banana", "cherry"}
set_y = {"lenovo", "hp", "apple"}
if set_x ^ set_y:
    symetric=set_x ^ set_y
else: 
    symetric= 'none'
print(symetric)
