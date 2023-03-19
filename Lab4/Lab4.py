from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    # создадим начальную матрицу, проход по первой вертикали и горизонталь всегда один, мы не возвращаемся назад
    field = [[1] * n] * m

    # пройдём по всему полю, игнорируя первую (нулевую) вертикаль и горизонталь,
    # впишем в каждую из следующих клеток сумму 3-х значений - прохода от предыдущих значений
    # по вертикали, диагонали и горизонтали
    for i in range(1, m):
        for j in range(1, n):
            field[i][j] = field[i][j - 1] + field[i - 1][j] + field[i - 1][j - 1]
    return field


if __name__ == '__main__':
    paths = car_paths(5, 5)
    print(paths[-1][-1])  # 7
