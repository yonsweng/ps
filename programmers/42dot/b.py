def solution(friends, user_id):
    adj = {}
    for f in friends:
        if f[0] not in adj:
            adj[f[0]] = set()
        if f[1] not in adj:
            adj[f[1]] = set()
        adj[f[0]].add(f[1])
        adj[f[1]].add(f[0])

    # get all nodes that are 2 hops away from user_id
    candidates = set()
    for f in adj[user_id]:
        for f2 in adj[f]:
            if f2 != user_id and f2 not in adj[user_id]:
                candidates.add(f2)

    # get all nodes that are 1 hop away from both candidates and user_id
    n_connects = {c: 0 for c in candidates}
    for c in candidates:
        for f in adj[c]:
            if f in adj[user_id]:
                n_connects[c] += 1

    # get max n_connects
    max_connects = max(n_connects.values())

    # get all elements that have max n_connects
    answer = []
    for c, n in n_connects.items():
        if n == max_connects:
            answer.append(c)

    answer.sort()

    return answer
