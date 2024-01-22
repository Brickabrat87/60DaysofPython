# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def calculate_upper_lower():
    value = input("Please write something:  ")
    upper = 0
    lower = 0
    for i in value:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return f"Upper character count:  {upper}, Lower character count:  {lower}"

print(calculate_upper_lower())

