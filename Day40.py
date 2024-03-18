#Write a function to find the largest common divisor of two numbers using a function

def largestcommondenominator(a,b):
    divisor = []
    divisorupdate = []
    if b/a > 0:
        if b%a == 0:
            print(a)
        for i in reversed(range(1, a)):
            if a%i == 0:
                divisor.append(i)
        for i in reversed(range(1, a)):
            if b%i == 0 and i in divisor:
                divisorupdate.append(i)


    if a/b > 0:
        if a%b == 0:
            print(b)
        for i in reversed(range(1, b)):
            if a%i == 0:
                divisor.append(i)
        for i in reversed(range(1, b)):
            if a%i == 0 and i in divisor:
                divisorupdate.append(i)

    return f"Max common denominator of value1 - {a} and value2- {b} is: {divisorupdate[0]}"

print(largestcommondenominator(9,30))
