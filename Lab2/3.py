def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError("Факториал считается от целого числа")
    if n < 0:
        raise ValueError("Факториал считается от положительных чисел")
    if n == 0:
        return 1
    if n == 1:
        return 1
    return factorial_recursive(n - 1) * n
