# Write a program to shuffle the elements of a list randomly.
import random


def random_shuffle():
    list_to_shuffle = input("Please enter values with ' ' delimiter:  ").split()
    random.shuffle(list_to_shuffle)
    return list_to_shuffle


print(random_shuffle())
