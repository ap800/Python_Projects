#Mini Calculator in Python using elif statements 

num1= float(input("Please enter your first number: "))
op= input("Please enter your operator: ")
num2= float(input("Please enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Please enter a valid operator")