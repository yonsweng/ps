from sys import stdin


def solve():
    counts = {}

    N = int(stdin.readline().rstrip())
    for _ in range(N):
        species = stdin.readline().rstrip()
        if species in counts:
            counts[species] += 1
        else:
            counts[species] = 1

    max_count = max(counts.values())
    max_species = [species for species, count in counts.items() if count == max_count]

    if len(max_species) == 1 and counts[max_species[0]] > N // 2:
        print(max_species[0])
    else:
        print("NONE")


if __name__ == "__main__":
    solve()
