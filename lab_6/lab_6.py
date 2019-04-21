# Дифференцирование
# Односторонние левые, правые производные, центральные разности
# Формулы повышенной точности на краях, формулы Рунге, выравнивающие переменные

from math import e, log

def f(x):
    return e**x

def psi(y):
    return log(y)


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


def Runge_center(y, h, r):
    n = len(y)
    p = 2
    
    ksi_h = [(y[i + 1] - y[i - 1]) / (2*h) for i in range(0, n-2)]
    ksi_rh = [(y[i + r] - y[i - r]) / (2*h*r) for i in range(0, n-2)]
    
    return [None if  i >= n - 2
            else (ksi_h[i] + (ksi_h[i] - ksi_rh[i]) / (r**p - 1)) 
            for i in range(0, n)]


def Runge_one_side(y, h, r):
    n = len(y)
    p = 1
    
    ksi_h = [(y[i + 1] - y[i]) / (h) for i in range(0, n-2)]
    ksi_rh = [(y[i + r] - y[i]) / (h*r) for i in range(0, n-2)]
    
    return [None if  i >= n - 2
            else (ksi_h[i] + (ksi_h[i] - ksi_rh[i]) / (r**p - 1)) 
            for i in range(0, n)]


def aline(y, h):
    eta = [psi(i) for i in y]
    l = Runge_one_side(eta, h, 2)
    return [None if l[i] == None else l[i]*y[i] for i in range(len(l))]


def print_res_line(text, res):
    print("{:<20}".format(text), end = "")
    for i in res:
        if (i != None):
            #print("%5.4f" % (i), end = " ")
            print("{: <15.4f}".format(i), end = "")
        else:
            print("{: <15}".format("None"), end = "")
    print()

    
x_start = 0
x_h = 1
x_amount = 11
x, y = get_table(x_start, x_h, x_amount)

r = 2

print_res_line("x:", x)
print_res_line("y:", y)
print_res_line("Left side:", left_side_diff(y, x_h))
print_res_line("Center differences:", center_diff(y, x_h))
print_res_line("Edges accurate:", edge_accuracy(y, x_h))
print_res_line("Runge side:", Runge_one_side(y, x_h, r))
print_res_line("Runge center:", Runge_center(y, x_h, r))
print_res_line("Alining:", aline(y, x_h))
