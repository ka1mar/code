import numpy as np
from math import exp
from prettytable import PrettyTable

class function:
    f = "exp(3x)"
    def __call__(self, x):
        return exp(3*x)
    def fd(self, x):
        return 3*exp(3*x)
    def sd(self, x):
        return 9*exp(3*x)


def first_dif(func, x, y, h, M):
    y_1 = []
    y_1t = []
    y_1.append((-3*y[0] + 4*y[1] - y[2])/(2*h))
    for i in range(1, M):
        y_1.append((y[i+1]-y[i-1])/(2*h))
    y_1.append((3*y[M] - 4*y[M-1] + y[M-2])/(2*h))
    for i in range(0, M+1):
        y_1t.append(func.fd(x[i]))
    y_p = abs(np.array(y_1t)-np.array(y_1))
    return(np.column_stack([y_1, y_p]))

def sec_dif(func, x, y, h, M):
    y_2 = []
    y_2t = []
    y_2.append((y[2] - 2*y[1] + y[0])/(h**2))
    for i in range(1, M):
        y_2.append((y[i+1] - 2*y[i] + y[i-1])/(h**2))
    y_2.append((y[M] - 2*y[M-1] + y[M-2])/(h**2))
    for i in range(0, M+1):
        y_2t.append(func.sd(x[i]))
    y_p = abs(np.array(y_2t)-np.array(y_2))
    return(np.column_stack([y_2, y_p]))


if __name__ == '__main__':
    print("Нахождение производных, вариант 11")
    func = function()
    print("f =", func.f)

    M = int(input("Введите число точек в таблице: "))
    a = float(input("Введите начало отрезка: "))
    h = float(input("Введите шаг h: "))
    x = []
    y = []
    x_ = 0

    for j in range (0, M+1):
        x_ = a + j*h
        x.append(x_)
        y.append(func(x_))

    F = np.column_stack([x, y])
    p1 = first_dif(func, x, y, h, M)
    p2 = sec_dif(func, x, y, h, M)

    mytable = PrettyTable()
    mytable.field_names = ["x","y","y'", "пoгрешность","y''", "погрешность"]

    dif = np.column_stack([x,y, p1, p2])
    mytable.add_rows(dif)

    print("Tаблица производных:")
    print(mytable)
