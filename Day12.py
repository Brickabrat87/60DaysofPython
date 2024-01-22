# Write a program to reverse a given string.

def reverse_string():
    input_value = input("Input string for reversal:  ")
    rvalue = ''
    if input_value == '':
        return ''
    elif len(input_value) == 1:
        return input_value
    for i in range(len(input_value)):
        rvalue += (input_value[len(input_value) - 1 - i])

    return rvalue

print(reverse_string())
