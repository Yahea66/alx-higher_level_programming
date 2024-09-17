#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    length = len(args) - 1
    if length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    oprs = ["+", "-", "*", "/"]
    functions = [add, sub, mul, div]
    first = int(args[1])
    opr = args[2]
    second = int(args[3])

    for o, f in zip(oprs, functions):
        if o == opr:
            print("{} {} {} = {}".format(first, opr, second, f(first, second)))
            exit(0)

    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
