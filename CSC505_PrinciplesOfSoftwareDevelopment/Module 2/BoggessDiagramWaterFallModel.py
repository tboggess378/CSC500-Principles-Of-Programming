# Name: Tobias Boggess
# Date: April 30, 2023
# Purpose: Prints the names of the phases for the modified waterfall model
# for a single successful implementation assuming all resources are
# available, requirements have been discovered or mostly discovered
# at the beginning of the project. Future versions may allow for more dynamic
# behavior as outlined in the Boggess Diagram.jpg file found within this folder.

def print_modified_waterfall(diagram_name):

    # Prints the diagram line by line for one project
    if diagram_name in f'Boggess Diagram':
        print(f'Communication')
        print(f'Planning')
        print(f'Communication')
        print(f'Modeling')
        print(f'Planning')
        print(f'Communication')
        print(f'Construction')
        print(f'Planning')
        print(f'Communication')
        print(f'Deployment')
        print(f'Steps for single task deployment: 10')
        return True

    # Display the name of the diagram and determine it was not found
    else:
        print(f'{diagram_name} not found.')
        return False


def main():
    # Used to determine if the user entered a valid diagram name
    successful = False
    num_runs = 0

    # Loop through until the user enters the correct name or until the loop has gone
    # through 5 iterations
    while not successful and num_runs < 5:
        # Get the name of the diagram to print out
        input_path_image = input(f'Input the name of the diagram: ')

        # call to print_modified waterfall
        successful = print_modified_waterfall(input_path_image)

        # gather the number of runs to break out of loop
        num_runs += 1

        if successful:
            print(f'\n\nMatch found. Exiting program.')
            break
        else:
            print(f'\nNo match found. Please input another diagram name.\n')


if __name__ == "__main__":
    main()
