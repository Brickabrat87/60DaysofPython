# Write a program to count the occurrences of a specific character in a string.

def occurrence(value):
    result = {}
    counter = 1

    for values in value:
        if values in result:
            result[values] = counter + 1
        else:
            result[values] = counter

    for key, value in result.items():
        print(f"Character:  {key}, Occurrences:  {value} ")


user_input = input("Please type anything: ")
test = user_input.count('a')
print(test)
#occurrence(user_input)