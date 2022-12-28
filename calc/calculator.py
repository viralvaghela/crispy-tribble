num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("What do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice(1/2/3/4): ")

if choice == '1':
    print(num1, "+", num2, "=", float(num1) + float(num2))

elif choice == '2':
    print(num1, "-", num2, "=", float(num1) - float(num2))

elif choice == '3':
    print(num1, "*", num2, "=", float(num1) * float(num2))

elif choice == '4':
    try:
        print(num1, "/", num2, "=", float(num1) / float(num2))
    except Exception as e:
        print("Cannot divide by zero, please try again.", e)

else:
    print("Invalid input")
