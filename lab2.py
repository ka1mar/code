import numpy as np
from math import sin


class function():
    def __call__(self, x):
        return 1/2*(x**2) + sin(x)
    a = 0.4
    b = 0.9
    x0 = 0.75
    N = 7
    M = 15



def sort_x(f, x0):
    comp = np.array(abs(f[:, 0] - float(x0)))
    f = np.column_stack([f, comp])
    f = f[np.argsort(f[:, 2])]  # сортируем по посл строке
    f = np.delete(f, np.s_[2], 1)  # удалили посл строку
    return f


def enter_x0():
    x0 = float(input("Введите точку интерполирования: "))
    N = int(input("Введите степень интерполяционного многочлена <M: "))
    while int(N) >= int(M):
        print("степень должна быть меньше ", M, ", повторите ввод")
        N = input()
    return (x0, N)


def lagrange(N, f):
    Pol = float(0);
    for i in range(0, N + 1):
        p = float(1);
        for j in range(0, N + 1):
            if i != j:
                p = p * (x0 - f[j][0]) / (f[i][0] - f[j][0])
        p = p * f[i][1]
        Pol = Pol + p
    return Pol


def dividedDiffTable(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j]));
    return y;


def printDiffTable(y, n):
    print("Таблица раздельных разностей:")
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t", end=" ");
        print("");


def applyFormula(x0, x, y, n):
    sum = y[0][0];
    for i in range(1, n):
        mul_x = 1
        for j in range(i):
            mul_x = mul_x * (x0 - x[j]);
        sum = sum + (mul_x * y[0][i]);
    return sum;


if __name__ == '__main__':
    f = function()

    print("Задача алгебраического интерполирования, вариант 11")
    M = int(input("Введите число M значений в таблице: "))
    print("Введите точки x: ")
    x = np.array(input().split()).astype(float)
    while int(x.size) != int(M):
        print("размер не равен ", M, ", повторите ввод")
        x = np.array(input().split()).astype(float)
    print("Введите f(x): ")
    y = np.array(input().split()).astype(float)
    while int(y.size) != int(M):
        print("размер не равен ", M, ", повторите ввод")
        y = np.array(input().split()).astype(float)
    F = np.column_stack([x, y])
    print("таблица значений функции:\n", F)


    x0, N = enter_x0()
    print(x0)
    f = sort_x(F, x0)
    f = f[0:N+1, 0:N+1]
    print("Отсортированная таблица значений функции:\n", f)
    fx0_l = lagrange(N, f)
    print("Значение в точке ", x0, " по методу Лагранжа = ", fx0_l)

    x = f[0:N, 0]
    y = f[0:N, 1]
    y_table = [[0 for i in range(N-1)] for j in range(N)]
    y = np.column_stack([y, y_table])
    y = dividedDiffTable(x, y, N);
    printDiffTable(y, N)
    fx0_n = applyFormula(x0, x, y, N)
    print("Значение в точке ", x0, " по методу Ньютона = ", fx0_n)





