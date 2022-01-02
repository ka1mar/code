import numpy as np
import matplotlib.pyplot as plt
from math import sin

class function:
    f = "2*x**2 - 2**x -5"
    def __call__(self, x):
        return 2*x**2 - 2**x -5
    def paint(self, a, b, M, x, y):
        plt.title("График функции")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.plot(x, y)
        plt.show()


def enter_y0(M):
    y0 = float(input("Введите точку интерполирования: "))
    print("Введите степень интерполяционного многочлена < ", M)
    N = int(input())
    while int(N) >= int(M):
        print("степень должна быть меньше ", M, ", повторите ввод")
        N = int(input())
    return (y0, N)

def mono_up(y, M):
    for j in range(1, M):
        if y[j]-y[j-1] < 0:
            return False
    return True

def mono_do(y, M):
    for j in range(1, M):
        if y[j]-y[j-1] > 0:
            return False
    return True

def sort_y(f, y0):
    comp = np.array(abs(f[:, 0] - y0))
    f = np.column_stack([f, comp])
    f = f[np.argsort(f[:, 2])]  # сортируем по последней строке
    f = np.delete(f, np.s_[2], 1)  # удалили последнюю строку
    return f

def lagrange(N, f, y0):
    Pol = float(0)
    for i in range(0, N + 1):
        p = float(1)
        for j in range(0, N + 1):
            if i != j:
                p = p * (y0 - f[j][0]) / (f[i][0] - f[j][0])
        p = p * f[i][1]
        Pol = Pol + p
    return Pol

def pollagrange(N, f):
    pol = ""
    Pol = float(0)
    for i in range(0, N + 1):
        p = float(1)
        p_ = "1"
        for j in range(0, N + 1):
            if i != j:
                p = p * (y0 - f[j][0]) / (f[i][0] - f[j][0])
                p_ = p_ + "* (x -" + str(f[j][0]) + ") / (" + str(f[i][0]) + "-" + str(f[j][0]) + ")"
        p = p * f[i][1]
        p_ = str(f[i][1])+" * ("+p_+")"
        Pol = Pol + p
        pol = pol + "  +  " + p_
    return pol

def polbisection(ra, rb, Pol, e, y0):
    i = 0
    rc = 0
    while abs(rb-ra) > e:
        i+=1
        rc = ra+ (rb-ra)/2
        x = ra
        t1 = eval(Pol)
        x = rc
        t2 = eval(Pol)
        if t1*t2 < 0:
            rb = rc
        else:
            ra = rc
    x = rc
    print('точка x= ', round(rc, 3),'; ', i, ' шагов, длина последнего сегмента= ', rb-ra)
    print("модуль невязки=", abs(y0 - func(x)))



if __name__ == '__main__':
    print("Задача обратного алгебраического интерполирования, вариант 11")
    func = function()
    print("f =", func.f)

    M = int(input("Введите число точек в таблице: "))
    a = float(input("Введите начало отрезка: "))
    b = float(input("Введите конец отрезка: "))
    x = []
    y = []
    x_ = 0

    for j in range (0, M):
        x_ = a + j*(b-a)/(M-1)
        x.append(x_)
        y.append(func(x_))

    F_ = np.column_stack([x, y])
    print("таблица значений функции:\n", F_)
    func.paint(a, b, M, x, y)

    if mono_up(y, M) or mono_do(y, M):
        print("Функция монотонна, интерполируем обратную функцию методом Лагранжа:")
        y0 = 0
        N = 0
        y0, N = enter_y0(M)
        print("Точка обратного интерполирования: ", y0)
        F = np.column_stack([y, x])

        f = sort_y(F, y0)
        f = f[0:N + 1, 0:N + 1]
        print("Отсортированная таблица значений функции: \n", f)
        fy0_l = lagrange(N, f, y0)
        print("Значение в точке ", y0, " по методу Лагранжа = ", fy0_l)
        print("Модуль невязки: ", abs(y0 - func(fy0_l)))

        print("Ищем корень методом бисекции:")
        Pol = pollagrange(N, F_) + " - " + str(y0)
        h = (b - a) / 100
        x = a
        roots = []
        for i in range(0, 101):
            t1 = eval(Pol)
            x = x + h
            t2 = eval(Pol)
            if t1 * t2 <= 0:
                roots.append(x - h)
                roots.append(x)
        e = float(input("Введите e: "))

        for i in range(0, len(roots) - 1, 2):
            polbisection(roots[i], roots[i + 1], Pol, e, y0)

    else:
        print("Функция не монотонна, ищем корень методом бисекции:")
        y0, N = enter_y0(M)
        Pol = pollagrange(N, F_) + " - " + str(y0)
        h = (b - a) / 100
        x = a
        roots = []
        for i in range(0, 101):
            t1 = eval(Pol)
            x = x + h
            t2 = eval(Pol)
            if t1 * t2 <= 0:
                roots.append(x-h)
                roots.append(x)
        e = float(input("Введите e: "))

        print()
        for i in range(0, len(roots)-1, 2):
            polbisection(roots[i], roots[i+1], Pol, e, y0)



