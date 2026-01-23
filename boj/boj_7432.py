from sys import setrecursionlimit, stdin

setrecursionlimit(510)


def print_structure(structure, depth=0):
    for folder in sorted(structure.keys()):
        print(" " * depth + folder)
        print_structure(structure[folder], depth + 1)


def solve():
    N = int(stdin.readline().strip())

    structure = {}
    for _ in range(N):
        path = stdin.readline().strip().split("\\")
        current = structure
        for folder in path:
            if folder not in current:
                current[folder] = {}
            current = current[folder]

    print_structure(structure)


if __name__ == "__main__":
    solve()
