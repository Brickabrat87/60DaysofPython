#Write a function that takes a list of numbers and returns a new list containing only the even numbers.

def even_list():
    user_input = input("Please enter numbers with ',' as a delimiter: " )
    a = user_input.split(',')
    new_list = []

    for i in a:
        if int(i)%2 == 0:
            new_list.append(i)

    return new_list

print(even_list())