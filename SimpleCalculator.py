# import libraries
import sys

# Entry point function
def main():
    choose = -1  # Loop variable intialization

    while choose != 0:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = None
        
        print("Choose from the following options - ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("0. To exit")
        choose = int(input("Enter your option: "))

        if choose == 1:
            print("Performing addition")
            result = num1 + num2
        elif choose == 2:
            print("Performing subtraction")
            result = num1 - num2
        elif choose == 3:
            print("Performing multiplication")
            result = num1 * num2
        elif choose == 4:
            print("Performing division")
            result = num1 / num2
        elif choose == 0:
            break
        else:
            print("[INFO] Invalid option provided!!!")
            print("Please try again...")

        if result != None:
            print(f"Result: {result}")
            
    sys.exit(0)

# Call main()
main()
