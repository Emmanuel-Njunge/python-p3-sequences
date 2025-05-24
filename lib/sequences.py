#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    for i in range(length):
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)

print_fibonacci(9)
