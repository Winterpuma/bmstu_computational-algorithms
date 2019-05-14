def middle(a, b):
    return (a + b) / 2


def dichotomy(a, b, eps, func):
    c = middle(a, b)

    f_a = func(a)
    f_c = func(c)
    f_b = func(b)

    if (f_a * f_b) > 0:
        print("Функция не меняет знак на концах отрезка.")
        return None
    
    while abs(b - a) > eps*c + eps:
        if (f_a * f_c) <= 0:
            b = c
            f_b = func(b)
        else:
            a = c
            f_a = func(a)
            
        c = middle(a, b)
        f_c = func(c)
        
    return c
    
