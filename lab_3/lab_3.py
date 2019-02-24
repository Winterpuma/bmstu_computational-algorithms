# Аппроксимация ф-и, восстановление ф-и по ее дискретному значению
# Многомерная интерполяция

from math import ceil

def f(x, y):
    return x**2 + y**2

# x_h, y_h - step
# x_n, y_n - amount
def get_matrix(x_beg, x_h, x_n, y_beg, y_h, y_n):
    x = [x_beg + i*x_h for i in range(x_n)]
    y = [y_beg + i*y_h for i in range(y_n)]
    z = [[f(i, j) for i in x] for j in y]
    return x, y, z

def print_matrix(x, y, z):
    print("   y\\x ", end = '')
    for i in x:
        print("{:6}".format(i), end = ' ')
    
    for i in range(len(y)):
        print("\n{:6}".format(y[i]), end = ' ')
        for j in z[i]:
            print("{:6}".format(j), end = ' ')
    print('\n')
            

# Choose n dots nearest to x in a
def choose_dots(a, n, x):
    a_len = len(a)
    i_near = min(range(a_len), key = lambda i: abs(a[i] - x)) # index of nearest value
    space_needed = ceil(n / 2)
    
    if (i_near + space_needed + 1 > a_len):
        i_end = a_len
        i_start = a_len - n
    elif (i_near < space_needed):
        i_start = 0
        i_end = n
    else:
        i_start = i_near - space_needed + 1
        i_end = i_start + n        

    return i_start, i_end

# Matrix of differences 
def get_diff_matr(tbl, n):
    for i in range(n):
        tmp = []
        for j in range(n-i):
            tmp.append((tbl[i+1][j] - tbl[i+1][j+1]) / (tbl[0][j] - tbl[0][i+j+1]))
        tbl.append(tmp)
    return tbl

# n - polynom's power
def newtons_interpolation(tbl, n, x):
    matr = get_diff_matr(tbl, n)
    tmp = 1
    res = 0
    for i in range(n+1):
        res += tmp * matr[i+1][0]
        tmp *= (x - matr[0][i])
    return res

def multi_interpolation(x, y, z, x_val, y_val, x_n, y_n):
    ix_beg, ix_end = choose_dots(x, x_n + 1, x_val)
    iy_beg, iy_end = choose_dots(y, y_n + 1, y_val)

    x = x[ix_beg : ix_end]
    y = y[iy_beg : iy_end]
    z = z[iy_beg : iy_end]
    for i in range(y_n + 1):
        z[i] = z[i][ix_beg : ix_end]

    #print("Choosen dots:"
    #print_matrix(x, y, z)

    res = [newtons_interpolation([x, z[i]], x_n, x_val) for i in range(y_n + 1)]
    return newtons_interpolation([y, res], y_n, y_val)
           

x_beg = float(input("Input beginning value of x: "))
x_h = float(input("Input step for x value: "))
x_N = int(input("Input amount of dots: "))

y_beg = float(input("Input beginning value of y: "))
y_h = float(input("Input step for y value: "))
y_N = int(input("Input amount of dots: "))

x, y, z = get_matrix(x_beg, x_h, x_N, y_beg, y_h, y_N)
print("\nCreated matrix:")
print_matrix(x, y, z)

x_n = int(input("Input n(x): "))
x_find = float(input("Input x: "))

y_n = int(input("Input n(y): "))
y_find = float(input("Input y: "))

# Results
found = multi_interpolation(x, y, z, x_find, y_find, x_n, y_n)
print("\nInterpolated   : ", found)
print("F(x, y)        : ", f(x_find, y_find))
print("Error          : ", abs(f(x_find, y_find) - found), "\n")

