
def sortIntegers(array):
    if not array:
        return []
    temp = [] # merge sort O(n) space complexity due to creating a new array
    
    return mergesort(array, 0, len(array) - 1, temp)

def mergesort(array, start, end, temp):
    if start >= end:
        return
    
    left, right = start, end
    mid = (start + end) // 2
    
    mergesort(array, start, mid, temp)
    mergesort(array, mid + 1, end, temp)
    merge(array, start, mid, end, temp)


def merge(array, start, end, temp):
    mid = (start + end) // 2
    left, right = start, mid + 1
    index = start

    while left <= mid and right <= end:
        if array[left] < array[right]:
            temp[index] = array[left]
            left += 1
        else:
            temp[index] = array[right]
            right += 1
        index += 1

    while left <= mid:
        temp[index] = array[left]
        left += 1
        index += 1
    
    while right <= end:
        temp[index] = array[right]
        right += 1
        index += 1
    
    for index in range(start, end + 1):
        array[index] = temp[index]
    
    return array
    

print(sortIntegers([1, 3, 100000, 2, 5]))