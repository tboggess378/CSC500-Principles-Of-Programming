# Name: Tobias Boggess
# Date: May 14, 2023
# Purpose: Outlines the number of qualities in a good software engineer

# Displays the personality traits of a good software engineer in a chart
def display_personality_traits():
    print(f'Qualities of a Good Software Engineer')
    print(f'\tCommunication --> ', end=' ')
    print(f'honesty, awareness of others, individual responsibility')
    print(f'\tCollaboration --> ', end=' ')
    print(f'honesty, awareness of others')
    print(f'\tIndividual responsibility --> ', end=' ')
    print(f'honesty, awareness of others, taking responsibility for good and bad actions')


def get_number_of_traits():
    return 3, 2, 3


# Call the display_personality_trait
def main():
    # Get the total number of personality traits in each category
    communication_qualities, collaboration_qualities, individual_responsibility_qualities = get_number_of_traits()

    # calculate the total number of qualities
    total_qualities = communication_qualities + collaboration_qualities + individual_responsibility_qualities

    # Print results to console
    print(f'Total Qualities: {total_qualities}')
    print(f'Communication Qualities: {communication_qualities}')
    print(f'Collaboration Qualities: {collaboration_qualities}')
    print(f'Individual Responsibility Qualities: {individual_responsibility_qualities}\n')

    # Print the actual qualities
    display_personality_traits()


# runs the program
if __name__ == "__main__":
    main()
