from sys import stdin, setrecursionlimit

setrecursionlimit(30)

answer = ""


def is_a_shoter_than_b(a, b):
    if len(a) < len(b):
        return True
    elif len(a) > len(b):
        return False
    elif a > b:
        return True
    return False


def backtrack(permutation, sequence, index, current_string):
    global answer

    if is_a_shoter_than_b(answer, current_string):
        return

    if index == len(sequence):
        if is_a_shoter_than_b(current_string, answer):
            answer = current_string
        return

    backtrack(
        permutation,
        sequence,
        index + 1,
        current_string + permutation[int(sequence[index])],
    )
    if index + 2 <= len(sequence) and int(sequence[index : index + 2]) < 26:
        backtrack(
            permutation,
            sequence,
            index + 2,
            current_string + permutation[int(sequence[index : index + 2])],
        )


problem_number = 0
while True:
    permutation = stdin.readline().rstrip()
    if permutation == "#":
        break

    problem_number += 1
    print(f"Problem {problem_number}", flush=False)

    while True:
        sequence = stdin.readline().rstrip()
        if sequence == "0":
            break

        answer = "AAAAAAAAAAAAAAAAAAAA"
        backtrack(permutation, sequence, 0, "")

        print(answer, flush=False)
    print(flush=False)
