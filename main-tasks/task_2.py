# Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal.
# Depending on whether the number is even or odd, display  
# either “odd” or “even” to the user.
# Hint: how does an even / odd number react differently when divided by 2*/

number=int(input("enter number: "))
if number%2==0:
    print(f"Number {number } is even")
elif number%2>0:
    print(f"Number {number } is odd")
else:
    number="invalid"

# If the number is a multiple of 4, print out “divisible by 4”.
if number%4==0:
    print(f"number { number } is divisible by 4")

