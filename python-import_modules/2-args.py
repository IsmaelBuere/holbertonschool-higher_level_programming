#!/usr/bin/python3
import sys
if __name__ == "__main__":

    num_arguments = len(sys.argv) - 1

    print("Number of argument(s): {}".format(num_arguments)

    if num_arguments == 0:
        print(".\n")
    else:
        for i, arg in enumerate(sys.argv[i:], start = 1):
            print("{}: {}".format(i, arg))

        print()
