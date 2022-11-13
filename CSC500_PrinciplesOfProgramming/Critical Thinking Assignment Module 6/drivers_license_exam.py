# Name: Tobias Boggess
# Date: 11-14-2022
# Purpose: Reads a text file containing answers from a student
# and compares it to the list of questions with the correct answers
# then outputs number of questions correct, wrong, and displays question
# numbers that were incorrect.

# Reads and puts answers into array of test answers given by student
def readTextFile(answers_file):
    answers = []

    # Reads from file and stores in answers list
    with open(answers_file, 'r') as f:
        lines = f.readlines()

    # Appends answer to answer list
    for line in lines:
        answers.append(line.split()[0].upper())

    return answers


def main():
    # Index can relate to question number
    # List with correct answers to compare from students exam
    correct_answers = 'A C A A D B C A C B A D C A D C B B D A'.split()

    # File to take answers in
    file_name = './answers.txt'
    student_answers = readTextFile(file_name)

    # Arrays to store the indexes of correct and incorrect answers given by student
    wrong = 0
    correct = 0
    wrong_answers = []

    # Checks answers between student and key
    for idx in range(len(student_answers)):
        if correct_answers[idx] == student_answers[idx]:
            correct += 1
        else:
            wrong_answers.append(idx + 1)
            wrong += 1

    # Displays students score (pass or fail), total answered correctly,
    # total answered incorrectly, questions that were wrong
    if correct >= 15:
        print(f'Student passed test!')
    else:
        print(f'Student failed test.')

    print(f'Total Correct: {correct}')
    print(f'Total Incorrect: {wrong}')
    print(f'Questions with wrong answer: ', end=' ')
    for i in wrong_answers:
        print(f'{i}', end=' ')
    print()


if __name__ == '__main__':
    main()