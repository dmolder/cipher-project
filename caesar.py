import string

def caesar_cypher(s, k: int):
    """
    The function is expected to return a STRING.
    The function accepts following parameters:
    1. STRING s
    2. INTEGER k
    """
    s = list(s)
    letters = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    for index in range(len(s)):
        if s[index] in string.punctuation or s[index].isnumeric():
            continue
        elif s[index].isupper():
            s[index] = s[index].lower()
            s[index] = letters[(letters.index(s[index]) + int(k)) % 26]
            s[index] = s[index].upper()
        else:
            s[index] = letters[(letters.index(s[index]) + int(k)) % 26]
    return ''.join(s)
