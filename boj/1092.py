answer = 0

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes = sorted(cranes, reverse=True)
boxes = sorted(boxes, reverse=True)

crane_pointers = [0] * len(cranes)

while crane_pointers[0] < len(boxes):
    for crane_num, crane_limit in enumerate(cranes):
        while crane_pointers[crane_num] < len(boxes):
            if boxes[crane_pointers[crane_num]] > 0 and \
                    boxes[crane_pointers[crane_num]] <= crane_limit:
                boxes[crane_pointers[crane_num]] = 0
                crane_pointers[crane_num] += 1

                if crane_num == 0:
                    answer += 1

                break
            crane_pointers[crane_num] += 1

if boxes[0] == 0:  # good
    print(answer)
else:
    print(-1)
