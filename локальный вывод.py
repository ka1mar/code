import numpy as np
from scipy.optimize import linprog
from itertools import *

I1 = np.array([[1, -1], [0, 1]])
I0 = np.array([[0, 0], [0, 0]])


def degreeI(n):
    m = n - 1
    In = I1
    for k in range(m):
        In_ = np.copy(In)
        In0 = np.copy(In)
        for (y, x), value in np.ndenumerate(In_):
            In_[y, x] = - (In_[y, x])
        for (y, x), value in np.ndenumerate(In0):
            In0[y, x] = 0
        A = np.hstack((In, In_))
        B = np.hstack((In0, In))
        C = np.vstack((A, B))
        n = n * 2
        In = C
    return In


class ScalarFK:
    def __init__(self, n, Pn):
        self.n = n
        self.Pn = Pn

    type = 'ScalarFK'

    def is_correct_spot_(self):
        if (degreeI(2).dot(self.Pn)).all() > 0:
            return True
        return False


class IntervalFK:
    def __init__(self, n, Pn_m, Pn_p):
        self.n = n
        self.Pn_m = Pn_m
        self.Pn_p = Pn_p
        self.isNarr = [False, np.zeros(1), np.zeros(1)]

    type = 'IntervalFK'

    def is_correct_spot(self):
        print(self.Pn_m, self.Pn_p)
        N = 2 ** self.n
        val = [0, 1]
        perm_set_min = combinations_with_replacement(val, N)
        val = [0, -1]
        perm_set_max = combinations_with_replacement(val, N)

        degreeIn_ = degreeI(self.n)
        for (y, x), value in np.ndenumerate(degreeIn_):
            degreeIn_[y, x] = - (degreeIn_[y, x])


        bnd = list(zip(self.Pn_m, self.Pn_p))
        Pn_m_narr = np.ones(N)
        Pn_p_narr = np.zeros(N)
        for p in perm_set_min:
            min_sol = (linprog(c=p, A_ub=degreeIn_, b_ub=np.zeros(N),
                       bounds=bnd, method="simplex"))
            if not min_sol.success:
                return False


            for i in range(N):
                if Pn_m_narr[i] > min_sol.x[i]:
                    Pn_m_narr[i] = min_sol.x[i]
        for p in perm_set_max:
            max_sol = (linprog(c=p, A_ub=degreeIn_, b_ub=np.zeros(N), bounds=bnd, method="simplex"))
            if not max_sol.success:
                return False
            for i in range(N):
                if Pn_p_narr[i] < max_sol.x[i]:
                    Pn_p_narr[i] = max_sol.x[i]
        if not np.array_equal(Pn_p_narr, self.Pn_p) or not np.array_equal(Pn_m_narr, self.Pn_m):
            self.isNarr = [Pn_m_narr, Pn_p_narr]
        return True, self.isNarr

    def toNarr(self):
        self.Pn_m = self.isNarr[2]
        self.Pn_p = self.isNarr[2]


def probability_spot(L, fk):
    N = 2 ** fk.n
    p_matrix = np.identity(N)
    a = degreeI(fk.n)
    np.transpose(a)
    func = (a.dot(L)).dot(p_matrix)

    degreeIn_ = degreeI(fk.n)
    for (y, x), value in np.ndenumerate(degreeIn_):
        degreeIn_[y, x] = - (degreeIn_[y, x])

    if fk.type == 'IntervalFK':
        bnd = list(zip(fk.Pn_m, fk.Pn_p))
    else:
        bnd = list(zip(fk.Pn, fk.Pn))

    min_sol = (linprog(c=func, A_ub=degreeIn_,
                       b_ub=np.zeros(N), bounds=bnd, method="simplex"))
    if not min_sol.success or min_sol.fun < 0:
        return False
    for x, value in np.ndenumerate(func):
        func[x] = -func[x]

    max_sol = (linprog(c=func, A_ub=degreeIn_,
                       b_ub=np.zeros(N), bounds=bnd, method="simplex"))
    if not max_sol or max_sol.fun > 0:
        return False
    return True, min_sol.fun, -max_sol.fun


A = IntervalFK(2, [1, 0.3, 0.4, 0.2], [1, 0.99, 0.8, 0.7])
B = IntervalFK(2, [1, 0.5, 0.4, 0.6], [1, 0.99, 0.8, 0.7])
C = IntervalFK(2, [1, 0.5, 0.4, 0.3], [1, 0.7, 0.6, 0.2])
D = IntervalFK(2, [1, 0.2, 0.2, 0.3], [1, 0.4, 0.3, 0.4])
E = IntervalFK(2, [1, 0.45, 0.6, 0.55], [1, 0.8, 0.8, 0.7])
print(A.is_correct_spot())
print(B.is_correct_spot())
print(C.is_correct_spot())
print(D.is_correct_spot())
print(E.is_correct_spot())




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
