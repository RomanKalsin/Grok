def find_smallest(arr):
    smallerest = arr[0]
    smallerest_index = 0
    for index, value in enumerate(arr):
        if smallerest > value:
            smallerest = value
            smallerest_index = index
    return smallerest_index
        
def selecion_sort(arr):
    new_arr = []
    i = 0
    while i < len(arr):
        smallerest = find_smallest(arr)
        new_arr.append(arr.pop(smallerest))
    return new_arr
list = [1, 3, 4, 6, 7, 8, 23, 54, 66, 76, 85, 111, 123, 342, 4, 2, 54, 34, 654, 23, 322,]
print(selecion_sort(list))