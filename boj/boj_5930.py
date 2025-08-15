from sys import stdin


def solve():
    N = int(stdin.readline().strip())
    notes = [int(stdin.readline().strip()) for _ in range(N)]
    C = int(stdin.readline().strip())
    chord = [int(stdin.readline().strip()) for _ in range(C)]

    chord_diff = {}
    for c1 in chord:
        for c2 in chord:
            chord_diff[abs(c1 - c2)] = chord_diff.get(abs(c1 - c2), 0) + 1

    answer = []
    for left in range(N - len(chord) + 1):
        current = notes[left:left + len(chord)]

        current_diff = {}
        for n1 in current:
            for n2 in current:
                current_diff[abs(n1 - n2)] = current_diff.get(abs(n1 - n2), 0) + 1

        if current_diff == chord_diff:
            answer.append(left + 1)

    print(len(answer))
    for idx in answer:
        print(idx)


if __name__ == "__main__":
    solve()
