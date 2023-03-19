def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок
    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    queue = []
    for letter in brackets_row:  # O(N)
        if letter in ['(']:  # скобка открылась - добавляем элемент в список
            queue.append(letter)
        if letter in [')']:  # скобка закрылась - убираем последний элемент из списка
            if not queue:  # если список пуст - удалять нечего, False
                return False
            del queue[-1]
    if queue:  # проверка на оставшиеся открытые скобки, если есть - False
        return False
    return True


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets(""))  # True
    print(check_brackets("())(()"))  # False
    print(check_brackets("((())(())"))  # False
