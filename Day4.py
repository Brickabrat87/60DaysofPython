# Write a program to find the sum of all elements in a list.

def sum_all_elements(provided_list):
    end_value = 0
    for value in provided_list:
        end_value = value + end_value
    return end_value


elements = [1, 2, 3, 4, 5, 6]
elements1 = [7, 8, 9, 4, 5, 6, 11, 12]

print(sum_all_elements(elements1))
print(sum_all_elements(elements))
