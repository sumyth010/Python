


# name = input("What is your name ?")

# print(f"Hello {name}, I am learing Python!")


# num1 =  int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# additon = num1 + num2
# subtraction  = num1 - num2
# multiply = num1 * num2
# divison = num1 / num2

# print(f"The sum is {additon}")
# print(f"The sub is {subtraction }")
# print(f"The Multiplation is {multiply}")
# print(f"The Divsion is {divison}")


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second Nunmebr: "))


# print("Choose operation")
# print("1. Addidtion")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Divison")

# choice = int(input("Your Choice: "))

# if choice == 1:
#     add = num1 + num2
#     print(f"The resullt is {add} " )
# elif choice == 2:
#     sub = num1 - num2
#     print(f"The result is {sub}" )
# elif choice == 3 : 
#     mul = num1 * num2
#     print(f"The result is {mul}")
# elif choice == 4:
#     div = num1 / num2
#     print(f"The result is {div}")
# else:
#     print("Invalid choice, please try again.")



while True:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Choose opration")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divison")

    choice = int(input("Your choice: "))

    if choice == 1: 
        add = num1 + num2
        print(f"The result is {add}")
    elif choice == 2: 
        sub = num1 - num2
        print(f"The result is {sub}")
    elif choice == 3: 
        mul = num1 * num2
        print(f"The result is {mul}")
    elif choice == 4:
        div = num1 / num2
        print(f"The result is {div}")
    else:
        print("Invalid choice")
    
    continues = input("Do you want to continue? (yes/no)")
    if continues.lower() == "no":
        print("Goodbye")
        break
