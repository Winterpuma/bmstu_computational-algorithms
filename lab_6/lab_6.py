# Дифференцирование
# Односторонние левые, правые производные, центральные разности
# Формулы повышенной точности на краях, формулы Рунге, выравнивающие переменные

from math import e, log

def f(x):
    return e**x

def get_table(x_beg, step, amount):
    x_tbl = [x_beg + step*i for i in range(amount)]
    y_tbl = [f(x) for x in x_tbl]
    return x_tbl, y_tbl

def left_side_diff(y, h):
    return [None if not i
            else ((y[i] - y[i - 1]) / h)
            for i in range(len(y))]

def right_side_diff(y, h):
    return [None if i == len(y) - 1
            else ((y[i + 1] - y[i]) / h)
            for i in range(len(y))]          

def center_diff(y, h):
    return [None if not i or i == len(y) - 1
            else (y[i + 1] - y[i - 1]) / (2*h)
            for i in range(len(y))]

def edge_accuracy(y, h):
    n = len(y)
    a = [None for i in range(n)]
    a[0] = (-3 * y[0] + 4 * y[1] - y[2]) / (2 * h)
    a[n-1] = (y[n - 3] - 4 * y[n - 2] + 3 * y[n - 1]) / (2 * h)
    return a     

def Runge(y, h, r):
    n = len(y)
    ksi_h = [(y[i + 1] - y[i - 1]) / (2*h) for i in range(2, n-2)]
    ksi_rh = [(y[i + r] - y[i - r]) / (2*r*h) for i in range(2, n-2)]
    
    return [None if (i < 0 or i >= n-4)
            else (ksi_h[i] + (ksi_h[i] - ksi_rh[i]) / (r ** 2 - 1))
            for i in range(-2, n - 2)]

def aline(x, y, h):
    eta = [log(i) for i in y]
    l = Runge(eta, h, 2)
    return [None if l[i] == None else l[i]*y[i] for i in range(len(l))]
    
x, y = get_table(0, 1, 11)


