#Write a Python program to check if two strings are anagrams

def anagram(val1, val2):
    if len(val1) != len(val2):
        return 'Not an anagram'

    check = 0
    for i in val1:
        if i not in val2:
            check += 1

    if check > 1:
        return 'Not an anagram'
    else:
        return 'Guess what an anagram!!'

print(anagram('ant', 'net'))
