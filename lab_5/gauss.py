def solve_lin_system_gauss(left_side, right_side):
    n = len(left_side)
    for i in range(0, n):
        for j in range(i+1, n):
            sep = left_side[j][i]/left_side[i][i]
            for k in range(0, n):
                left_side[j][k] -= left_side[i][k] * sep
            right_side[j] -= right_side[i] * sep

    for i in range(n-1, -1, -1):
        for k in range(i+1, n):
            right_side[i] -= left_side[i][k] * right_side[k]
        right_side[i] /= left_side[i][i]

    return right_side

def Gauss(matr):
    n = len(matr)
    # приводим к треугольному виду
    for k in range(n):
        for i in range(k+1,n):
            coeff = -(matr[i][k]/matr[k][k])
            for j in range(k,n+1):
                matr[i][j] += coeff*matr[k][j]
    # находим неизвестные
    a = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            matr[i][n] -= a[j]*matr[i][j]
        a[i] = matr[i][n]/matr[i][i]
    return a
