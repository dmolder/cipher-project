"""
N/A
"""
import string

def caesar_cypher(intake: str, amount: int) -> str:
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
    for index in enumerate(intake):
        if intake[index] in string.punctuation or intake[index].isnumeric():
            continue
        elif intake[index].isupper():
            intake[index] = intake[index].lower()
            intake[index] = letters[(letters.index(intake[index]) + int(amount)) % 26]
            intake[index] = intake[index].upper()
        else:
            intake[index] = letters[(letters.index(intake[index]) + int(amount)) % 26]
    return ''.join(intake)