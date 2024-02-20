#Create a function that generates a random number between a given range.
import random
def random_num(a,b):
    return random.randint(a, b)

print(random_num(1,99))