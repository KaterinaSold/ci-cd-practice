def add(a, b):
    """Возвращает сумму двух чисел"""
    return a + b

def subtract(a, b):
    """Возвращает разность двух чисел"""
    return a - b

def multiply(a, b):
    """Возвращает произведение двух чисел"""
    return a * b

def divide(a, b):
    """Возвращает частное двух чисел"""
    if b == 0:
        raise ValueError("Нельзя делить на ноль!")
    return a / b

def factorial(n):
    """Вычисляет факториал числа"""
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result