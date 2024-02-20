#Write a test case for a function that checks if a number is prime

def prime(n):
    if n%2 != 0:
        return 'Prime Number'
    else:
        return 'Prime'

print(prime(9))