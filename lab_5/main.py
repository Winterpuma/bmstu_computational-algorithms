from math import pow, exp, log
from time import time
from numpy.linalg import solve

from interpolation import *
from integration import integrate
from gauss import solve_lin_system_gauss


Q_data = [[2000,   4000,   6000,   8000,   10000,  12000,  14000,  16000,  18000,  20000,  22000,  24000,  26000],
          [1.0000, 1.0000, 1.0000, 1.0001, 1.0025, 1.0198, 1.0895, 1.2827, 1.6973, 2.4616, 3.3652, 5.3749, 7.6838],
          [4.0000, 4.0000, 4.1598, 4.3006, 4.4392, 4.5661, 4.6817, 4.7923, 4.9099, 5.0511, 5.2354, 5.4841, 5.8181],
          [5.5000, 5.5000, 5.5116, 5.9790, 6.4749, 6.9590, 7.4145, 7.8370, 8.2289, 8.5970, 8.9509, 9.3018, 9.6621],
          [11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000],
          [15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000]]

P_mind = 2
P_maxd = 25
EPS = 1e-4

Z_c = [0, 1, 2, 3, 4]
E_c = [12.13, 20.98, 31.00, 45.00]

def F(curr_p):
    return coeff - 2*integrate(0, 1, lambda z: Nt(T(z), curr_p)*z)
    

def middle(a, b):
    return (a + b) / 2


def T(z):
    return T0 + (Tw - T0)*(z**m)


def find_d_e(T, gamma):
    return [8.61*pow(10, -5)*T*log((1 + Z_c[i+1]*Z_c[i+1]*gamma/2) * (1+gamma/2) /
                (1+Z_c[i]*Z_c[i]*gamma/2)) for i in range(4)]


def find_K(T, d_e):
    K = []
    for i in range(4):
        Q_ip1 = interpolate([Q_data[0], Q_data[i+2]], 4, T)
        Q_i = interpolate([Q_data[0], Q_data[i+1]], 4, T)
        K_i = 2*2.415*pow(10, -3) * (Q_ip1/Q_i) * pow(T, 3/2) * exp(-(E_c[i]-d_e[i])*11603/T)

        K.append(K_i)

    return K


def gamma_func(gamma, T, X):
    right_part = exp(X[0])/(1+gamma/2)

    for i in range(1, 6):
        right_part += ((exp(X[i])*Z_c[i-1]*Z_c[i-1]) /
                       (1+Z_c[i-1]*Z_c[i-1]*gamma/2))

    right_part *= 5.87*pow(10, 10)/pow(T, 3)

    return gamma*gamma - right_part


def find_gamma(st, end, T, X):
    while abs(st-end) > EPS:
        cur_gamma = (st+end)/2

        if gamma_func(cur_gamma, T, X) <= 0:
            st = cur_gamma
        else:
            end = cur_gamma

    return (st+end)/2


def find_max_increment(X, d_X):
    max_inc = abs(d_X[0]/X[0])
    for i in range(1, len(X)):
        if abs(d_X[i]/X[i]) > max_inc:
            max_inc = abs(d_X[i]/X[i])
    return max_inc


def Nt(T, P):#, X):
    X = [-1, 3, -1, -20, -20, -20]
    #X = [10, 10, 10, -1, -1, -1]

    while True:
        gamma = find_gamma(0, 3, T, X)
        d_e = find_d_e(T, gamma)
        K = find_K(T, d_e)

        lin_sys_left_side = [[1, -1, 1, 0, 0, 0],
                             [1, 0, -1, 1, 0, 0],
                             [1, 0, 0, -1, 1, 0],
                             [1, 0, 0, 0, -1, 1],
                             [-exp(X[0]), -exp(X[1]), -exp(X[2]), -exp(X[3]), -exp(X[4]), -exp(X[5])],
                             [exp(X[0]), 0, -Z_c[1]*exp(X[2]), -Z_c[2]*exp(X[3]), -Z_c[3]*exp(X[4]), -Z_c[4]*exp(X[5])]]

        alpha = 0.285*pow(10, -11)*pow(gamma*T, 3)

        lin_sys_right_side = [log(K[0])+X[1]-X[2]-X[0],
                              log(K[1])+X[2]-X[3]-X[0],
                              log(K[2])+X[3]-X[4]-X[0],
                              log(K[3])+X[4]-X[5]-X[0],
                              exp(X[0])+exp(X[1])+exp(X[2])+exp(X[3])+exp(X[4])+exp(X[5])-alpha-P*7243/T,
                              Z_c[1]*exp(X[2])+Z_c[2]*exp(X[3])+Z_c[3]*exp(X[4])+Z_c[4]*exp(X[5])-exp(X[0])]

        d_X = solve_lin_system_gauss(lin_sys_left_side, lin_sys_right_side)
        #d_X = solve(lin_sys_left_side, lin_sys_right_side) # ~30% быстрее

        if find_max_increment(X, d_X) < EPS:
            break

        for i in range(len(X)):
            X[i] += d_X[i]
    # print([exp(i) for i in X], gamma)
    return sum([exp(i) for i in X])


        
if __name__ == '__main__':
    a = 2
    b = 25

    X = [-1, 3, -1, -20, -20, -20]

    Pn = 0.5#float(input("Pнач: "))
    Tn = 300#float(input("Tнач: ")
    T0 = 3000#8000#float(input("T0: "))
    Tw = 3000#2000#float(input("Tw: "))
    m = 6#float(input("m: "))

    coeff = 7243 * (Pn / Tn)
    time_start = time()

    c = middle(a, b)

    f_a = F(a)
    f_c = F(c)
    f_b = F(b)

    while abs(f_c) > EPS:
        if (f_a * f_c) <= 0:
            b = c
            f_b = F(b)
        elif (f_b * f_c) <= 0:
            a = c
            f_a = F(a)
        else:
            print("Ошибка. Корень не найден.")
            break
        c = middle(a, b)
        f_c = F(c)
        
    print("Result: ", c)

    time_end = time()

    print("Time req: ", time_end - time_start)

    # # print(t(0, T0, Tw, m))
    # for i in range(1000, 10001, 1000):
    #     Nt(t(0, i, Tw, m), 5)
    #     print(t(0, i, Tw, m))'''

