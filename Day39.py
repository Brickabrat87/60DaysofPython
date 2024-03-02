#Write a program to find the most common words in a text file

A = 'Hi Hi my name is brittany mcnair'

B = A.split()
keyvalue = {}

for i in B:
    if i in keyvalue.keys():
        c = keyvalue[i] + 1
        keyvalue[i] = c
    else:
        keyvalue[i] = 0
    print(keyvalue)

keyvalue.

