# Name: Tobias Boggess
# Date: May 21, 2023
# Purpose: Displays the actors within the diagram and the use case scenarios associated

def print_use_cases(actor):
    # initialize use cases and empty contents
    use_cases = []

    # Gather use cases for each actor
    if actor == f'citizen':
        # possible use cases for citizens based on diagram
        use_cases = [f'Set username',
                     f'Create Login',
                     f'Set/Change password, security questions, profile information',
                     f'Report Pothole',
                     f'Update Pothole Information',
                     f'Close request']

    elif actor == f'database':
        # Use cases for the database
        use_cases = [f'Update queue/Priority of request',
                     f'Determine number of crew, cost, equipment, and material',
                     f'Update request order depending on citizen information or city official',
                     f'Setup connection with actor',
                     f'Timeout/Request reload of page']

    elif actor == f'user_interface':
        # Use cases for the user interface
        use_cases = [f'Report time for work completed',
                     f'Report progress of work on pothole',
                     f'Display relevant information to other actors']

    else:
        print(f'No actor found associated with diagram.')

    print(f'\tUse Cases:')
    # Print use cases
    for case in use_cases:
        print(f'\t\t{case}')


def print_actors():
    # actors in diagram
    actors = [f'citizen', f'database', f'user_interface']

    # iterate through actors and print related use cases
    for actor in actors:
        print(f'Actor: {actor}')
        print_use_cases(actor)


def print_description():
    # Description for the format of actors and their associated use cases
    print(f'Displays some use cases for each actor in the following format.')
    print(f'Actor: <actor>')
    print(f'\tUse Cases: <use case>, <use case>, <use case>, ...\n\n')


def main():
    print_description()
    print_actors()


if __name__ == "__main__":
    main()
