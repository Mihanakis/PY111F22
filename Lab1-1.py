from random import shuffle

"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди - слева списка, соответственно справа - конец.
        """
        self.queue = []

    def enqueue(self, elem: Any) -> None:  # O(N)
        """
        Добавление элемент в конец очереди
        :param elem: Элемент, который должен быть добавлен
        """
        self.queue.append(elem)

    def dequeue(self) -> Any:  # O(N)
        """
        Извлечение элемента из начала очереди.
        :raise: IndexError - Ошибка, если очередь пуста
        :return: Извлеченный с начала очереди элемент.
        """
        if not self.queue:
            raise IndexError("Очередь пуста")
        output = self.queue[0]
        del self.queue[0]
        return output

    def peek(self, ind: int = 0) -> Any:  # O(N)
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.
        :param ind: индекс элемента
        (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)
        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди
        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Индекс не целый")
        if not 0 <= ind <= len(self.queue):
            raise IndexError("Индекс вне границ")
        return self.queue[ind]

    def clear(self) -> None:  # O(N)
        """ Очистка очереди. """
        self.queue.clear()

    def __len__(self):  # O(N)
        """ Количество элементов в очереди. """
        count = 0
        if self.queue:
            for val in self.queue:
                count += 1
        return count

if __name__ == '__main__':
    a = Queue()
    for n in range(10):
        a.enqueue(n)
    shuffle(a.queue)
    print(f"Очередь: {a.queue}, длина очереди: {a.__len__()}")
    for n in range(3):
        print(f"Убираем первый элемент: {a.dequeue()}")
    print(f"Очередь: {a.queue}, длина очереди: {a.__len__()}")
    for n in range(3):
        print(f"Смотрим {n} элемент: {a.peek(n)}")
    print(f"Очередь: {a.queue}, длина очереди: {a.__len__()}")
    print(f"Очищаем очередь")
    a.clear()
    print(f"Очередь: {a.queue}, длина очереди: {a.__len__()}")
