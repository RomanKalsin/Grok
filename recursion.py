def fact(num): # Поиск факториала числа
    if num == 0: # Базовый случай число 0
        return 1
    elif num == 1: # Базовый случай число 1
        return 1
    else:
        return num * fact(num - 1) 

def sum_arr(arr): # Сумма элементов массива
    if arr == []: # Базовый случай массив пустой
        return 0
    else:
        return arr[0] + sum_arr(arr[1:]) # Прибавляем первый элемент к рекрсивному случаю со срезом массива начиная с индекса 1

def count_arr(arr): # Колличество элементов массива
    if arr == []: # Базовый случай массив пустой
        return 0
    else:
        return 1 + count_arr(arr[1:]) # Прибавляем 1 к рекрсивному случаю со срезом массива начиная с индекса 1

def max(arr): # Поиск большего числа в массиве
    if len(arr) == 2: # Базовый случай если в массиве осталось два элемента
        return arr[0] if arr[0] > arr[1] else arr[1] # Сравниваем два последних элемента массива
    max_num = max(arr[1:]) # Рекурсивный случай срез массива начаиная с индекса 1 
    return arr[0] if arr[0] > max_num else max_num # Сравнимаем первый элемент массива в текушем стеке вызова с переменной max