import random
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        rand = random.randrange(0, len(arr))
        pivot = arr[rand]
        arr.remove(pivot)
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)