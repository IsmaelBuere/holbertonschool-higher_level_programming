#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = 10
    b = 5

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

    result = a + b
    print("Result of adding {} and {}: {}".format(a, b, result))

