from sys import stdin


def solve():
    birth_year, birth_month, birth_day = map(int, stdin.readline().strip().split())
    current_year, current_month, current_day = map(
        int, stdin.readline().strip().split()
    )

    age_man = (
        current_year
        - birth_year
        - (1 if (current_month, current_day) < (birth_month, birth_day) else 0)
    )
    age_korean = current_year - birth_year + 1
    age_year = current_year - birth_year
    print(age_man)
    print(age_korean)
    print(age_year)


if __name__ == "__main__":
    solve()
