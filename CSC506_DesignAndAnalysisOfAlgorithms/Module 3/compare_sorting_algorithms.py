# Name: Tobias Boggess
# Date: July 2, 2023
# Purpose: Compose different sorting algorithms to compare to each other based on timeit functions.
import random
import timeit
import math
import copy


def selection_sort(arr):
    # iterate through the input array
    for i in range(len(arr)):
        idx_smallest = i

        # iterate through the rest of the array to find smallest value
        for j in range(i + 1, len(arr)):

            # assign the smallest idx
            if arr[j] < arr[idx_smallest]:
                idx_smallest = j

        # swap values in array
        temp = arr[i]
        arr[i] = arr[idx_smallest]
        arr[idx_smallest] = temp


def insertion_sort(arr, arr_size):
    # initialize variables
    i = j = 0
    temp = 0

    # iterate through input array
    for i in range(arr_size):
        j = i

        # swap each smaller value starting at i
        while j > 0 and arr[j] < arr[j - 1]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp

            j -= 1


def shell_insertion_sort(arr, start_idx, gap):
    # iterate through the input array by gap number
    for i in range(start_idx + gap, len(arr), gap):
        j = i

        # compare values starting at the start index
        while (j - gap >= start_idx) and (arr[j] < arr[j - gap]):
            # swap values and decrease j
            temp = arr[j]
            arr[j] = arr[j - gap]
            arr[j - gap] = temp
            j -= gap


def partition(arr, start_idx, end_idx):
    # find midpoint of input array
    mid_idx = (start_idx + end_idx) // 2
    pivot = arr[mid_idx]

    # look through array to partition and swap
    while True:

        # increment start_idx
        while arr[start_idx] < pivot:
            start_idx += 1

        # decrement end_idx
        while arr[end_idx] > pivot:
            end_idx -= 1

        # stop if input array is already sorted
        if start_idx >= end_idx:
            break

        # swap  values
        else:
            temp = arr[start_idx]
            arr[start_idx] = arr[end_idx]
            arr[end_idx] = temp
            start_idx += 1
            end_idx -= 1

    return end_idx


def quick_sort(arr, start_idx, end_idx):
    # stop once the end idx is less than start idx
    if end_idx <= start_idx:
        return

    # partition list segment
    high = partition(arr, start_idx, end_idx)

    # sort left and right segments
    quick_sort(arr, start_idx, high)
    quick_sort(arr, high + 1, end_idx)


def merge(arr, i, j, k):
    # preallocate the size of the temp array
    size = k - i + 1
    merged = [0] * size

    # determine left, right, and merged position
    position = 0
    left = i
    right = j + 1

    # add elements depending on value in jth position
    while left <= j and right <= k:
        if arr[left] <= arr[right]:
            merged[position] = arr[left]
            left += 1
        else:
            merged[position] = arr[right]
            right += 1

        position += 1

    # add remaining elements from left array to merged array
    while left <= j:
        merged[position] = arr[left]
        left += 1
        position += 1

    # add remaining elements from right array to merged array
    while right <= k:
        merged[position] = arr[right]
        right += 1
        position += 1

    # rearrange elements from the temp array
    for position in range(size):
        arr[i + position] = merged[position]


def merge_sort(arr, i, k):
    # initialize j
    j = 0

    # continue until i is greater than the size of the array
    if i < k:
        j = (i + k) // 2

        merge_sort(arr, i, j)
        merge_sort(arr, j + 1, k)

        merge(arr, i, j, k)


