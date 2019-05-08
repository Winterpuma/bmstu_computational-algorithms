# Аппроксимация ф-и, восстановление ф-и по ее дискретному значению
# Полином Ньютона
# Нахождение корней этим способом. 

from math import cos, radians, ceil

def f(x):
    return cos(radians(90*x)) #cos(x)-x #x*x

def get_array(x_beg, step, amount):
    x_tbl = [x_beg + step*i for i in range(amount)]
    y_tbl = [f(x) for x in x_tbl]
    return x_tbl, y_tbl

def print_table(x, y):
    length = len(x)
    for i in range(length):
        print("%.4f %.4f" % (x[i], y[i]))
    print()

def get_matr(tbl, n):
    for i in range(n):
        tmp = []
        for j in range(n-i):
            tmp.append((tbl[i+1][j] - tbl[i+1][j+1]) / (tbl[0][j] - tbl[0][i+j+1]))
        tbl.append(tmp)
    return tbl

# Choose n dots nearest to x in tbl
def choose_dots(tbl, n, x):
    tbl_len = len(tbl[0])
    i_near = min(range(tbl_len), key = lambda i: abs(tbl[0][i] - x)) # index of nearest value
    space_needed = ceil(n / 2) #amount of max space needed up or down if there is enough space 
    
    if (i_near + space_needed + 1 > tbl_len): # if not enough dots bottomn
        i_end = tbl_len
        i_start = tbl_len - n
    elif (i_near < space_needed): # if not enough dots above
        i_start = 0
        i_end = n
    else:
        i_start = i_near - space_needed + 1
        i_end = i_start + n        

    return [tbl[0][i_start:i_end], tbl[1][i_start:i_end]]
    
def interpolate(tbl, n, x):
    tbl = choose_dots(tbl, n + 1, x)
    matr = get_matr(tbl, n)
    tmp = 1
    res = 0
    for i in range(n+1):
        res += tmp * matr[i+1][0]
        tmp *= (x - matr[0][i])
    return res
        
if __name__ == '__main__':
    x_beg = float(input("Input beginning value of x: "))
    x_step = float(input("Input step for x value: "))
    x_amount = int(input("Input amount of dots: "))

    x_tbl, y_tbl = get_array(x_beg, x_step, x_amount)
    print("\nCreated table:")
    print_table(x_tbl, y_tbl)

    n = int(input("Input n: "))
    x = float(input("Input x: "))

    # Results
    found = interpolate([x_tbl, y_tbl], n, x)
    print("\nInterpolated: ", found)
    print("F(x)        : ", f(x))
    print("Error       : ", abs(f(x) - found), "\n")
    print("Root of this function is: ", interpolate([y_tbl, x_tbl], n, 0))
