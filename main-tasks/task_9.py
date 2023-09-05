# // Write a program called stars.py. It should prompt the user for a number, and it should print the number of stars till the number entered.
#     // Example If rows is 5, it should print the following:
#     // *
#     // **
#     // ***
#     // ****
#     // *****.
rows = int(input("Enter a number: "))

def star_row():
    count = 0
    format = ""
    for i in range(1, rows + 1):
        format= "*" * i
        count += 1
        if count == rows:
            format += "." * i
    return format

result = star_row()
print(result)
