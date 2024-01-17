# Write a program to check if a number is positive, negative, or zero.

def number_check(number):
    if number == 0:
        return "Number is 0"
    elif number < 0:
        return "Number is negative"
    elif number > 0:
        return "Number is positive"


value = int(input("Please input number:  "))

print(number_check(value))