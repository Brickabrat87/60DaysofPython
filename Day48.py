#Create a program that replaces specific words in a text with their synonyms

A = 'Hey, my name is Brittany and I am happy'
syno = {'happy': 'elated', 'Brittany': 'Bmac'}

newword = A.split()
for i in range(len(newword)):
    if newword[i] in syno.keys() :
        newword[i] = syno[newword[i]]

my_string = " ".join(str(element) for element in newword)
print(my_string)
