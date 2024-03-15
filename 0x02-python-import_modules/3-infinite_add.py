#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv
    sum = 0
    for i in arguments[1:]:
        sum += int(i)
    print(sum)
