#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        return
    elif length == 1:
        print(0)
        return
    elif length == 2:
        print(0)
        print(1)
        return
    
    a, b = 0, 1
    print(a)
    print(b)
    for _ in range(2, length):
        a, b = b, a + b
        print(b)
