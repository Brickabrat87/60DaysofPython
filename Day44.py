#Write a program that removes all whitespaces from a given string

a = 'asdfd dfd   dfd fd'
b = ''
a.replace('')

for i in a:
    if i != ' ':
        b += i

def remove_whitespaces(txt):
    return txt.replace(" ", "")