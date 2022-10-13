
import math
import timeit
from joblib import Parallel, delayed


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


def print_states2a_from_to(N: int, from_: int, to: int) -> None:
    return  ''.join(
        f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n'
        for i in range(from_, to)
        )


N = 20
M = 3


states_core = pow(2, N - M)
states = pow(2, N)


def print_states2a_from_to_write(N: int, from_: int, to: int) -> None:
    open(f'file_from_{from_}_to_{to}', 'w').write(
        ''.join(
            f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n'
            for i in range(from_, to)
        )
    )


def parallel_job():

    Parallel(n_jobs=pow(2, M))(
    delayed(print_states2a_from_to_write)(N, from_, to)
    for from_, to in zip(
        range(0, states + 1, states_core),
        range(states_core, states + 1, states_core)
        )
    )

# print(timeit.timeit(parallel_job, number=1))

# print(timeit.timeit(lambda: print_states2a(N), number=1))

# print(timeit.timeit(lambda: parallel_job(), number=1))


def print_states2a_inverted(N: int):

    ai = 0b111
    (
        ''.join(
            f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n {bin(i ^ ai)[2:].zfill(N)} \t {(i ^ ai).bit_count()}'
            for i in range(
                int(math.pow(2, N - 1))
            )
        )
    )



def generate_states(N):

    for i in range(int(math.pow(2, N))):
        yield f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n'


def save_states(N):
    with open('states.txt', 'w') as f:
        f.writelines(generate_states(N))


def generate_states_from_to(N: int, from_: int, to: int) -> None:

    for i in range(from_, to):
        f'{bin(i)[2:].zfill(N)} \t {i.bit_count()} \n'


def save_states_from_to(N, from_, to):

    with open(f'file_from_{from_}_to_{to}', 'w') as f:
        f.writelines(generate_states_from_to(N, from_, to))




def parallel_save_states_from_to(N, M):

    states_core = pow(2, N - M)
    states = pow(2, N)

    Parallel(n_jobs=pow(2, M))(
    delayed(save_states_from_to)(N, from_, to)
    for from_, to in zip(
        range(0, states + 1, states_core),
        range(states_core, states + 1, states_core)
        )
    )



def parallel_generate_states_from_to(N, M):

    states_core = pow(2, N - M)
    states = pow(2, N)

    Parallel(n_jobs=pow(2, M))(
    delayed(generate_states_from_to)(N, from_, to)
    for from_, to in zip(
        range(0, states + 1, states_core),
        range(states_core, states + 1, states_core)
        )
    )


N = 30
M = 3
# print(timeit.timeit(lambda: parallel_save_states_from_to(N, M), number=1))




N = 33
M = 3
print(timeit.timeit(lambda: parallel_generate_states_from_to(N, M), number=1))
# print(timeit.timeit(lambda: save_states(N), number=1))