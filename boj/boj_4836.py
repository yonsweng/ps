from sys import stdin


def find_error_1(dance) -> bool:
    found = False
    for i in range(len(dance)):
        if dance[i] == "dip":
            if i >= 2 and dance[i - 2] == "jiggle":
                continue
            if i >= 1 and dance[i - 1] == "jiggle":
                continue
            if i + 1 < len(dance) and dance[i + 1] == "twirl":
                continue
            if i + 2 < len(dance) and dance[i + 2] == "twirl":
                continue
            found = True
            dance[i] = "DIP"
    return found


def find_error_2(dance) -> bool:
    if len(dance) >= 3 and dance[-3] == "clap" and dance[-2] == "stomp" and dance[-1] == "clap":
        return False
    return True


def find_error_3(dance) -> bool:
    if "twirl" in dance and "hop" not in dance:
        return True
    return False


def find_error_4(dance) -> bool:
    if len(dance) >= 1 and dance[0] == "jiggle":
        return True
    return False


def find_error_5(dance) -> bool:
    if "dip" not in dance and "DIP" not in dance:
        return True
    return False


def solve():
    while True:
        dance = stdin.readline().strip()
        if dance == "":
            break
        
        dance = dance.split()

        errors = []
        if find_error_1(dance):
            errors.append(1)
        if find_error_2(dance):
            errors.append(2)
        if find_error_3(dance):
            errors.append(3)
        if find_error_4(dance):
            errors.append(4)
        if find_error_5(dance):
            errors.append(5)

        if errors:
            print(f"form {('errors ' + ', '.join(map(str, errors[:-1])) + ' and') if len(errors) > 1 else 'error'} {errors[-1]}:", end=" ")
        else:
            print("form ok:", end=" ")
        print(" ".join(dance))


if __name__ == "__main__":
    solve()
