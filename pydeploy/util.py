from random import choice
from string import ascii_letters


def generate_random_string(length=30):
    return ''.join([choice(ascii_letters) for _ in range(length)])
