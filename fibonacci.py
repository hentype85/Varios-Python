#!/usr/bin/python3

def fib(n):
    a = 0
    b = 1
    while a < n:
        print(a, b, end=" ")
        a = a + b
        b = a + b
    print()


fib(100)
