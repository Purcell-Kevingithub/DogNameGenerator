# imported modulues for script
import random
word_file = "dog.py"
dog_list = []

# fill up the word_list
with open(word_file, 'r') as dogname:
    for line in dogname:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # excludes words that are too long or too short
        if 2 < len(word) < 20:
            dog_list.append(word)

# function returns a random name from the dogname file and the first letter is capitalized


def generate_dognames():
    return random.choice(dog_list).title()


# runs the function 10 times
for i in range(10):
    print(generate_dognames())
