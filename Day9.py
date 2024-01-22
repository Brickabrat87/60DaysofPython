#Write a program to check if a number is even or odd.


def check_even_or_odd():
    response = int(input("Please enter number:  "))
    if response%2 == 0:
        return "Value is even!"
    else:
        return "Value is odd!"


print(check_even_or_odd())