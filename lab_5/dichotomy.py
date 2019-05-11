def middle(a, b):
    return (a + b) / 2


def dichotomy(a, b, eps, func):
    c = middle(a, b)

    f_a = func(a)
    f_c = func(c)
    f_b = func(b)

    while abs(f_c) > eps:
        if (f_a * f_c) <= 0:
            b = c
            f_b = func(b)
        elif (f_b * f_c) <= 0:
            a = c
            f_a = func(a)
        else:
            print("Ошибка. Корень не найден.")
            break
        c = middle(a, b)
        f_c = func(c)
        
    return c
