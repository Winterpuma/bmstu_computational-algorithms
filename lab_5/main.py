from math import pow, exp, log
from time import time

from interpolation import *
from integration import integrate
from gauss import Gauss
from dichotomy import dichotomy


Q_data = [[2000,   4000,   6000,   8000,   10000,  12000,  14000,  16000,  18000,  20000,  22000,  24000,  26000],
          [1.0000, 1.0000, 1.0000, 1.0001, 1.0025, 1.0198, 1.0895, 1.2827, 1.6973, 2.4616, 3.3652, 5.3749, 7.6838],
          [4.0000, 4.0000, 4.1598, 4.3006, 4.4392, 4.5661, 4.6817, 4.7923, 4.9099, 5.0511, 5.2354, 5.4841, 5.8181],
          [5.5000, 5.5000, 5.5116, 5.9790, 6.4749, 6.9590, 7.4145, 7.8370, 8.2289, 8.5970, 8.9509, 9.3018, 9.6621],
          [11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000, 11.000],
          [15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000, 15.000]]

EPS = 1e-4

Z_c = [0, 1, 2, 3, 4]
E_c = [12.13, 20.98, 31.00, 45.00]


def F(curr_p):
    return coeff - 2*integrate(0, 1, lambda z: Nt(T(z), curr_p)*z)
    

def T(z):
    return T0 + (Tw - T0)*(z**m)


def find_d_e(T, gamma):
    return [8.61*pow(10, -5)*T*log((1 + Z_c[i+1]*Z_c[i+1]*gamma/2) * (1+gamma/2) /
                (1+Z_c[i]*Z_c[i]*gamma/2)) for i in range(4)]


def find_K(T, d_e):
    Q_i = [interpolate([Q_data[0], Q_data[i+1]], 4, T) for i in range(4)]
    Q_ip1 = [interpolate([Q_data[0], Q_data[i+2]], 4, T) for i in range(4)]

    return [2*2.415*pow(10, -3) * (Q_ip1[i]/Q_i[i]) * pow(T, 3/2) * exp(-(E_c[i]-d_e[i])*11603/T) for i in range(4)]


def gamma_func(gamma, T, X):
    right_part = exp(X[0])/(1+gamma/2)

    for i in range(1, 6):
        right_part += ((exp(X[i])*Z_c[i-1]*Z_c[i-1]) /
                       (1+Z_c[i-1]*Z_c[i-1]*gamma/2))

    return gamma*gamma - right_part*5.87*pow(10, 10)/pow(T, 3)


def Nt(T, P):
    X = [-1, 3, -1, -20, -20, -20]

    while True:
        gamma = dichotomy(0, 3, EPS, lambda cur_gamma: gamma_func(cur_gamma, T, X))
        d_e = find_d_e(T, gamma)
        K = find_K(T, d_e)

        alpha = 0.285*pow(10, -11)*pow(gamma*T, 3)

        system = [[1, -1, 1, 0, 0, 0, log(K[0])+X[1]-X[2]-X[0]],
                  [1, 0, -1, 1, 0, 0, log(K[1])+X[2]-X[3]-X[0]],
                  [1, 0, 0, -1, 1, 0, log(K[2])+X[3]-X[4]-X[0]],
                  [1, 0, 0, 0, -1, 1, log(K[3])+X[4]-X[5]-X[0]],
                  [-exp(X[0]), -exp(X[1]), -exp(X[2]), -exp(X[3]),
                   -exp(X[4]), -exp(X[5]), exp(X[0])+exp(X[1])+exp(X[2])+exp(X[3])+exp(X[4])+exp(X[5])-alpha-P*7243/T],
                  [exp(X[0]), 0, -Z_c[1]*exp(X[2]), -Z_c[2]*exp(X[3]), -Z_c[3]*exp(X[4]), -Z_c[4]*exp(X[5]),
                   Z_c[1]*exp(X[2])+Z_c[2]*exp(X[3])+Z_c[3]*exp(X[4])+Z_c[4]*exp(X[5])-exp(X[0])]]

        d_X = Gauss(system)

        if max([d_X[i]/X[i] for i in range(len(X))]) < 1e-4:
            break
        
        for i in range(len(X)):
            X[i] += d_X[i]
            
    return sum([exp(i) for i in X])

Pn = 0.5#float(input("Pнач: "))
Tn = 300#float(input("Tнач: ")
T0 = 12000#float(input("T0: "))
Tw = 6000#float(input("Tw: "))
m = 12#float(input("m: "))

coeff = 7243 * (Pn / Tn)  

if __name__ == '__main__':
    a = time()
    res_p = dichotomy(2, 25, EPS, F)
    b = time()
    print("Result: ", res_p)
    t = b - a
    

