#Create a program that sorts a list of strings alphabetically.


def sortlist(inputlist):
    inputlist.sort(reverse=False)
    return inputlist


A = ['z', 'e', 'a', 'b', 'c']
print(sortlist(A))