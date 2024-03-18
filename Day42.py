#Write a program that uses a try-except block to handle division by zero

def yourknowlege():
    a = input("Please enter numberator:  ")
    b = input("Please enter denommenator:  ")
    try:
        print(a/b)
    except:
        print("you can't divide by 0 fool!!")

yourknowlege()
