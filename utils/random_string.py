import random
import string

def random_string(str_length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(str_length))