import os
import sys

def addNumbers(x,y):
    result = int(x+y)
    return result

def main():
    if len(sys.argv) > 2:
        first_number = int(sys.argv[1])
        second_number = int(sys.argv[2])
        print("First Number: " + str(first_number) + "  and Second Number: " + str(second_number))
        result = addNumbers(first_number, second_number)
        print("Result: "+ str(result))
    else:
        print("Improper number of arguments provided")

if __name__ == "__main__":
    main()
