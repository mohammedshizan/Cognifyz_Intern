def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


user_input = input("Enter your choice(1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if user_input == '1':
    print("Result:", add(num1, num2))
elif user_input == '2':
    print("Result:", subtract(num1, num2))
elif user_input == '3':
    print("Result:", multiply(num1, num2))
elif user_input == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")
    
    
    
    
