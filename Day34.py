#Write a Python program to merge two dictionaries

A = {'a': 1, 'b': 2}
B = {'c': 1, 'd': 2, 'a': 1}

for i in B.items():
    A.update({i})
    print(A)

