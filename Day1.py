#Create a program that swaps the values of two variables.

def swap(firstValue, secondValue):
    newSecondValue = firstValue
    newFirstValue = secondValue
    print("First Value:  ", firstValue)
    print("Second Value: ", secondValue)
    print("Original order:  ", firstValue, secondValue)
    print("First and Second Value swapping.....")
    print("Swapped Values: ", newFirstValue, newSecondValue)

swap('Brittany', 'McNair')