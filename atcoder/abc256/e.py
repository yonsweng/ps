N = int(input())
X = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

answer = 0
visited = set()
for i in range(1, N+1):
    if i in visited:
        continue

    stack = []
    curr_visited = set()
    j = i
    while j not in visited:
        visited.add(j)
        curr_visited.add(j)
        stack.append(j)
        j = X[j]

    if j not in curr_visited:
        continue

    # print('stack:', stack)

    cycle = []
    while len(stack) > 0:
        top = stack.pop()
        cycle.append(top)
        if top == j:
            break

    # print('cycle:', cycle)

    min_x = 10 ** 9
    for j in cycle:
        min_x = min(min_x, C[j])

    answer += min_x

print(answer)
