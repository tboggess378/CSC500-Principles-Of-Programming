import numpy as np


def main():
    # Gets the target number to sum from user
    target_number = int(input('Enter target number: \n'))

    # Creates random array of integers
    arr1 = np.random.randint(1, target_number, size=5)
    arr2 = np.random.randint(1, target_number, size=5)
    arr3 = np.random.randint(1, target_number, size=5)

    try:
        # Iterates through 3 arrays to find sums that will equate to target number
        found_value = False
        for i in range(arr1.size):
            for j in range(arr2.size):
                for k in range(arr3.size):
                    if (arr1[i] + arr2[j] + arr3[k]) == target_number:
                        print(f'{arr1[i]} + {arr2[j]} + {arr3[k]} = {target_number}')
                        found_value = True

        if not found_value:
            print('No values found.')

    except ValueError:
        raise 'Invalid character entered.'


if __name__ == '__main__':
    main()
