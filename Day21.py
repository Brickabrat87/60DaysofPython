#Create a program to remove a specific element from a set.


def remove_element(element,n):
    if len(element) < n+1:
        return 'Location not found!!'
    else:
        element.remove(n)
        return element

a = [1,2,3,4,5,6]

print(remove_element(a,3))
