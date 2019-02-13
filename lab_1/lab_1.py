# Аппроксимация фи-и, восстановление ф-и по ее дискретному значению

from math import cos, radians

def f(x):
    return x*x#cos(radians(90*x))

def get_array(x_beg, step, amount):
    x_tbl = [x_beg + step*i for i in range(amount)]
    y_tbl = [f(x) for x in x_tbl]
    return x_tbl, y_tbl

def print_table(x, y):
    length = len(x)
    for i in range(length):
        print(x[i], y[i])
    print()

def get_matr(tbl, n): #n - кол-во узлов
    for i in range(n-1):
        T = []
        for j in range(n-i-1):
            T.append((tbl[i+1][j] - tbl[i+1][j+1]) / (tbl[0][j] - tbl[0][i+j+1]))
        tbl.append(T)
    return tbl
    
def interpolate(tbl, n, x):
    matr = get_matr(tbl, n)
    tmp = 1
    res = 0
    for i in range(n):
        res += tmp * matr[i+1][0]
        tmp *= (x - matr[0][i])
    return res
        

x_beg = 0#float(input("Input beginning value of x: "))
x_step = 0.25#float(input("Input step for x value: "))
x_amount = 5#int(input("Input amount of dots: "))

x_tbl, y_tbl = get_array(x_beg, x_step, x_amount) 
print_table(x_tbl, y_tbl)

print()
n = 4#int(input("Input n: "))
#x = float(input("Input x: "))
print(interpolate([x_tbl, y_tbl], n+1, 0.6), f(0.6))

