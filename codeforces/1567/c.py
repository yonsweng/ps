def f(p, n, carries, acc):
    if p == -1:
        return acc

    ret = 0
    for carry in range(2):
        if p < 2 and carry == 1:
            continue
        target = n[p] - carry + carries[p+2] * 10
        if target < 0:
            continue
        if target >= 10:
            curr = 19 - target
        else:
            curr = target + 1
        if curr > 0:
            carries[p] = carry
            ret += f(p-1, n, carries, acc*curr)

    return ret


T = int(input())
for _ in range(T):
    n = tuple(map(int, reversed(input())))
    carries = [0] * 12
    answer = f(len(n)-1, n, carries, 1) - 2
    print(answer)
