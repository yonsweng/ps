def get_subtree_size(parking, i, subtree_size):
    subtree_size[i] = 1
    for j in range(2):
        if parking[i][j] != -1:
            get_subtree_size(parking, parking[i][j], subtree_size)
            subtree_size[i] += subtree_size[parking[i][j]]


def solution(parking):
    n = len(parking)

    total = n * (n - 1) // 2

    subtree_size = [0] * n  # subtree_size[i] = size of subtree rooted at i
    get_subtree_size(parking, 0, subtree_size)

    fail_case = 0
    for i in range(n):
        fail_case += subtree_size[i] - 1

    return total - fail_case
