A, B = map(int, input().split())

answer = []

if A > B:
    for i in range(1, A+1):
        answer.append(i)
    for i in range(-1, -B, -1):
        answer.append(i)
    answer.append(-sum(answer))
else:
    for i in range(1, A):
        answer.append(i)
    for i in range(-1, -B-1, -1):
        answer.append(i)
    answer.append(-sum(answer))

print(*answer)
