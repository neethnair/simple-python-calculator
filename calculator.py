def main():
    print("Welcome to the Calculator app.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    user_input = str(input("What would you like to do today?"))
    if user_input == 'addition':
        num3 = num1 + num2
        print ("Your answer is", str(num3))
    elif user_input == 'subtraction':
        num3 = num1 - num2
        print("Your answer is", str(num3))
    elif user_input == 'multiplication':
        num3 = num1 * num2
        print("Your answer is", str(num3))
    elif user_input == 'division':
        num3 = num1/num2
        print("Your answer is", str(num3))
    else:
        print("Invalid. Please select addition, subtraction, multiplication or division.")    

if __name__ == "__main__":
    main()
