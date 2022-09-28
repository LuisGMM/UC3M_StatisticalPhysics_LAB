
# import math

# n = 6

# l = [0, ] * n
# li = [1, ] * n

# ceil = math.floor(n*0.5)
# print(ceil)

# print()
# print(l)
# print()

# answers = set()
# answers.add(tuple(l))

# for idx in range(ceil):

#     l[idx] = 1
#     li[idx] = 0

#     print(l)
#     answers.add(tuple(l))
#     answers.add(tuple(li))

#     lc = l.copy()
#     lic = li.copy()

#     for c in range(n - idx):  # n - idx = number of zeros, or number of movements to the right

#         print('\t', lc)
#         lcc = lc.copy()
#         licc = lic.copy()

#         for a in range(idx + c, n - 1):

#             lcc.insert(a+1, lcc.pop(a))
#             licc.insert(a+1, licc.pop(a))

#             print('\t\t', lcc)
#             answers.add(tuple(lcc))
#             answers.add(tuple(licc))

#         lc.insert(0, lc.pop())
#         lic.insert(0, lic.pop())
#         answers.add(tuple(lc))
#         answers.add(tuple(lic))


# answers.add((1, ) * n)

# print(len(answers), 2**n)



def permute(l: list, idx: int, a):
    """_summary_

    Parameters
    ----------
    l : list
        List to permute in place.
    idx : int
        Last '1' position in the ordered list.
        Example [1, 1, 0, 0, 0] -> idx=1
    """

    for i in range(len(l)-idx-1 - a):  # equivalent to the number of zeros minus the ones to the right of idx element
        l.insert(idx+(i+1), l.pop(idx+i))
        print('\t\t', l)


def combine(l: list, idx: int):

    idx_to_permute = idx

    lc = l.copy()
    for i in range(idx+1):  # equivalent to the number of ones minus 1
        print('\t', lc)
        permute(lc, idx-i, i)

        # l.insert(idx+(i+1), l.pop(idx+i))


# l = [1, 1, 1, 1, 0, 0, 0]

# for i in range(3, len(l)-1):
#     print(l)
#     combine(l, i)
#     l.insert(0, l.pop())
# print(l)



l = [0, ] * 3


for idx in range(len(l)):
    l[idx] = 1
    print(f'{l =}')

    lc = l.copy()
    for i in range(idx, len(l)-1):
        print(lc)
        combine(lc, i)
        lc.insert(0, lc.pop())