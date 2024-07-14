history = []

def addition():
    print("Please enter 2 numbers to add:")
    a = int(input("a = "))
    b = int(input("b = "))
    addresult = a + b
    result = ("Result of " +str(a)+ " + " +str(b)+ " = " +str(addresult))
    print(result)
    history.append(result)


def subtraction():
    print("Please enter 2 numbers to subtract:")
    a = int(input("a = "))
    b = int(input("b = "))
    subtractresult = a - b
    result = ("Result of " +str(a)+ " - " +str(b)+ " = " +str(subtractresult))
    print(result)
    history.append(result)

def multiplication():
    print("Please enter 2 numbers to multiply:")
    a = int(input("a = "))
    b = int(input("b = "))
    multiplyresult = a * b
    result = ("Result of " +str(a)+ " * " +str(b)+ " = " +str(multiplyresult))
    print(result)
    history.append(result)
    
def division():
    print("Please enter 2 numbers to divide:")
    a = int(input("a = "))
    b = int(input("b = "))
    divideresult = a / b
    result = ("Result of " +str(a)+ " / " +str(b)+ " = " +str(divideresult))
    print(result)
    history.append(result)

def exponentiation():
    print("Please enter the first number to be raised to the power of the second number:")
    a = int(input("a = "))
    b = int(input("b = "))
    exponentresult = a ** b
    result = ("Result of " +str(a)+ " ** " +str(b)+ " = " +str(exponentresult))
    print(result)
    history.append(result)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. View History")
        print("7. Quit")
        choice = input("Choice: ")
    
        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            multiplication()
        elif choice == "4":
            division()
        elif choice == "5":
            exponentiation()
        elif choice == "6":
            for operation in history:
                print(operation)
        elif choice == "7":
            break
        else:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    main()