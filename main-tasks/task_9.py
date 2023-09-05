# // Write a program called stars.py. It should prompt the user for a number, and it should print the number of stars till the number entered.
#     // Example If rows is 5, it should print the following:
#     // *
#     // **
#     // ***
#     // ****
#     // *****.
# rows = int(input("Enter a number: "))

# def star_row():
#     count = 0
#     format = ""
#     for i in range(1, rows + 1):
#         format= "*" * i
#         count += 1
#         if count == rows:
#             format += "." * i
#     return format

# result = star_row()
# print(result)
stars=int(input("Enter a number: "))
count=0
for i in range(1,stars+1):
    value=("x"*i)
    count=count+1
    if count==stars:
        value+=("."*i)
    print(value)    