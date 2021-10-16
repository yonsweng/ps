def solution(registered_list, new_id):
    n_first_index = len(new_id)
    for i, c in enumerate(new_id):
        if c in '0123456789':
            n_first_index = i
            break
    S, N = new_id[:n_first_index], new_id[n_first_index:]
    N = int(N) if len(N) > 0 else 0

    registered_list = set(registered_list)
    while True:
        new_id = S + (str(N) if N > 0 else '')
        if new_id not in registered_list:
            return new_id

        N += 1


registered_list = ["apple1", "orange", "banana3"]
new_id = "apple"
answer = solution(registered_list, new_id)
print(answer)
