# Simple Mini Calculator

# Ask the user for the first number
num1 = float(input("Enter the first number: "))

# Ask the user for the second number
num2 = float(input("Enter the second number: "))

# Ask the user for the operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*": 
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else: 
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid Operation!"

# Show the result
print("Result:", result)