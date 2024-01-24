#Create a program that checks if a year is a leap year.


def leapyeartest():
    try:
        year = int(input("Please insert year:  "))
    except:
        return "Invalid Year format, should be YYYY"


    lytest = year%4
    centurytest = year%100
    if lytest == 0 and centurytest != 0:
        return "heyy!! Leap year!"
    else:
        return "booo nope not Leap year!!"

print(leapyeartest())