#Create a program that checks if a year is a leap year.


def leapyeartest():
    try:
        year = int(input("Please insert year:  "))
    except:
        return "Invalid Year format, should be YYYY"

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "heyy!! Leap year!"
    else:
        return "booo nope not Leap year!!"

print(leapyeartest())