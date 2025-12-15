# import libraries
import sys

# Entry point function
def main():
    n = 10
    l = 12

    result = n + l # Addition
    print(f"{n} + {l} = {result}")

    # Subtraction
    print(f"{l} - {n} = {l - n}")

    num1 = 2
    num2 = 5

    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

    result = num2 / num1
    print(f"Normal division {num2} / {num1} = {result}")

    print(f"Floor division {num2} // {num1} = {num2 // num1}")

    print(f"Exponential operation {num2} ** {num1} = {num2 ** num1}")

    print(f"Modulus operation {num2} % {num1} = {num2 % num1}")

    sys.exit(0)

# Call the main()
main()


    
    
    
