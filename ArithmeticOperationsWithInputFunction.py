# import libraries
import sys

# Entry point function
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 + num2
    print(f"{num1} + {num2} =  {result}")
    sys.exit(0)

# Call main()
main()
