

# def greet(name):
#     print(f"Hello {name}!")

# greet("Alex")
# greet("Sam")

def calculator(num1, num2, choice):
    if choice == 1 :
        print(f"The result is {num1 + num2}")
    elif choice == 2: 
        print(f"The result is {num1 - num2}")
    elif choice == 3: 
        print(f"The result is { num1 * num2}")
    elif choice == 4: 
        if num2 == 0: 
             print("Error: Cannot divide by zero")
        else:
            print(f"The result is {num1/num2}")
    else:
        print("Invalid Choice")

while True: 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the Second number: "))

    print("Choice Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divison")

    choice = int(input("Enter a number: "))

    calculator(num1, num2, choice)

    continues = input("Do you want to continue Yes/No ?")
    if continues.lower() == "no":
        print("Goodbye!")
        break


