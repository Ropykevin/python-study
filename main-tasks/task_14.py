def add_two_values():
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
  except ValueError:
    print("Invalid character entered. Please enter numbers or floats only.")
    return add_two_values()
  else:
    return num1 + num2
print(add_two_values())