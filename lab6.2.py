from math import sin, cos, sqrt
import scipy.integrate as integrate


def func(x):
    return cos(x)*sin(x)

def middle_rectangle(f):
    a = 0
    b = 1
    m = 100000
    h = (b-a)/m
    Im = 0
    for i in range(0, m - 1):
        Im += h * f(a + (i + 1 / 2) * h)
    return Im


if __name__ == '__main__':
    print('Вычисление интеграла при помощи КФ типа Гаусса c 2-мя узлами')
    N = 2
    moments = []
    moments.append(middle_rectangle(lambda x: cos(x)))
    moments.append(middle_rectangle(lambda x: cos(x)*x))
    moments.append(middle_rectangle(lambda x: cos(x)*x**2))
    moments.append(middle_rectangle(lambda x: cos(x)*x**3))

    print("Моменты весовой функции cos(x):")
    for i in range(4):
        print('moment', i, ': ', moments[i])

    a1 = (moments[0]*moments[3] - moments[2]*moments[1])/(moments[1]**2 - moments[0]*moments[2])
    a2 = (moments[2]**2 - moments[3]*moments[1])/(moments[1]**2 - moments[0]*moments[2])

    print('Ортогональный многочлен: x^2 ' + str(a1) + '*x + ' + str(a2))

    x1 = (-a1 + sqrt(a1**2 - 4*a2))/2
    x2 = (-a1 - sqrt(a1**2 - 4*a2))/2

    A1 = (moments[1] - x2*moments[0])/(x1-x2)
    A2 = (moments[1] - x1*moments[0])/(x2-x1)

    print('Узлы и коэффициенты КФ:')
    print('x1 = ', x1, '  A1 = ', A1)
    print('x2 = ', x2, '  A2 = ', A2)

    print('Сумма коэффициентов:', A1 + A2)

    print('Проверка для f = x^3')
    print('Интеграл по КФ:', A1*(x1**3) + A2*(x2**3))
    print('Интеграл через мат. пакет:', integrate.quad(lambda x: cos(x)*x**3, 0, 1))

    print('Интеграл для f = sin(x):', A1*sin(x1) + A2*sin(x2))




