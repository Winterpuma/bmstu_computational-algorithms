# Аппроксимация ф-и
# Наилучшее среднеквадратичное значение

# Считать данные с файла
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

# Вычислить значение
# Отобразить результат

x, y, ro = read_from_file("data.txt")
print_table(x, y, ro)
