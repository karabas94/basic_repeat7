from random import randint

"""
Напишіть функцію, яка обчислює добуток елементів списку цілих. Список передається як параметр.
Отриманий результат повертається із функції.
"""


def multi_list(num_list: list):
    if not num_list:
        raise ValueError('Empty list')
    result = 1
    for num in num_list:
        if not isinstance(num, (int, float)):
            raise ValueError('you must input integer or float value')
        result *= num
    return result


try:
    nums = [randint(1, 5) for _ in range(5)]

    print(f"Input list: {nums}")
    result = multi_list(nums)
    print(f"Result: {result}")

except ValueError as e:
    print(f"Error: {e}")

print('\n')
"""
Напишіть функцію для знаходження мінімуму у списку цілих. Список передається як параметр.
Отриманий результат повертається із функції.
"""
def min_num(num_list: list):
    if not num_list:
        raise ValueError('Empty list')
    for num in num_list:
        if not isinstance(num, (int, float)):
            raise ValueError('Invalid data type, expected int or float')
    return min(num_list)


try:
    nums = [randint(1, 5) for _ in range(5)]
    print(f"Input list: {nums}")
    result = min_num(nums)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Error: {e}")

print('\n')
"""
Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
Отриманий результат повертається із функції.
"""
def prime_num(num_list):
    if not num_list:
        raise ValueError('Empty list')
    count = 0
    for num in num_list:
        if not isinstance(num, (int, float)):
            raise ValueError('Invalid data type, expected int or float')
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
    return count


try:
    nums = [randint(1, 10) for _ in range(9)]
    print(f"Input list: {nums}")
    result = prime_num(nums)
    print(f'Result: {result}')
except ValueError as e:
    print(f'ValueError: {e}')

print('\n')
"""Напишіть функцію, яка видаляє зі списку ціле задане число.
З функції потрібно повернути кількість видаленних елементів.
"""


def remove_num(num_list: list, num: int):
    if not isinstance(num, int):
        raise ValueError('Must be only int for removed number')
    if not num_list or not num:
        raise ValueError('Empty input')
    count = 0
    for i in num_list:
        if not isinstance(i, int):
            raise ValueError('Invalid data type, expected int')
        if num == i:
            num_list.remove(i)
            count += 1
    return count


try:
    nums = [randint(1, 5) for _ in range(5)]
    print(f'Input list: {nums}')
    num_remove = randint(1, 5)
    print(f'Remove number: {num_remove}')
    result = remove_num(nums, num_remove)
    print(f'Result: {result}')
except ValueError as e:
    print(f'ValueError: {e}')

print('\n')
"""
Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.
"""


def new_list(first_list: list, second_list: list):
    if not first_list or not second_list:
        raise ValueError('Empty list')
    new_list = []
    for item in second_list:
        if item in first_list:
            new_list.append(item)
    return list(set(new_list))


try:
    first_list = [randint(1, 5) for i in range(5)]
    second_list = [randint(1, 5) for i in range(5)]
    print(f'First list: {first_list}')
    print(f'Second list: {second_list}')
    result = new_list(first_list, second_list)
    print(f'Result: {result}')
except ValueError as e:
    print(f'ValueError: {e}')

print('\n')
"""
Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих чисел.
Значення для ступеня передається як параметр, список також передається як параметр.
Функція повертає новий список, який містить отримані результати.
"""


def degree_num(*, num_list: list, degree: int):
    if not num_list or not degree:
        raise ValueError('empty data')
    if not isinstance(degree, int):
        raise ValueError('degree must be an integer value')
    new_list = []
    for num in num_list:
        if not isinstance(num, (int, float)):
            raise ValueError('Invalid data type, expected int or float')
        new_list.append(num ** degree)
    return new_list


try:
    nums = [randint(1, 5) for _ in range(5)]
    print(f'Input list: {nums}')
    degree = 2
    print(f'Input degree: {degree}')
    result = degree_num(num_list=nums, degree=degree)
    print(f'Result: {result}')
except ValueError as e:
    print(f'ValueError: {e}')
