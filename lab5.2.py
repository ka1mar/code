import numpy as np
from math import sin, cos, sqrt, pi

class function:
    f = 'cos(2,6x)/(0,3 + x^2)'
    def __call__(self, x):
        return cos(2.6*x)/(0.3 + x**2)


def calculate_meler(func, n):
    coef = pi/n
    print('A = pi /',n,'=', coef)
    integral = 0
    for i in range(1, n+1):
        root = cos(pi*(2*i-1)/(2*n))
        if abs(root) < 0.000000001: root = 0
        print('root =', root)
        integral += coef*func(root)
    return round(integral, 12)


if __name__ == '__main__':
    print('Вычисление интеграла при помощи КФ Мелера')
    func = function()
    print('Функция', func.f)

    while (True):
        n = int(input("Введите N: "))
        print('Значение по КФ:', calculate_meler(func, n))
        print()