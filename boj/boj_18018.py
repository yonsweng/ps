from sys import stdin


def solve():
    previous = stdin.readline().strip()
    n = int(stdin.readline().strip())
    animals = [stdin.readline().strip() for _ in range(n)]

    candidates = {}
    for animal in animals:
        if animal[0] not in candidates:
            candidates[animal[0]] = []
        candidates[animal[0]].append(animal)

    first_letter = previous[-1]
    if first_letter not in candidates:
        print("?")
        return

    for animal in candidates[first_letter]:
        if animal[0] == animal[-1]:
            if len(candidates[animal[-1]]) == 1:
                print(animal + "!")
                return
        else:
            if animal[-1] not in candidates:
                print(animal + "!")
                return

    print(candidates[first_letter][0])


if __name__ == "__main__":
    solve()
