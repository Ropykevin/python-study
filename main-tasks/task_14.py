def add_two_values(num1=None, num2=None):
    try:
        if num1 is None:
            num1 = float(input("Enter the first number: "))
        if num2 is None:
            num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid character entered. Please enter numbers or floats only.")
        return add_two_values()
    else:
        return num1 + num2

value = add_two_values()
print("The sum is:", value)
