from sys import stdin


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        s = stdin.readline().strip()

        counts = {'N': 0, 'S': 0, 'E': 0, 'W': 0}
        for c in s:
            counts[c] += 1

        if (counts['N'] + counts['S']) % 2 == 1 or (counts['E'] + counts['W']) % 2 == 1:
            print('NO', flush=False)
            continue

        if list(sorted(counts.values())) == [0, 0, 1, 1]:
            print('NO', flush=False)
            continue

        rh = {'N': [], 'S': [], 'E': [], 'W': []}
        rh['N'].extend(['R', 'H'] * (counts['N'] // 2))
        counts['N'] %= 2
        rh['S'].extend(['R', 'H'] * (counts['S'] // 2))
        counts['S'] %= 2
        rh['E'].extend(['R', 'H'] * (counts['E'] // 2))
        counts['E'] %= 2
        rh['W'].extend(['R', 'H'] * (counts['W'] // 2))
        counts['W'] %= 2

        if counts['N'] == 1:
            rh['N'].append('R')
            rh['S'].append('R')

        if counts['E'] == 1:
            rh['E'].append('H')
            rh['W'].append('H')

        answer = []
        for c in s:
            answer.append(rh[c].pop())

        print(''.join(answer), flush=False)


if __name__ == "__main__":
    main()
