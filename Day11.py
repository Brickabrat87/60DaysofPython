#Write a program to print the multiplication table of a given number.

def multiplication_table():
    value = int(input("Please input value:  "))
    final = []
    for i in range(1,13):
        final.append(i*value)
    return final


print(multiplication_table())