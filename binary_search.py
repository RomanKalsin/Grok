def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

list = [1, 3, 4, 6, 7, 8, 23, 54, 66, 76, 85, 111, 123, 342]
print(binary_search(list, 4))