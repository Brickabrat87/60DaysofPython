def findMaxSum(A: List[int], N: int, K: int) -> int:
    current_sum = sum(A[:K])
    answer = current_sum

    for i in range(K, N):
        current_sum = current_sum + A[i] - A[i - K]
        answer = max(answer, current_sum)

    return answer

#Python program to find n-th stair
# using step size 1 or 2 or 3.

# Returns count of ways to reach n-th
# stair using 1 or 2 or 3 steps.


def findStep(n):
	if ( n == 0 ):
		return 1
	elif (n < 0):
		return 0

	else:
		return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)


# Driver code
n = 4
print(findStep(n))

# This code is contributed by Nikita Tiwari.


