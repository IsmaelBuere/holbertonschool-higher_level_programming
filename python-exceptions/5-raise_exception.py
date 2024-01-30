#!/usr/bin/python3
def raise_exception():
    try:
        raise ValueError("Custom type exception raised")
    except ValueError as e:
        print("Caught an exception:", e)
