def shuffle(intake: str, amount: int) -> str:
    answer = list(' '*len(intake))
    for i in range(len(intake)):
        first = (i % amount) * int(len(intake) / amount) + int(i/amount)
        if answer[first] == ' ':
            answer[first] = intake[i]
        else:
            answer.insert(first,intake[i])
            answer.pop()
    return ''.join(answer)
