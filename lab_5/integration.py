# Исправить метод интегрирования/заменить на новый
def integrate(start, end, function):
    step = 0.05#(end - start)/20
    result = 0

    while start <= end:
        left = function(start)
        start += step
        right = function(start)

        result += step*(left + right)/2

    return round(result, 4)
