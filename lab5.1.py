import numpy as np
from math import sin, cos, sqrt

class function:
    f = 'Vx * cos(x^2)'
    def __call__(self, x):
        return sqrt(x)*cos(x**2)


class function5:
    f = 'x^5 + 4'
    def __call__(self, x):
        return x**5+ 4
    def integral(self, x):
        return (x**4)/6 + 4*x

class function7:
    f = 'x^7 - 2x^3 - 1'
    def __call__(self, x):
        return x**7 -2*x**3 - 1
    def integral(self, x):
        return (x**6)/7 + (x**4)/2 -x

class function9:
    f = 'x^9 - 70'
    def __call__(self, x):
        return x**9 - 70
    def integral(self, x):
        return (x**10)/10 - 70*x

def calculate_gauss(func, n, coef, root, a, b):
    print('Функция',func.f)
    print('КФ степени', n)
    integral = 0
    q = (b-a)/(2)
    for i in range(n):
        print('root =', a+q*(root[i]+1), ' A =', q*coef[i])
        integral += q*coef[i]*func(a+q*(root[i]+1))
    return round(integral, 12)

def bisection(ra, rb, pol):
    i = 0
    E = 0.00000000000000012
    while abs(rb-ra) > E:
        i+=1
        x = ra
        bound1 = eval(pol)
        rc = ra+ (rb-ra)/2
        x = rc
        bound2 = eval(pol)
        if bound1*bound2 < 0:
            rb = rc
        else:
            ra = rc
    if (abs(rc) < 0.0000000001):
        rc = 0
    return rc




def legendre(pol):
    for i in range(2, 9):
        el = str((2*i-1)/i) + '*(' + pol[i-1] + ')*x - ' + str((i-1)/i) + '* (' + pol[i-2] + ')'
        pol.append(el)
    return pol


if __name__ == '__main__':
    print('Вычисление интеграла при помощи КФ Гаусса')

    a = -1
    b = 1
    pol = ['1', 'x']
    pol = legendre(pol)

    pol_candidate = []
    for n in range(0, 9):
        h = (b - a) / 100
        x = a
        candidate = []
        for i in range(0, 100):
            bound1 = eval(pol[n])
            x = x+h
            bound2 = eval(pol[n])
            if bound1*bound2 <= 0:
                candidate.append(x - h)
                candidate.append(x)
        pol_candidate.append(candidate)

    pol_roots = []
    for n in range(0, 9):
        roots = []
        candidate = pol_candidate[n]
        for i in range(0, len(candidate)-1, 2):
            roots.append(bisection(candidate[i], candidate[i+1], pol[n]))
        pol_roots.append(roots)


    pol_A = []
    pol_A.append(0)
    for n in range(1, 9):
        A = []
        for i in range(0, len(pol_roots[n])):
            x = pol_roots[n][i]
            p = eval(pol[n-1])
            A.append(2*(1-x**2)/(n*n*p*p))
        pol_A.append(A)

    for n in range(1, 9):
        print('Узлы и коэффициенты КФ Гаусса степени N =', n)
        for i in range(len(pol_roots[n])):
            print('k =', i+1, 'root =', pol_roots[n][i], ' A =', pol_A[n][i])
        print('sum Ak =', round(np.sum(pol_A[n]), 5))
        print()

    func5 = function5()
    print('Значение по КФ:', calculate_gauss(func5, 3, pol_A[3], pol_roots[3], -1, 1))
    print('Tочный интеграл:', func5.integral(1) - func5.integral(-1))
    print()

    func7 = function7()
    print('Значение по КФ:',calculate_gauss(func7, 4, pol_A[4], pol_roots[4], -1, 1))
    print('Tочный интеграл:', func7.integral(1) - func7.integral(-1))
    print()

    func9 = function9()
    print('Значение по КФ:',calculate_gauss(func9, 5, pol_A[5], pol_roots[5], -1, 1))
    print('Tочный интеграл:', func9.integral(1) - func9.integral(-1))
    print()

    func = function()
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))
    for el in [3, 6, 7, 8]:
        print('Значение по КФ:',calculate_gauss(func, el, pol_A[el], pol_roots[el], a, b))
        print()
        print()