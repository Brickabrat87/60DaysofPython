#Write a function to count the number of vowels in a given string

def vowel_count(text):
    vowels = 'aeiou'
    count = 0
    for character in text.lower():
        search = vowels.find(character)
        if search != -1:
            count += 1
    print(count)


vowel_count('Hi, my name is Brittany MCNAIR')