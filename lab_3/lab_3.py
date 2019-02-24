# Аппроксимация ф-и, восстановление ф-и по ее дискретному значению
# Многомерная интерполяция

def f(x, y):
    return x**2 + y**2

# x_h, y_h - step
# x_n, y_n - amount
def get_matrix(x_beg, x_h, x_n, y_beg, y_h, y_n):
    x = [x_beg + i*x_h for i in range(x_n)]
    y = [y_beg + i*y_h for i in range(y_n)]
    z = [[f(i, j) for i in x] for j in y]
    return x, y, z

# Choose n dots nearest to x in a
def choose_dots(a, n, x):
    a_len = len(a)
    i_near = min(range(tbl_len), key = lambda i: abs(a[i] - x)) # index of nearest value
    space_needed = ceil(n / 2)
    
    if (i_near + space_needed + 1 > tbl_len):
        i_end = a_len
        i_start = a_len - n
    elif (i_near < space_needed):
        i_start = 0
        i_end = n
    else:
        i_start = i_near - space_needed + 1
        i_end = i_start + n        

    return i_start, i_end

# n - polynom's power
def newtons_interpolation(tbl, n, x):
    tbl = choose_dots(tbl, n + 1, x)
    matr = get_matr(tbl, n)
    tmp = 1
    res = 0
    for i in range(n+1):
        res += tmp * matr[i+1][0]
        tmp *= (x - matr[0][i])
    return res

x_beg = float(input("Input beginning value of x: "))
x_h = float(input("Input step for x value: "))
x_N = int(input("Input amount of dots: "))

y_beg = float(input("Input beginning value of y: "))
y_h = float(input("Input step for y value: "))
y_N = int(input("Input amount of dots: "))

x, y, z = get_matrix(x_beg, x_h, x_N, y_beg, y_h, y_N)
print("\nCreated matrix:")
#print_matrix(x_tbl, y_tbl)

x_n = int(input("Input n(x): "))
x_find = float(input("Input x: "))

y_n = int(input("Input n(y): "))
y_find = float(input("Input y: "))

# Results
'''
found = interpolate([x_tbl, y_tbl], n, x)
print("\nInterpolated: ", found)
print("F(x)        : ", f(x))
print("Error       : ", abs(f(x) - found), "\n")
print("Root of this function is: ", interpolate([y_tbl, x_tbl], n, 0))
'''
