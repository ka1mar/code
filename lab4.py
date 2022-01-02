import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos

class function:
    f = "sin(x)*x - 1"
    def __call__(self, x):
        return sin(x)*x - 1
    def integr(self, a, b):
        return sin(b)-b-b*cos(b) - sin(a)+a + a*cos(a)

class function0:
    f = "5"
    def __call__(self, x):
        return 5
    def integr(self, a, b):
        return 5*(b-a)

class function1:
    f = "8*x"
    def __call__(self, x):
        return 8*x
    def integr(self, a, b):
        return 4*(b*b-a*a)

class function2:
    f = "2*x**2 - x +2"
    def __call__(self, x):
        return 2*x**2 - x +2
    def integr(self, a, b):
        return (2/3)*(b**3-a**3) - (b**2-a**2)/2 + 2*(b-a)


class function3:
    f = "x**3 - 1"
    def __call__(self, x):
        return x**3 - 1
    def integr(self, a, b):
        return (b**4 - a**4)/4 - (b-a)

def apply(f, a, b, J):
    print("f =", f.f)
    integr(a, b, f, J)
    print()

def integr(a, b, f, J):
    print("Точный интеграл:", J)
    I = (b-a)*f(a)
    print("Левый прямоугольник:", I,", погрешность: ", abs(round(I - J, 14)))
    I = (b-a)*f(b)
    print("Правый прямоугольник:", I, ", погрешность: ", abs(round(I - J, 14)))
    I = (b-a)*f((a+b)/2)
    print("Средний прямоугольник:", I, ", погрешность: ", abs(round(I - J, 14)))
    I = ((b-a)/2)*(f(a)+f(b))
    print("Трапеция:", I, ", погрешность: ", I - J)
    I = (f(a)+4*f((a+b)/2)+f(b))*(b-a)/6
    print("Симпсона:", I, ", погрешность: ", abs(round(I - J, 14)))
    h = (b - a) / 3
    (b-a)*((1/8)*f(a) + (3/8)*f(a+h)+(3/8)*f(a+2*h) + (1/8)*f(b))
    print("3/8:", I, ", погрешность: ", abs(round(I - J, 14)))

if __name__ == '__main__':
    print("Приближённое вычисление интеграла по квадратурным формулам")

    func = function()
    func0 = function0()
    func1 = function1()
    func2 = function2()
    func3 = function3()

    a = float(input("Введите начало отрезка: "))
    b = float(input("Введите конец отрезка: "))

    apply(func, a, b, func.integr(a, b))
    apply(func0, a, b, func0.integr(a, b))
    apply(func1, a, b, func1.integr(a, b))
    apply(func2, a, b, func2.integr(a, b))
    apply(func3, a, b, func3.integr(a, b))