import math

def calculator():
    print("Please choose option for mathemetical operations :")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7.Root")

    option = int(input("Enter your option from 1 to 7 : "))

    if option in (1, 2, 3, 4, 5, 6, 7):
        num1 = int(input("Enter the number :"))
        num2 = int(input("Enter the number :"))
    else:
        print("Invalid option")
        print("Please choose option between 1 to 7:")

    if option == 1:
        print("Addition Operation : ",num1, "+", num2, "=", num1 + num2)
    elif option == 2:
        print("Subtraction Operation : ", num1, "-", num2, "=", num1 - num2)
    elif option == 3:
        print(num1, "*", num2, "=", num1 * num2)
    elif option == 4:
        if num1 == 0:
            print("Cannot divide by zero")
        elif num2 ==0:
            print("Cannot divide by zero")
        print("Multiplication Operation : ",num1, "/", num2, "=", num1 / num2)
    elif option == 5:
        print("Multiplication Operation : ",num1, "%", num2, "=", num1 % num2)
    elif option == 6:
        print("Multiplication Operation : ",num1, "**", num2, "=", num1 ** num2)
    elif option == 7:
        print("Multiplication Operation : ",num1, "root", num2, "=", math.sqrt(num1))
        

if __name__ == "__main__":
    calculator()