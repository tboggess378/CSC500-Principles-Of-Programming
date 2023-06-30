import random
import timeit


# Partion an array into two
def partition(arr, start_idx, end_idx):
    midpoint = (start_idx + end_idx) // 2
    pivot = arr[midpoint]

    while True:

        # increase index by one if value is smaller than pivot
        while arr[start_idx] < pivot:
            start_idx += 1

        # decrease index by one if value is larger than pivot
        while arr[end_idx] > pivot:
            end_idx -= 1

        if start_idx >= end_idx:
            break

        else:
            # swap values
            temp = arr[start_idx]
            arr[start_idx] = arr[end_idx]
            arr[end_idx] = temp

            # increment/decrement low/high index
            start_idx += 1
            end_idx -= 1

    return end_idx


def quick_sort(arr, low_idx, high_idx):
    if high_idx <= low_idx:
        return

    # call partition to split array
    high = partition(arr, low_idx, high_idx)

    # recursively call until a sorted array
    quick_sort(arr, low_idx, high)
    quick_sort(arr, high + 1, high_idx)


def insertion_sort(arr, len_arr, start_idx, gap):

    # swap values for an array
    for i in range(0, len_arr, gap):
        j = i

        # continue while j is greater than the start index
        while j - gap >= start_idx and arr[j] < arr[j - gap]:

            # swap values in array
            temp = arr[j]
            arr[j] = arr[j - gap]
            arr[j - gap] = temp

            # decrease j by the gap value
            j -= gap


def modified_quick_sort(arr, num_elements, max_allowed_elements):

    # shell sort implementation of insertion sort
    if num_elements < max_allowed_elements:
        # initially start with a gap size = number of elements / 2
        gap_size = num_elements // 2

        # continue to use smaller gap sizes until it reaches a value of 1
        while gap_size >= 1:
            for i in range(gap_size):
                insertion_sort(arr, num_elements, i, gap_size)
            gap_size = gap_size // 2 - 1

    else:
        # call if the number of values is greater than the provided max
        quick_sort(arr, 0, num_elements - 1)


def main():
    # get array and determine max length for insertion sort
    short_arr = random.sample(range(500), 20)
    long_arr = random.sample(range(500), 300)
    max_len_insertion_sort = 25

    # combined quick sort and insertion sort examples
    print(f'Combined Insertion/Quick Sort analysis:')
    print(f'Short Array before sorting: {short_arr}')
    start_short_combined = timeit.default_timer()
    modified_quick_sort(short_arr, 20, max_len_insertion_sort)
    end_short_combined = timeit.default_timer()
    print(f'Short Array after sorting: {short_arr}')

    print(f'\nLong Array before sorting: {long_arr}')
    start_long_combined = timeit.default_timer()
    modified_quick_sort(long_arr, 300, max_len_insertion_sort)
    end_long_combined = timeit.default_timer()
    print(f'Long Array after sorting: {long_arr}')

    # insertion sort examples
    short_arr = random.sample(range(500), 20)
    long_arr = random.sample(range(500), 300)

    print(f'\n\nInsertion sort analysis:')
    print(f'Short Array before sorting: {short_arr}')
    start_short_insertion = timeit.default_timer()
    insertion_sort(short_arr, 20, 1, 1)
    end_short_insertion = timeit.default_timer()
    print(f'Short Array after sorting: {short_arr}')

    print(f'\nLong Array before sorting: {long_arr}')
    start_long_insertion = timeit.default_timer()
    insertion_sort(long_arr, 300, 1, 1)
    end_long_insertion = timeit.default_timer()
    print(f'Long Array after sorting: {long_arr}')

    # quick sort examples
    short_arr = random.sample(range(500), 20)
    long_arr = random.sample(range(500), 300)

    print(f'\n\nQuick Sort analysis:')
    print(f'Short Array before sorting: {short_arr}')
    start_short_quick_sort = timeit.default_timer()
    quick_sort(short_arr, 0, 19)
    end_short_quick_sort = timeit.default_timer()
    print(f'Short Array after sorting: {short_arr}')

    print(f'\nLong Array before sorting: {long_arr}')
    start_long_quick_sort = timeit.default_timer()
    quick_sort(long_arr, 0, 299)
    end_long_quick_sort = timeit.default_timer()
    print(f'Long Array after sorting: {long_arr}')

    print(f'\nAnalysis between the algorithms:')
    print(f'Number of elements in short array: {20}')
    print(f'Number of elements in long array: {300}')
    print(f'Combined Sorting Algorithm short array time: {end_short_combined - start_short_combined}')
    print(f'Combined Sorting Algorithm long array time: {end_long_combined - start_long_combined}')
    print(f'Combined Sorting Algorithm total time: {end_long_combined - start_short_combined}')
    print(f'\nInsertion Sorting Algorithm short array time: {end_short_insertion - start_short_insertion}')
    print(f'Insertion Sorting Algorithm long array time: {end_long_insertion - start_long_insertion}')
    print(f'Insertion Sorting Algorithm total time: {end_long_insertion - start_short_insertion}')
    print(f'\nQuick Sorting Algorithm short time: {end_short_quick_sort - start_short_quick_sort}')
    print(f'Quick Sorting Algorithm long time: {end_long_quick_sort - start_long_quick_sort}')
    print(f'Quick Sorting Algorithm total time: {end_long_quick_sort - start_short_quick_sort}')



if __name__ == "__main__":
    main()
