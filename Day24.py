#Write a program to remove vowels from a given string.

vowels = 'aeiouAEIOU'

value = 'Hi, my name is Brittany McNair'

new_value = ''

for i in value:
    if i not in vowels:
        new_value += i

print(new_value)