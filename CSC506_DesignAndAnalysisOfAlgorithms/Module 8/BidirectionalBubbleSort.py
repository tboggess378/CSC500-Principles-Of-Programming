# Name: Tobias Boggess
# Date: August 3, 2023
# Purpose: Create a bubble sort variation algorithm
import copy
import timeit
import random


# Code inspired/from www.geeksforgeeks.org/cocktail-sort/
def bidirectional_bubble_sort(arr):
    # get length of array, start index, end index, and indication of a swap occurring
    arr_copy = copy.deepcopy(arr)
    arr_length = len(arr_copy)
    start = 0
    end = arr_length - 1
    any_swaps = True

    # Start timer
    start_time = timeit.default_timer()
    # Continue until array is sorted
    while any_swaps:
        any_swaps = False

        # swap pieces of array from start to end
        for i in range(start, end):
            if arr_copy[i] > arr_copy[i + 1]:
                arr_copy[i], arr_copy[i + 1] = arr_copy[i + 1], arr_copy[i]
                any_swaps = True

        # break if array is sorted
        if not any_swaps:
            break

        # value at end should be max value of array
        end -= 1

        # swap pieces but from end to start
        for j in range(end - 1, start - 1, -1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                any_swaps = True

        # increment start as min should be at beginning of array
        start += 1

    # end timer and record length of time taken with various arrays
    end_time = timeit.default_timer()
    time_taken = end_time - start_time

    return arr_copy, time_taken


def bubble_sort(arr):
    # make copy of array
    arr_copy = copy.deepcopy(arr)

    # Timer for normal bubble sort
    start_time = timeit.default_timer()

    # sorts array by swapping values
    for i in range(len(arr_copy)):
        for j in range(0, len(arr_copy) - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]

    # end timer and compute time taken to complete operations
    end_time = timeit.default_timer()
    time_taken = end_time - start_time

    return arr_copy, time_taken


def main():
    # create single array of random value from 0 to 10000
    arr = [random.randint(1, 10000) for _ in range(10)]

    # Short array with 10 elements
    print(f'Short array: {arr}')
    bi_bubble_arr, bi_bubble_time = bidirectional_bubble_sort(arr)
    bubble_arr, bubble_time = bubble_sort(arr)
    print(f'Short array sorted: {bi_bubble_arr}')
    print(f'Short array sorted: {bubble_arr}')
    print(f'\nBidirectional Bubble Sort Time: {bi_bubble_time}')
    print(f'Bubble Sort Time: {bubble_time}')

    # Medium array with 500 elements
    medium_arr = [random.randint(1, 10000) for _ in range(500)]
    medium_bi_bubble_arr, medium_bi_bubble_time = bidirectional_bubble_sort(medium_arr)
    medium_bubble_arr, medium_bubble_time = bubble_sort(medium_arr)
    print(f'Medium length Bidirectional Bubble Sort Time: {medium_bi_bubble_time}')
    print(f'Medium length Bubble Sort Time: {medium_bubble_time}')

    # Long array with 1000 elements
    long_arr = [random.randint(1, 10000) for _ in range(1000)]
    long_bi_bubble_arr, long_bi_bubble_time = bidirectional_bubble_sort(long_arr)
    long_bubble_arr, long_bubble_time = bubble_sort(long_arr)
    print(f'Long length Bidirectional Bubble Sort Time: {long_bi_bubble_time}')
    print(f'Long length Bubble Sort Time: {long_bubble_time}')


if __name__ == '__main__':
    main()
