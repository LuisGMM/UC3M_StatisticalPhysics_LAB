
import math

import time
import timeit



def print_states(N: int) -> None:

    string = ''
    for i in range(int(math.pow(2, N))):
        a = f'{bin(i)[2:].zfill(N)} \t {i.bit_count()}'
        string += a

    open('file.txt', 'w').write(string)


def print_states2(N: int) -> None:
    string = ''.join(
        f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n'
    for i in range(
        int(math.pow(2, N))
        )
    )
    open('file.txt', 'w').write(string)


def print_states2a(N: int) -> None:  # WINNER of vs 1, 2 and 2a
    open('file.txt', 'w').write(
        ''.join(
            f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n'
        for i in range(
            int(math.pow(2, N))
            )
        )
    )


# a = timeit.timeit(lambda: print_states(10), number=100)
# b = timeit.timeit(lambda: print_states2(10), number=100)
# c = timeit.timeit(lambda: print_states2a(10), number=100)

# print(a)
# print(b)
# print(c)

# print(a/b)
# print(b/c)


def print_states2a_inverted(N: int):

    ai = 0b111
    open('file.txt', 'w').write(
        ''.join(
            f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n {bin(i ^ ai)[2:].zfill(N)} \t {(i ^ ai).bit_count()}'
        for i in range(
            int(math.pow(2, N - 1))
            )
        )
    )


# print(timeit.timeit(lambda: print_states2a(21), number=1))
# print(timeit.timeit(lambda: print_states2a_inverted(21), number=1))