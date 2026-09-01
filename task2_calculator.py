# CODSOFT Python Programming Internship
# Task 2: Calculator

def calculator():

    print("\n===== SIMPLE CALCULATOR =====")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            result = num1 + num2
            print("Result =", result)

        elif choice == "2":
            result = num1 - num2
            print("Result =", result)

        elif choice == "3":
            result = num1 * num2
            print("Result =", result)

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print("Result =", result)

        else:
            print("Invalid operation.")

    except ValueError:
        print("Please enter valid numbers.")


while True:

    calculator()

    again = input("\nDo you want to calculate again? (y/n): ")

    if again.lower() != "y":
        print("Thank you for using the calculator!")
        break
