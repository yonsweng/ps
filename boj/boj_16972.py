from math import sqrt


def solve():
    for a in range(1, 500):
        for b in range(1, 500):
            answer = []
            x, y = -8140, -8140
            a = 360
            b = 450
            toggle = 1
            for _ in range(813):
                answer.append((x, y))
                x += a * 2
                if x > 8140:
                    x = -8140 + a * toggle
                    y += b
                    toggle = 1 - toggle
                if y > 8140:
                    print("Error: y exceeded limit")
                    return
            answer.append((8140, 8140))

            # Find minimum distance
            min_dist2 = float('inf')
            dist_list = {}
            for i in range(len(answer)):
                for j in range(i + 1, len(answer)):
                    dist = (answer[i][0] - answer[j][0]) * (answer[i][0] - answer[j][0]) + (answer[i][1] - answer[j][1]) * (answer[i][1] - answer[j][1])
                    dist_list[dist] = dist_list.get(dist, 0) + 1
                    min_dist2 = min(min_dist2, dist)
            if dist_list[min_dist2] > 1:
                print("Error: Multiple pairs with minimum distance")
                return
            print(sqrt(min_dist2))


if __name__ == "__main__":
    solve()
