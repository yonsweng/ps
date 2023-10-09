def solution(card, word):
    deck = {}
    for row, c in enumerate(card, 1):
        for alphabet in c:
            if alphabet not in deck:
                deck[alphabet] = [row, 0]
            deck[alphabet][1] += 1

    answer = []

    for w in word:
        needs = {}
        for alphabet in w:
            if alphabet not in needs:
                needs[alphabet] = 0
            needs[alphabet] += 1

        checked_rows = [True, False, False, False]
        for alphabet, cnt in needs.items():
            if alphabet not in deck:
                checked_rows[0] = False
                break
            if deck[alphabet][1] < cnt:
                break
            checked_rows[deck[alphabet][0]] = True

        if all(checked_rows):
            answer.append(w)

    if len(answer) == 0:
        answer.append("-1")

    return answer
