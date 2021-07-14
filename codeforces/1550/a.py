length = 1
max_s = 0
add = 1
answer = [0] * 5001
while max_s < 5000:
    for s in range(max_s + 1, min(5001, max_s + add + 1)):
        answer[s] = length
    length += 1
    max_s += add
    add += 2

# print(answer[:10])

T = int(input())

for _ in range(T):
    s = int(input())
    print(answer[s])
