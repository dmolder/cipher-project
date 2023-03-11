"""
TODO: Psuedo-One time pads for obvious or guessable keys
"""
import string

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
