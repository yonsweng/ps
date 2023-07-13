from collections import deque

n, k = map(int, input().split())

dist = [999999] * 100001
dist[n] = 0
q = deque([n])

while q:
    m = q.popleft()
    l = m - 1
    if l >= 0 and l <= 100000 and dist[l] > dist[m] + 1:
        dist[l] = dist[m] + 1
        q.append(l)
    l = m + 1
    if l >= 0 and l <= 100000 and dist[l] > dist[m] + 1:
        dist[l] = dist[m] + 1
        q.append(l)
    l = m * 2
    if l >= 0 and l <= 100000 and dist[l] > dist[m] + 1:
        dist[l] = dist[m] + 1
        q.append(l)

print(dist[k])
