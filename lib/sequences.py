#!/usr/bin/env python3

def print_fibonacci(length):
    num1 = 0
    num2 = 1
    count = 0
    fib_sequence = []

    while count < length:
        fib_sequence.append(num1)
        num1, num2 = num2, num1 + num2
        count += 1

    print(f'[{", ".join(map(str, fib_sequence))}]')

print(print_fibonacci(9))