#Bubble sort
def bubble_sort(array):
    n = len(array)
    for  i in range(n):
        swapped = False
        for j in range(n-i-1):
            yield array, j
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
                yield array, j
        if not swapped:
            break

#Merge sort wrapper
def merge_sort(array):
    yield from _merge_sort(array, 0, len(array) - 1)

#Actual merge sort
def _merge_sort(array, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    yield from _merge_sort(array, left, mid)
    yield from _merge_sort(array, mid + 1, right)
    yield from _merge(array, left, mid, right)

#Helper merge function
def _merge(array, left, mid, right):
    left_copy = array[left:mid + 1]
    right_copy = array[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            array[k] = left_copy[i]
            i += 1
        else:
            array[k] = right_copy[j]
            j += 1

        yield array, k
        k += 1

    while i < len(left_copy):
        array[k] = left_copy[i]
        i += 1
        yield array, k
        k += 1

    while j < len(right_copy):
        array[k] = right_copy[j]
        j += 1
        yield array, k
        k += 1

#QuickSort wrapper method 
def quick_sort(array):
    yield from _quick_sort(array, 0, len(array) - 1)

#Actual quick sort
def _quick_sort(array, low, high):
    if low >= high:
        return

    pivot_index = yield from _partition(array, low, high)

    yield from _quick_sort(array, low, pivot_index - 1)
    yield from _quick_sort(array, pivot_index + 1, high)

#Helper method
def _partition(array, low, high):
    pivot = array[high]
    i = low

    for j in range(low, high):
        if array[j] < pivot:
            if i != j:
                array[i], array[j] = array[j], array[i]
                yield array, i
            i += 1
    if i != high:
        array[i], array[high] = array[high], array[i]
        yield array, i

    return i

#SelectionSort 
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        yield array, min_index

        for j in range(i + 1, n):
            yield array, j
            if array[j] < array[min_index]:
                min_index = j
                yield array, min_index

        array[i], array[min_index] = array[min_index], array[i]
        yield array, i

#InsertionSort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        yield array, i
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            yield array, j+1
        array[j + 1] = key
        yield array, j+1



