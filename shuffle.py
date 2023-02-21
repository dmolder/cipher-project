"""
N/A
"""
def shuffle(intake: str, amount: int) -> str:
    """
    This function returns a string where each character is
    shuffled by a given number of spots.

    The function is expected to return a STRING.
    The function accepts following parameters:
    1. STRING intake
    2. INTEGER amount
    """
    answer = list(' '*len(intake))
    for i,_ in enumerate(intake):
        first = (i % amount) * int(len(intake) / amount) + int(i/amount)
        if answer[first] == ' ':
            answer[first] = intake[i]
        else:
            answer.insert(first,intake[i])
            answer.pop()
    return ''.join(answer)
