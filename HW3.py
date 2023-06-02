#Задача1
import math
from typing import List, Any


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)
    return distance

# Пример использования функции
x1 = 1
y1 = 2
x2 = 4
y2 = 6

result = distance(x1, y1, x2, y2)
print("Расстояние между точками:", result)


#Задача2

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

lst = []
n = int(input("Введите количество элементов в списке: "))

for i in range(n):
    element = int(input("Введите элемент: "))
    lst.append(element)

reversed_lst = reverse_list(lst)
print(reversed_lst)

#Задание2 Вар2
def reverse_list(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst

# Пример использования функции
my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print(reversed_list)


#Задание4

for num in range(0, 501):
    if num % 7 == 0 and '8' in str(num):
        print(num)


#Задание5

def more_than_five(lst):
    result = []
    for num in lst:
        if abs(num) > 10:
            result.append(num)
    return result

lst = []
n = int(input("Введите количество элементов в списке: "))

for i in range(n):
    element = int(input("Введите элемент: "))
    lst.append(element)

result = more_than_five(lst)
print("Результат:", result)


#Задание6

def get_transactions(t):
    transactions = {}
    total_spent = 0

    for transaction in t:
        if transaction == 'print_it':
            for trans_type, count in transactions.items():
                print(f"{count} - {trans_type}: {count * 1000}")
            return

        phone, trans_data = transaction.split('-')
        trans_type, amount = trans_data.split(':')

        if trans_type in transactions:
            transactions[trans_type] += 1
        else:
            transactions[trans_type] = 1

        total_spent += int(amount)

    print(f"Total transactions: {len(t)}")
    print(f"Total spent: {total_spent}")
    print("Transactions by type:")
    for trans_type, count in transactions.items():
        print(f"{count} - {trans_type}")

transactions = [
    '111111111-перевод:1000',
    '222222222-платеж:500',
    '111111111-перевод:2000',
    '333333333-платеж:700',
    'print_it'
]

get_transactions(transactions)

#Задание7

def roman():
    global one, two, three

    # Считываем два числа
    one = int(input("Введите первое слагаемое: "))
    two = int(input("Введите второе слагаемое: "))

    # Вычисляем сумму
    three = one + two

    # Преобразуем числа в римскую запись
    roman_one = convert_to_roman(one)
    roman_two = convert_to_roman(two)
    roman_three = convert_to_roman(three)

    # Выводим результат
    print(f"{one} в римской записи: {roman_one}")
    print(f"{two} в римской записи: {roman_two}")
    print(f"Сумма {one} и {two} в римской записи: {roman_three}")

# Функция для преобразования числа в римскую запись
def convert_to_roman(num):
    roman_values = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
        90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    roman = ''
    for value, symbol in roman_values.items():
        while num >= value:
            roman += symbol
            num -= value

    return roman

# Пример использования функции
roman()


#Задание8

def discount_checker(threshold, *purchases):
    exceeding_customers = []

    for i, purchase in enumerate(purchases, start=1):
        if purchase > threshold:
            exceeding_customers.append(i)

    return exceeding_customers

threshold = int(input("Введите пороговое значение: "))
purchases = []

n = int(input("Введите количество покупателей: "))
for i in range(n):
    purchase = float(input(f"Введите сумму покупок покупателя {i+1}: "))
    purchases.append(purchase)

result = discount_checker(threshold, *purchases)
print("Номера покупателей с превышением пороговой суммы:", result)


#Задача9

def solve_sudoku(matrix):
    # Находим первую незаполненную позицию
    row, col = find_empty_position(matrix)

    # Если все позиции заполнены, значит судоку решено
    if row == -1 and col == -1:
        return True

    # Перебираем числа от 1 до 4
    for num in range(1, 5):
        # Проверяем, можно ли поместить число в текущую позицию
        if is_valid_move(matrix, row, col, num):
            # Помещаем число в текущую позицию
            matrix[row][col] = num

            # Рекурсивно вызываем функцию для следующей позиции
            if solve_sudoku(matrix):
                return True

            # Если рекурсивный вызов не привел к решению, отменяем выбор числа
            matrix[row][col] = 0

    # Если не удалось найти допустимое число, судоку неразрешимо
    return False

def find_empty_position(matrix):
    # Поиск первой незаполненной позиции
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return i, j

    # Если все позиции заполнены, возвращаем -1, -1
    return -1, -1

def is_valid_move(matrix, row, col, num):
    # Проверка, можно ли поместить число в данную позицию

    # Проверка вертикали
    for i in range(4):
        if matrix[i][col] == num:
            return False

    # Проверка горизонтали
    for j in range(4):
        if matrix[row][j] == num:
            return False

    # Проверка квадрата 2x2
    start_row = (row // 2) * 2
    start_col = (col // 2) * 2

    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if matrix[i][j] == num:
                return False

    return True

matrix = [
    [0, 0, 3, 0],
    [0, 0, 0, 2],
    [2, 0, 0, 0],
    [0, 1, 0, 0]
]

if solve_sudoku(matrix):
    print("Решение найдено:")
    for row in matrix:
        print(row)
else:
    print("Судоку неразрешимо.")
