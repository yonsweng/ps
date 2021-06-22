S = input()
T = input()

alphabets = set(T)

left_most = {alphabet: [0] * len(T) for alphabet in alphabets}
for alphabet in alphabets:
    curr_left_most = len(T)
    for i in range(len(T) - 1, -1, -1):
        if T[i] == alphabet:
            curr_left_most = i
        left_most[alphabet][i] = curr_left_most

# print(left_most)

fail = False
answer = 1
i = -1
for j, s in enumerate(S):
    if s not in left_most:
        fail = True
        break

    i += 1
    if i == len(T):
        answer += 1
        i = 0
    i = left_most[s][i]
    if i == len(T):
        answer += 1
        i = 0
        i = left_most[s][i]

if fail:
    print(-1)
else:
    print(answer)
