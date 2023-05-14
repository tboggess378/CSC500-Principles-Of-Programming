import os
import time


def display_times(in_directory):
    # Initialized variables to create string tree
    num_tabs = 0
    str_times_tree = f""
    str_tab = f""

    try:
        # Traverse through all the directories and files starting at the given directory
        for (root, dirs, files) in os.walk(in_directory):

            # Add the root directory to the string
            if num_tabs > 0:
                str_times_tree = str_times_tree + f"|\n{str_tab} Directory \"{root}\" created/modified: {time.ctime(os.path.getctime(root))}\n"
            else:
                str_times_tree = str_times_tree + f"{str_tab}Root \"{root}\" created/modified: {time.ctime(os.path.getctime(root))}\n"

            # Each of the following is another subdirectory or file under the root directory
            num_tabs = num_tabs + 1
            str_tab = f"\\{'-' * num_tabs}>"

            # Add each sub-directory to the root directory string
            for directory in dirs:
                d_time = os.path.getctime(os.path.join(in_directory, root, directory))
                str_times_tree = str_times_tree + f"|\n{str_tab} Directory \"{directory}\" created/modified: {time.ctime(d_time)}\n"

            # Add each file in the root directory string
            for file in files:
                f_time = os.path.getctime(os.path.join(in_directory, root, file))
                str_times_tree = str_times_tree + f"|\n{str_tab} File \"{file}\" created/modified: {time.ctime(f_time)}\n"

    # Print if no directory exists under that path
    except FileNotFoundError:
        print(f'Could not find: {in_directory}. Please run program again.')

    # display any errors made besides file not found "should replace with known errors as time goes on"
    except Exception as e:
        print(f'Error: {e}')

    return str_times_tree


def main():
    # Allow for an input string to print the directory tree
    times_str = display_times(input(f'Enter the directory to print the tree first: '))
    print(f"{times_str}")

    # Save the string to an external file
    with open(f'./Sample1.txt', 'w+') as f:
        f.write(times_str)


if __name__ == '__main__':
    main()
