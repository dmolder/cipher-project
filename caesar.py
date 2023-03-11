"""
TODO: Tests, subtracts for ciphers, letter to numbers
"""
import string
import math

def caesar_cipher(intake: str, amount: int) -> str:
    """
    This function returns a string where each character is
    shifted forwards or backwards in the alphabet by a given value.

    The function is expected to return a STRING.
    The function accepts following parameters:
    1. STRING intake
    2. INTEGER amount
    """
    intake = list(intake)
    letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    for index,_ in enumerate(intake):
        if intake[index] in string.punctuation or intake[index].isnumeric():
            continue
        if intake[index].isupper():
            intake[index] = intake[index].lower()
            intake[index] = letters[(letters.index(intake[index]) + int(amount)) % 26]
            intake[index] = intake[index].upper()
        else:
            intake[index] = letters[(letters.index(intake[index]) + int(amount)) % 26]
    return ''.join(intake)

def number_cipher(intake: str) -> str:
    """
    This function returns a string where each character is
    converted from a numerical value, i.e (a=1,b=2,etc...)
    Expected format is to use space as a delimitter.

    The function is expected to return a STRING.
    The function accepts the following parameter:
    1. STRING intake
    """
    intake = intake.split(" ")
    letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    for index,_ in enumerate(intake):
        if intake[index].isnumeric():
            num = int(intake[index])-1
            if num > 25 or num < 0:
                continue
            intake[index] = letters[num]
        else:
            continue
    return ''.join(intake)

def vigenere_cipher(intake: str, key: str, repeat: str) -> str:
    """
    This function returns a string where each character is
    shifted forwards or backwards in the alphabet by a given value
    which is determined by the corresponding letter in the key.

    The function is expected to return a STRING.
    The function accepts following parameters:
    1. STRING intake
    2. STRING key
    """
    intake = list(intake)
    key = list(key)
    if (repeat == "True" or repeat == "true" or repeat == "T" or repeat == "t"):
        key = key * math.ceil((len(intake)/len(key)))
        key = key[0:len(intake)]
    else:
        while len(key) < len(intake):
            key.append('a')

    letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    for index,_ in enumerate(intake):
        if intake[index] in string.punctuation or intake[index].isnumeric():
            continue
        intake[index] = letters[(letters.index(key[index])+letters.index(intake[index])) % 26]
    return ''.join(intake)
