
def sortIntegers(array):
    if not array:
        return []
    return quicksort(array, 0, len(array) - 1)

def quicksort(array, start, end):
    if start >= end:
        return
    
    left, right = start, end
    pivot = array[(start + end) // 2]

    left, right = partition(array, left, right, pivot)
    quicksort(array, start, right)
    quicksort(array, left, end)

    return array


def partition(array, left, right, pivot):
    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1
        
        while left <= right and array[right] > pivot:
            right -= 1
        
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    
    return [left, right]

print(sortIntegers([1, 3, 100000, 2, 5]))
    