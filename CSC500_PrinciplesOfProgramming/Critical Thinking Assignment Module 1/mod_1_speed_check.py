def main():
    # Values to take user input
    num1 = None
    num2 = None

    # Values to store math operations
    multNums = None
    divNums = None

    try:
        # Takes user input for two numbers
        num1 = int(input('Enter num1: '))
        num2 = int(input('Enter num2: '))

        # Math operations to output
        multNums = num1 * num2
        divNums = num1 / num2

        # Output results from math operations above
        print(f'Result of {num1} * {num2} = {multNums}')
        print(f'Result of {num1} / {num2} = {divNums}')
    except ZeroDivisionError:
        print(f'Result of {num1} * {num2} = {multNums}')
        print('Error: Tried to divide by 0.')
    except ValueError:
        print('Error: Invalid entry.')


if __name__ == "__main__":
    main()
