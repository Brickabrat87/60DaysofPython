#Write a function that counts the frequency of each word in a sentence.


def word_frequency():
    user_input = input("Please provide a sentence:  ")
    user_input
    user_input_split = user_input.split(' ')
    print(user_input_split)
    freq = {}
    for i in user_input_split:
        freq[i] = user_input.count(i)
    return freq

print(word_frequency())