#Write a program that reads an integer from the user and handles invalid inputs

userinput = input("Please use a freaking number:  ")
try:
    print(int(userinput))
except:
    print("yeaaa that ain't it")