# Write a program to remove duplicates from a list.

def remove_duplicates(values):
    new_list = []
    for i in values:
        if new_list.count(i) == 0:
            new_list.append(i)
    return new_list


A = [1, 3, 4, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 6, 4, 1]

print(type(set(A)))
