# Аппроксимация ф-и
# Наилучшее среднеквадратичное значение
import matplotlib.pyplot as plt
import numpy as np

def f(x_arr, coeff):
    res = np.zeros(len(x_arr))
    for i in range(len(coeff)):
        res += coeff[i]*(x_arr**i)
    return res                   

### Считать данные с файла
def read_from_file(filename):
    f = open(filename, "r")
    x, y, ro = [], [], []
    for line in f:
        line = line.split(" ")
        x.append(float(line[0]))
        y.append(float(line[1]))
        ro.append(float(line[2]))
    return x, y, ro

def print_table(x, y, ro):
    length = len(x)
    print("x      y      ro")
    for i in range(length):
        print("%.4f %.4f %.4f" % (x[i], y[i], ro[i]))
    print()

def print_matr(matr):
    for i in matr:
        print(i)

### Вычислить значение
def root_mean_square(x, y, ro, n): #n - кол-во искомых коэффициентов
    length = len(x)
    sum_x_n = [sum([x[i]**j*ro[i] for i in range(length)]) for j in range(n*2 -1)]
    sum_y_x_n = [sum([x[i]**j*ro[i]*y[i] for i in range(length)]) for j in range(n)]
    matr = [sum_x_n[i:i+n] for i in range(n)]
    for i in range(n):
        matr[i].append(sum_y_x_n[i])
    print_matr(matr)
    return Gauss(matr)

def Gauss(matr):
    n = len(matr)
    # приводим к треугольному виду
    for k in range(n):
        for i in range(k+1,n):
            coeff = -(matr[i][k]/matr[k][k])
            for j in range(k,n+1):
                matr[i][j] += coeff*matr[k][j]
    print("\ntriangled:")
    print_matr(matr)
    # находим неизвестные
    a = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            matr[i][n] -= a[j]*matr[i][j]
        a[i] = matr[i][n]/matr[i][i]
    return a
    

### Отобразить результат
def show(a):
    t = np.arange(-1.0, 5.0, 0.02)
    plt.figure(1)
    plt.ylabel("y")
    plt.xlabel("x")
    plt.plot(t, f(t, a), 'k')
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'ro', markersize=ro[i]+2)
    plt.show()

x, y, ro = read_from_file("data2.txt")
n = 2 # Степень многочлена    
print_table(x, y, ro)
a = root_mean_square(x, y, ro, n+1)
print("\na:", a)
show(a)
