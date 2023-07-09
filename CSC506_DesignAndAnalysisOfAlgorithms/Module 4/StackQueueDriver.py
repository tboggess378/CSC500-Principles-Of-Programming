from QueueUsingLinkedList import QueueUsingLinkedList
from QueueUsingPythonList import QueueUsingPythonList
from StackUsingPythonList import StackUsingPythonList
from StackUsingLinkedList import StackUsingLinkedList
import random
import timeit


def compareQueue():
    # Initialize queues using both linked list and python list
    queueUsingLinks = QueueUsingLinkedList()
    queueUsingLists = QueueUsingPythonList()

    # arrays to keep track of times
    start_link_push_times = [None] * 10
    stop_link_push_times = [None] * 10
    start_list_push_times = [None] * 10
    stop_list_push_times = [None] * 10

    start_link_pop_times = [None] * 5
    stop_link_pop_times = [None] * 5
    start_list_pop_times = [None] * 5
    stop_list_pop_times = [None] * 5

    # append 10 value to queues
    for i in range(10):
        randNum = random.randrange(50)
        start_link_push_times[i] = timeit.default_timer()
        queueUsingLinks.push(randNum)
        stop_link_push_times[i] = timeit.default_timer()

        start_list_push_times[i] = timeit.default_timer()
        queueUsingLists.push(randNum)
        stop_list_push_times[i] = timeit.default_timer()

    # pop five values to get a good number of times queues pop values
    for i in range(5):
        start_link_pop_times[i] = timeit.default_timer()
        queueUsingLinks.pop()
        stop_link_pop_times[i] = timeit.default_timer()

        start_list_pop_times[i] = timeit.default_timer()
        queueUsingLists.pop()
        stop_list_pop_times[i] = timeit.default_timer()

    # Print analytics for queues
    print(f'Queue LinkedList Push Times: ')
    for j in range(len(start_link_push_times)):
        print(f'{stop_link_push_times[j] - start_link_push_times[j]}', end=' ')

    print(f'\nQueue ArrayList Push Times: ')
    for j in range(len(start_list_push_times)):
        print(f'{stop_list_push_times[j] - start_list_push_times[j]}', end=' ')

    print(f'\nQueue LinkedList Pop Times: ')
    for j in range(len(start_link_pop_times)):
        print(f'{stop_link_pop_times[j] - start_link_pop_times[j]}', end=' ')

    print(f'\nQueue ArrayList Pop Times: ')
    for j in range(len(start_list_pop_times)):
        print(f'{stop_list_pop_times[j] - start_list_pop_times[j]}', end=' ')

    print()


def compareStack():
    # Initialize queues using both linked list and python list
    stackUsingLinks = StackUsingLinkedList()
    stackUsingLists = StackUsingPythonList()

    # arrays to keep track of times
    start_link_push_times = [None] * 10
    stop_link_push_times = [None] * 10
    start_list_push_times = [None] * 10
    stop_list_push_times = [None] * 10

    start_link_pop_times = [None] * 5
    stop_link_pop_times = [None] * 5
    start_list_pop_times = [None] * 5
    stop_list_pop_times = [None] * 5

    # append 10 value to queues
    for i in range(10):
        randNum = random.randrange(50)
        start_link_push_times[i] = timeit.default_timer()
        stackUsingLinks.push(randNum)
        stop_link_push_times[i] = timeit.default_timer()

        start_list_push_times[i] = timeit.default_timer()
        stackUsingLists.push(randNum)
        stop_list_push_times[i] = timeit.default_timer()

    # pop five values to get a good number of times queues pop values
    for i in range(5):
        start_link_pop_times[i] = timeit.default_timer()
        stackUsingLinks.pop()
        stop_link_pop_times[i] = timeit.default_timer()

        start_list_pop_times[i] = timeit.default_timer()
        stackUsingLists.pop()
        stop_list_pop_times[i] = timeit.default_timer()

    # Print analytics for queues
    print(f'\n\nStack LinkedList Push Times: ')
    for j in range(len(start_link_push_times)):
        print(f'{stop_link_push_times[j] - start_link_push_times[j]}', end=' ')

    print(f'\nStack ArrayList Push Times: ')
    for j in range(len(start_list_push_times)):
        print(f'{stop_list_push_times[j] - start_list_push_times[j]}', end=' ')

    print(f'\nStack LinkedList Pop Times: ')
    for j in range(len(start_link_pop_times)):
        print(f'{stop_link_pop_times[j] - start_link_pop_times[j]}', end=' ')

    print(f'\nStack ArrayList Pop Times: ')
    for j in range(len(start_list_pop_times)):
        print(f'{stop_list_pop_times[j] - start_list_pop_times[j]}', end=' ')

    print()


def main():
    compareQueue()
    compareStack()


if __name__ == '__main__':
    main()
