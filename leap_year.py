"""
    Write a program to check leap year
"""

# import libraries
import sys

# Entry point function
def main():
    year = int(input("Enter the year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year...")
    else:
        print(f"{year} is not a leap year!!!")

    sys.exit(0)

# Call main()
main()
