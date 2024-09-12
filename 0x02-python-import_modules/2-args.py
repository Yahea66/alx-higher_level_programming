#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    length = len(args) - 1
    if length != 1:
        print("{} arguments:".format(length))
    else:
        print("{} argument:".format(length))
    for i in range(length):
        if i == 0:
            continue
        print("{}: {}".format(i, args[i]))
