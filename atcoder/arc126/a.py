T = int(input())
for _ in range(T):
    N2, N3, N4 = map(int, input().split())
    n1, n2, n3 = N2, N4, N3//2
    answer = 0
    if n2 >= 1 and n3 >= 1:
        fives = min(n2, n3)
        n2 -= fives
        n3 -= fives
        answer += fives
    if n1 >= 2 and n3 >= 1:
        fives = min(n1//2, n3)
        n1 -= fives*2
        n3 -= fives
        answer += fives
    if n1 >= 1 and n2 >= 2:
        fives = min(n1, n2//2)
        n1 -= fives
        n2 -= fives*2
        answer += fives
    if n1 >= 3 and n2 >= 1:
        fives = min(n1//3, n2)
        n1 -= fives*3
        n2 -= fives
        answer += fives
    if n1 >= 5:
        fives = n1//5
        n1 -= fives
        answer += fives
    print(answer)
