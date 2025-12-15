"""
    Program to print temerpature from
    farenheit to celsius in step of 20
    from 0 to 300
"""
# import libraries
import sys

# Entry point function
def main():
    # Local variable declaration
    lower = 0  # Lower temperature limit
    upper = 300  # Upper temperature limit
    step = 20  # Incremental temperature step

    # Initialize loop variable
    farh = lower
    while farh <= upper:
        celsius = int((farh - 32) * (5/9))
        print(f"{farh}\t=\t{celsius}")
        farh = farh + step

    sys.exit(0)

# Call entry point function
main()

    
