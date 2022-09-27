
from __future__ import annotations

import itertools
import math
from typing import Union


class Num(float):

    def __new__(self, *args, **kwargs):
        return float.__new__(self, *args, **kwargs)

    def __truediv__(self, __x: Union[float, Factorial]) -> Num:

        if isinstance(__x, float) or isinstance(__x, int):
            return Num(super().__truediv__(__x))

        return Num(super().__truediv__(__x.value()))

    def __mul__(self, __x: Union[float, Factorial]) -> Num:

        if isinstance(__x, float) or isinstance(__x, int):
            return Num(super().__mul__(__x))

        return Num(super().__mul__(__x.value()))


class Factorial:

    def __init__(self, n: int):

        if not isinstance(n, int):
            raise TypeError('n must be an integer')

        self.n: set = set(x for x in range(2, n + 1))

    def __mul__(self, other: Union[Factorial, Num]):

        if isinstance(other, Factorial):
            return Num(self.value() * other.value())

        return other * self.value()

    def __truediv__(self, other: Factorial):

        if isinstance(other, Factorial):
            return Num(math.prod(self.n.difference(other.n)))

        return other / self.value()

    def value(self) -> Num:

        if getattr(self, '__value', None) is None:
            self.__value = Num(math.prod(self.n))

        return self.__value




# question1 and 2

# microstates = (1, 0)
# states = 5
# possible_states = set()

# for i in itertools.combinations_with_replacement(microstates, states):

#     possible_states.add(i)

#     k = sum(i)
#     combinations = int(math.perm(states, k) / math.factorial(k))

#     if combinations == 6:
#         continue

#     for j in itertools.permutations(i, combinations):
#         possible_states.add(j)


# for i in itertools.combinations_with_replacement(microstates, states):
#     possible_states.update(itertools.permutations(i, states))



#question4

import matplotlib.pyplot as plt


def n_over_k(n, k):

    # fn = Factorial(n)
    # fk = Factorial(k)

    # fnk = Factorial(n-k)

    # return (fn/fk) / fnk if k > (n-k) else (fn/fnk) / fk

    return math.perm(n, k) / math.factorial(k)

n = 10
k = 4

# print(n_over_k(n, k))
# print(int(math.perm(n, k) / math.factorial(k)))


def plot_for_n(n):

    states = tuple(range(0, n + 1))
    combinations = tuple(n_over_k(n, k) for k in states)

    fig, ax = plt.subplots()

    ax.plot(states, combinations)

    plt.show()


# plot_for_n(33)
# plot_for_n(66)
# plot_for_n(100)


# ----------------------------------------------------------------


# Probabilities and Entropy


import statistics

nia_alfonso = int('100429848'[-2:])
nia_daniel = int('100452279'[-2:])
nia_alvaro = int('100454417'[-2:])
nia_luis = int('100454766'[-2:])


M = statistics.mean([nia_alfonso, nia_daniel, nia_alvaro, nia_luis])
N = int(100 + M) # TODO: is this adequate?


def p(k, N=N):
    return n_over_k(N, k) / math.pow(2, N)


# question1
print(p(10))

# question2

hN = int(N/2)
print(p(hN))

# question3
print(p(hN + 5) - p(hN - 5))

# question4
print(p(hN + 25) - p(hN - 25))

# questio5
kb = 1.380649e-23 #m2 kg s-2 K-1

def s(states):
    return kb * math.log(states)

states1 = n_over_k(hN + 10)
states2 = n_over_k(hN)

print(abs(s(states1) - s(states2)))

# questio6
states1 = n_over_k(hN + 5)
states2 = n_over_k(hN)
print(abs(s(states1) - s(states2)))

# questio7
states1 = n_over_k(hN)
states2 = n_over_k(2)
print(abs(s(states1) - s(states2)))


# questio9

p1 = p(hN)
p2 = p(M)

print(p1/p2)
