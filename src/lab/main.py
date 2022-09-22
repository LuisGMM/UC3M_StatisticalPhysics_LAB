
from __future__ import annotations


class Factorial:

    def __init__(self, n: int):

        if not isinstance(n, int):
            raise TypeError('n must be an integer')

        self.n = set(x for x in range(2, n + 1))

    def __div__(self, other: Factorial):
        
