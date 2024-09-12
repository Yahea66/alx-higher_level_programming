#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    length = len(args) 
    if length != 1:
        print("{} arguments:".format(length - 1))
    else:
        print("{} argument:".format(length - 1))
    for i in range (length):
        if i == 0:
            continue
        print("{}: {}".format(i, args[i])) 
