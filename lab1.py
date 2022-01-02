import numpy as np
from math import log

class function():
    a = -3
    b = 7
    E = 0.00000001
    def __call__(self, x):
        return 2*x**2 - 2**x -5
    def diff(self, x):
        return 4*x - log(2)*2**x

def bisection(f, ra, rb):
    i = 0
    while abs(rb-ra) > f.E:
        i+=1
        rc = ra+ (rb-ra)/2
        if f(ra)*f(rc) < 0:
            rb = rc
        else:
            ra = rc
    print('root= ', rc ,'; ', i, ' steps, last segment length= ', (rb-ra), '  absolute discrepancy=', abs(f(rc)))



def newton(f, x0):
    i = 1
    x = x0 - f(x0)/f.diff(x0)
    while abs(x - x0) > f.E:
        i+=1
        x0 = x
        x = x0 - f(x0)/f.diff(x0)
        if (i>10):
            break
    print('root= ', x ,'; ', i, ' steps, last segment length = ', abs(x-x0), '  absolute discrepancy=', abs(f(x)))


def mod_newton(f, x0):
    i = 1
    x = x0 - f(x0)/f.diff(x0)
    dif_x0 = f.diff(x0)
    while abs(x - x0) > f.E:
        i+=1
        x0 = x
        x = x0 - f(x0)/dif_x0
        if (i>10):
            break
    print('root= ', x ,'; ', i, ' steps, last segment length= ', abs(x-x0), '  absolute discrepancy=', abs(f(x)))

def secant(f, x0):
    i = 1
    x1 = x0 - 0.005
    x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
    while abs(x2 - x1) > f.E:
        i+=1
        x0 = x1
        x1 = x2
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if (i>10):
            break
    print('root= ', x2 ,'; ', i, ' steps, last segment length= ', abs(x2-x1), '  absolute discrepancy=', abs(f(x2)))



if __name__ == '__main__':
    f = function()

    h = (f.b-f.a)/100
    x = f.a
    roots = []
    for i in range(0, 100):
        if f(x)*f(x+h) <= 0:
            roots.append(x)
            roots.append(round(x+h, 1))
        x = round(x+h, 1)

    print()
    print('start:', roots)
    print()
    print('bisection:')
    for i in range(0, len(roots)-1, 2):
       bisection(f, roots[i], roots[i+1])
    print()
    print('newton:')
    for i in range(0, len(roots) - 1, 2):
        newton(f, roots[i])
    print()
    print('mod_newton:')
    for i in range(0, len(roots) - 1, 2):
        mod_newton(f, roots[i])
    print()
    print('secant:')
    for i in range(0, len(roots) - 1, 2):
        secant(f, roots[i])

