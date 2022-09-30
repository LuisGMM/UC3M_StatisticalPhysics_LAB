
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

# print(timeit.timeit(lambda: print_states2a(10), number=100))
# print(timeit.timeit(lambda: print_states2a_inverted(10), number=100))


def print_states2a_from_to(N: int, from_: int, to: int) -> None:
    return  ''.join(
        f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n'
        for i in range(from_, to)
        )


def print_states2a_return(N: int):
    return ''.join(
            f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n'
            for i in range(
                int(math.pow(2, N))
            )
        )



N = 21
M = 3

states_core = pow(2, N - M)
states = pow(2, N)

# print(states_core)
# print(states)

# for from_, to in zip(range(0, states + 1, states_core), range(states_core, states + 1, states_core)):
#     print_states2a_from_to(N, from_, to)


from joblib import Parallel, delayed


def print_states2a_from_to(N: int, from_: int, to: int) -> None:
    open(f'file_from_{from_}_to_{to}', 'w').write(''.join(
        f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n'
        for i in range(from_, to)
        )
    )



print(timeit.timeit(lambda: Parallel(n_jobs=pow(2, M))(
    delayed(print_states2a_from_to)(N, from_, to)
    for from_, to in zip(
        range(0, states + 1, states_core),
        range(states_core, states + 1, states_core)
        )
    ),
    number=2))

print(timeit.timeit(lambda: print_states2a(N), number=2))
