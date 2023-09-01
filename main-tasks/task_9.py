# // Write a program called stars.py. It should prompt the user for a number, and it should print the number of stars till the number entered.
#     // Example If rows is 5, it should print the following:
#     // *
#     // **
#     // ***
#     // ****
#     // *****.
rows = int(input("Enter a number: "))
count=0
for i in range(1, rows + 1):
  value=("*" * i)
  count=count
  if count==rows:
    value=value+("."*i)
