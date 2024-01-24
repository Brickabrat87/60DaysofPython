# Write a program to print the first n numbers of a Fibonacci sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


def fibonacci_sequence(n):
    if n == 1:
        fib = [0]
        return fib
    if n == 2:
        fib = [0, 1]
        return fib

    fib = fib = [0, 1]
    for i in range(1, n-1):
        count = fib[i] + fib[i-1]
        fib.append(count)
    return fib

print(fibonacci_sequence(50))