def main():
    # create array with random numbers
    # initial_arr = random.sample(range(10000), 500)

    # make copies of random number array
    SELECTION_SORT_SETUP = '''
import copy
import random
from __main__ import selection_sort
initial_arr = random.sample(range(10000), 500)
selection_copy = copy.deepcopy(initial_arr)
    '''

    SELECTION_SORT_CODE = '''
selection_sort(selection_copy)
    '''

    selection_sort_times = timeit.repeat(setup=SELECTION_SORT_SETUP,
                                         stmt=SELECTION_SORT_CODE,
                                         number=500,
                                         repeat=5)

    INSERTION_SORT_SETUP = '''
import copy
import random
from __main__ import insertion_sort
initial_arr = random.sample(range(10000), 500)
insertion_copy = copy.deepcopy(initial_arr) 
    '''

    INSERTION_SORT_CODE = '''
insertion_sort(insertion_copy, len(insertion_copy))
    '''

    insertion_sort_times = timeit.repeat(setup=INSERTION_SORT_SETUP,
                                         stmt=INSERTION_SORT_CODE,
                                         number=500,
                                         repeat=5)

    SHELL_SORT_SETUP = '''
import copy
import random
from __main__ import shell_insertion_sort
initial_arr = random.sample(range(10000), 500)
shell_insertion_copy = copy.deepcopy(initial_arr)
    '''

    SHELL_SORT_CODE = '''
gap = len(shell_insertion_copy) // 2
while gap > 0:

    for i in range(gap):
        shell_insertion_sort(shell_insertion_copy, i, gap)

    gap = gap // 2
    '''

    shell_sort_times = timeit.repeat(setup=SHELL_SORT_SETUP,
                                     stmt=SHELL_SORT_CODE,
                                     number=500,
                                     repeat=5)

    QUICK_SORT_SETUP = '''
import copy
import random
from __main__ import quick_sort
initial_arr = random.sample(range(10000), 500)
quick_sort_copy = copy.deepcopy(initial_arr)
    '''

    QUICK_SORT_CODE = '''
quick_sort(quick_sort_copy, 0, len(quick_sort_copy)-1)
    '''

    quick_sort_times = timeit.repeat(setup=QUICK_SORT_SETUP,
                                     stmt=QUICK_SORT_CODE,
                                     number=500,
                                     repeat=5)

    MERGE_SORT_SETUP = '''
import copy
import random
from __main__ import merge_sort
initial_arr = random.sample(range(10000), 500)
merge_sort_copy = copy.deepcopy(initial_arr)    
    '''

    MERGE_SORT_CODE = '''
merge_sort(merge_sort_copy, 0, len(merge_sort_copy) - 1)
    '''

    merge_sort_times = timeit.repeat(setup=MERGE_SORT_SETUP,
                                     stmt=MERGE_SORT_CODE,
                                     number=500,
                                     repeat=5)

    print(f'{"Sorting Algorithm":<25s}{"MIN":<15s}{"AVG":<15s}{"MAX":<15s}')
    print(f'{"Selection Sort":<25s}{min(selection_sort_times):<15.6f}', end='')
    print(f'{math.fsum(selection_sort_times) / len(selection_sort_times):<15.6f}', end='')
    print(f'{max(selection_sort_times):<15.6f}')

    print(f'{"Insertion Sort":<25s}{min(insertion_sort_times):<15.6f}', end='')
    print(f'{math.fsum(insertion_sort_times) / len(insertion_sort_times):<15.6f}', end='')
    print(f'{max(insertion_sort_times):<15.6f}')

    print(f'{"Shell Sort":<25s}{min(shell_sort_times):<15.6f}', end='')
    print(f'{math.fsum(shell_sort_times) / len(shell_sort_times):<15.6f}', end='')
    print(f'{max(shell_sort_times):<15.6f}')

    print(f'{"Quick Sort":<25s}{min(quick_sort_times):<15.6f}', end='')
    print(f'{math.fsum(quick_sort_times) / len(quick_sort_times):<15.6f}', end='')
    print(f'{max(quick_sort_times):<15.6f}')

    print(f'{"Merge Sort":<25s}{min(merge_sort_times):<15.6f}', end='')
    print(f'{math.fsum(merge_sort_times) / len(merge_sort_times):<15.6f}', end='')
    print(f'{max(merge_sort_times):<15.6f}')


if __name__ == '__main__':
    main()
