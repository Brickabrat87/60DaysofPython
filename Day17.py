#Create a program that capitalizes the first letter of each word in a sentence


def capitalize_first_letter(userinput):
    output = ''
    for i in range(0, len(userinput)):

        if i == 0 :
            output += userinput[i].upper()
        elif userinput[i-1] == ' ':
            output += userinput[i].upper()
        elif i == ' ':
            output += userinput[i]
        else:
            output += userinput[i]

    return output

u1 = input("Sentence to capitalize:  ")
print(capitalize_first_letter(u1))