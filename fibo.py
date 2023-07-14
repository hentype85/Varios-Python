#!/usr/bin/python3

def fib(num):
    """ calcula el numero fibonacci que
        corresponde al indice dado y
        lo retorna
    """
    if num == 0 or num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)


""" cargar indices en lista
    para imprimir
"""
n = 25
new_list = []
for i in range(0, 25):
    new_list.append(fib(i))

print(new_list)
