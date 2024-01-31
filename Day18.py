#Create a program to find the largest among three numbers.

def find_largest():
    output = []
    for i in range(0,3):
        try:
            userinput = int(input(f"Number {i+1}:  " ))
            output.append(userinput)
        except Exception as e:
            # By this way we can know about the type of error occurring
            print("The error is: ", e)

    return max(output)


print(find_largest())



