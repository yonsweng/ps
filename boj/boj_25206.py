from sys import stdin


def convert_to_score(grade):
    if grade == "A+":
        return 4.5
    elif grade == "A0":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B0":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C0":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D0":
        return 1.0
    else:  # F or other cases
        return 0.0


def solve():
    total_score = 0.0
    total_credits = 0
    for _ in range(20):
        subject, credit, grade = stdin.readline().split()

        if grade == "P":
            continue

        credit = float(credit)
        score = convert_to_score(grade)

        total_score += score * credit
        total_credits += credit

    if total_credits == 0:
        print("0.000000")
    else:
        print(f"{total_score / total_credits:.6f}")


if __name__ == "__main__":
    solve()
