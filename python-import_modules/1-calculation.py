#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    if n == 1:
        print("No arguments.")
    else:
        if n == 2:
            print(f"{n-1} argument:")
        else:
            print(f"{n-1} arguments:")
        
        for i in range(1, n):
            print(f"{i}: {sys.argv[i]}")
