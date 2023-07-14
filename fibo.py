#!/usr/bin/python3

def fib(num):
    if num == 0 or num == 1:
        return 1
    list_num = [fib(num - 1), fib(num - 2)]
    return sum(list_num)


res = []
for i in range(10):
    res.append(fib(i))

print(res)
