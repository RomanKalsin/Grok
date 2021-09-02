def find_smallest(arr): # Поиск наименьшего элемента массива
    smallerest = arr[0] # Наименьшее значение 
    smallerest_index = 0 # Индекс наименьшего значения 
    for index, value in enumerate(arr): 
        if smallerest > value: # Если наименьшее значение больше получнного
            smallerest = value # Наименьшим становится полученное
            smallerest_index = index # Индекс нового наименьшего значения
    return smallerest_index
        
def selecion_sort(arr):
    new_arr = []
    i = 0
    while i < len(arr):
        smallerest = find_smallest(arr)
        new_arr.append(arr.pop(smallerest)) # Удаляем наименьший элемент и тарого массива и добавляем в новый
    return new_arr
