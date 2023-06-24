#!/usr/bin/python3

def pascal_triangle(n):

    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                num = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(num)
            row.append(1)
            triangle.append(row)
        return triangle


def main():
    n = int(input("ingrese el numero de filas para el triangulo de Pascal: "))
    triangle = pascal_triangle(n)
    print("triangulo de Pascal:")
    for row in triangle:
        print(row)

if __name__ == "__main__":
    main()
