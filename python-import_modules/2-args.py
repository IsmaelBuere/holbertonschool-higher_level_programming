#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def main():
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("Number of arguments: 0.")
    elif num_args == 1:
        print(f"Number of argument: 1:")
    else:
        print(f"Number of arguments: {num_args}:")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
