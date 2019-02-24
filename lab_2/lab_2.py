# Аппроксимация ф-и, восстановление ф-и по ее дискретному значению
# Сплайны

from math import cos

def f(x):
    return x*x

def get_table(x_beg, step, amount):
    x_tbl = [x_beg + step*i for i in range(amount)]
    y_tbl = [f(x) for x in x_tbl]
    return x_tbl, y_tbl

def print_table(x, y):
    length = len(x)
    for i in range(length):
        print("%.4f %.4f" % (x[i], y[i]))
    print()


x_beg = float(input("Input beginning value of x: "))
x_step = float(input("Input step for x value: "))
x_amount = int(input("Input amount of dots: "))

x_tbl, y_tbl = get_array(x_beg, x_step, x_amount)
print("\nCreated table:")
print_table(x_tbl, y_tbl)

n = int(input("Input n: "))
x = float(input("Input x: "))

