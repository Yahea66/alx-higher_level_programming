#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    length = len(args)
    result = 0
    for i in range(length):
        if i == 0:
            continue
        result += int(args[i])
    print(result)
