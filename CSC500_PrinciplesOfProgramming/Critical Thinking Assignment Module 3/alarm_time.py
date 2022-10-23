def main():
    # Get current time, number of hours to wait for alarm to go off,
    # the time it will be after the alarm
    current_time = int(input('Enter current time (in hours -> i.e., 24 hour time format): \n'))
    hours_to_wait = int(input('Enter number of hours to wait (in hours):\n'))
    time_after_alarm = (current_time + hours_to_wait) % 24

    # Shows current time, number of hours to wait, time after alarm hours
    # time should be in 24-hour format
    print(f'You entered {current_time} hours.')
    print(f'You wanted to wait {hours_to_wait} hours for alarm.')
    print(f'Alarm will go off at {time_after_alarm}.')


if __name__ == '__main__':
    main()

