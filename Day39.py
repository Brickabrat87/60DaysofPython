#Write a program to find the most common words in a text file

A = 'Hi Hi my my my my my  name is brittany mcnair'

B = A.split()
keyvalue = {}
c = 0

for i in B:
    if i in keyvalue.keys():
        c = keyvalue[i] + 1
        keyvalue[i] = c
    else:
        keyvalue[i] = 1


maxword = max(keyvalue.values())

value = {i for i in keyvalue if keyvalue[i]== maxword}
print("key by value:",value)
