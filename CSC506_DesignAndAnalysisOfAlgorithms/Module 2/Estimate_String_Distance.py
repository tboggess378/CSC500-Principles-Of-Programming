# Name: Tobias Boggess
# Date: June 25, 2023
# Purpose: Finds the "distance" between two words. Each letter copied cost 5,
# deleted letters cost 20, and inserted letters cost 20.

# calculates the distance between two words
def travel_a_word(original_word, test_word):
    # create list for previous letters and set the distance to zero
    prev_letters = list()
    current_distance = 0
    original_word = original_word.lower()
    test_word = test_word.lower()

    # iterate through the letters in the test word and the original word
    for original_letter, test_letter in zip(original_word, test_word):

        # Store previous letters in the original word
        prev_letters.append(original_letter)

        # compare the current letter in the test word to see if it exists in the original word
        if test_letter not in prev_letters:
            current_distance += 20
        else:
            current_distance += 5

    return current_distance


# driver to run the program
def main():
    word_to_test_against = input('Input word to transform: ')
    word_to_test = input('Input word to create: ')
    distance = travel_a_word(word_to_test_against, word_to_test)
    print(f'Distance: {distance}')


# runs the main program
if __name__ == "__main__":
    main()
