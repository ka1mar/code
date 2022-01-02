from math import sin, cos
import numpy as np

class funcion:
    f = 'cos(x)*sin(x)'
    def __call__(self, x):
        return cos(x)*sin(x)


def calculate_gauss(func, n, coef, root, a, b, h):
    integral = 0
    q = h/2
    for i in range(n):
        integral += q*coef[i]*func(a+q*(root[i]+1))
    return integral


def legendre(pol):
    for i in range(2, 9):
        el = str((2*i-1)/i) + '*(' + pol[i-1] + ')*x - ' + str((i-1)/i) + '* (' + pol[i-2] + ')'
        pol.append(el)
    return pol


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


if __name__ == '__main__':
    print('Вычисление интеграла при помощи составной КФ Гаусса')
    func = funcion()
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


    N = int(input("Введите N<9: "))
    m = int(input("Введите m: "))

    print('Узлы и коэффициенты КФ Гаусса степени N =', N)

    for i in range(len(pol_roots[N])):
        print('k =', i + 1, 'root =', pol_roots[N][i], ' A =', pol_A[N][i])

        a = 0
        b = 1
        h = (b-a)/m
        j = a
        res = 0
        while(j<b):
            res += calculate_gauss(func, N, pol_A[N], pol_roots[N], j, j+h, h)
            j = round(j + h, 5)

    print('Вычисленное значение интеграла:', res)



