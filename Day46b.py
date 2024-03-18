#Write a function to check if a given list is sorted

A = [1,2,1,3,4,5,6,7]
def check_for_sorted(list):
    if(list == sorted(list)):
        print('Sorted!')
    else:
        print('not sorted')

check_for_sorted([1, 2, 3, 4])
check_for_sorted([8, 4, 6, 1])
def sortedlistcheck(a, b='asc'):
    if b == 'asc':
        for i in range(0, len(A) - 1):
            if A[i] > A[i+1]:
                print('list is not sorted in ascending order')
                break
    if b == 'desc' :
        for i in range(0, len(A) - 1):
            if A[i] < A[i + 1]:
                print('list is not sorted in descending order')
                break

print(sortedlistcheck(A,'asc'))

