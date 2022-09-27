


# l = [0, 0, 0, 0]
# n = len(l)

# print(l)
# print()

# for idx in range(n-1):
#     l[idx] = 1

#     print(l)

#     lc = l.copy()

#     for _ in range(n-1):
#         lc.insert(0, lc.pop())
#         print('\t', lc)

# l[n-1] = 1
# print(l)



import math

n = 6

l = [0, ] * n
li = [1, ] * n

ceil = math.floor(n*0.5)
print(ceil)

print()
print(l)
print()

answers = set()
answers.add(tuple(l))

for idx in range(ceil):

    l[idx] = 1
    li[idx] = 0

    print(l)
    answers.add(tuple(l))
    answers.add(tuple(li))

    lc = l.copy()
    lic = li.copy()

    for c in range(n - idx): # n - idx = number of zeros, or number of movements to the right

        print('\t', lc)
        lcc = lc.copy()
        licc = lic.copy()

        for a in range(idx + c, n - 1):

            lcc.insert(a+1, lcc.pop(a))
            licc.insert(a+1, licc.pop(a))

            print('\t\t', lcc)
            answers.add(tuple(lcc))
            answers.add(tuple(licc))


        lc.insert(0, lc.pop())
        lic.insert(0, lic.pop())
        answers.add(tuple(lc))
        answers.add(tuple(lic))


answers.add((1, ) * n)

print(len(answers), 2**n)