#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arguments = sys.argv
    operators = ["+", "-", "*", "/"]

    if len(arguments) > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(arguments[1])
        b = int(arguments[3])
        operator = arguments[2]

        if operator not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif arguments[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif arguments[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif arguments[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
