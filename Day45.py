#Write a function to check if a number is a prime number

a = 13
count = 0

for i in range(2, a):
    if a%i == 0:
        count += 1
if count != 0:
    print("value isn't prime")
else:
    print("Value is prime")


