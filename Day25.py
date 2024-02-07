#Create a program that uses a lambda function to square each element of a list.

A = [1,2,3,4,5,6,7]

def square(inputlist):
    x = lambda a: a * a
    for i in inputlist:
        print(x(int(i)))

square(A)