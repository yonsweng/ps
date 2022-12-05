def solution(record):
    answer = []

    n = len(record)

    people = {}

    game = [[] for _ in range(5)]
    for row in record:
        name, seconds = row.split(":")
        seconds = tuple(map(int, seconds.split(",")))

        people[name] = {
            "seconds": seconds,
            "golds": 0,
            "silvers": 0,
            "bronzes": 0,
            "total_games": sum([bool(a) for a in seconds]),
            "total_sec": sum(seconds),
            "last_game": [i for i in range(5) if seconds[i] != 0][-1],
        }

        for i in range(5):
            if seconds[i] != 0:
                game[i].append((name, seconds[i]))

    # calc medals
    for i in range(5):
        game[i].sort(key=lambda x: x[1])

        rank_gold = (len(game[i]) + 11) // 12
        rank_silver = (len(game[i]) + 3) // 4
        rank_bronze = (len(game[i]) + 1) // 2
        for rank, (name, _) in enumerate(game[i]):
            if rank < rank_gold:
                people[name]["golds"] += 1
            elif rank < rank_silver:
                people[name]["silvers"] += 1
            elif rank < rank_bronze:
                people[name]["bronzes"] += 1
                # print(i, name, rank, "bronze")
            else:
                break

    people = [
        (
            -data["total_games"],  # total_games
            -data["last_game"],  # last_game_reverse,
            -data["golds"],
            -data["silvers"],
            -data["bronzes"],
            data["total_sec"],
            name,
        )
        for name, data in people.items()
    ]

    people.sort()

    # print(people)

    answer = [tup[-1] for tup in people]

    return answer


record = [
    "jack:9,10,13,9,15",
    "jerry:7,7,14,10,17",
    "jean:0,0,11,20,0",
    "alex:21,2,7,11,4",
    "kevin:8,4,5,0,0",
    "brown:3,5,16,3,18",
    "ted:0,8,0,0,8",
    "lala:0,12,0,7,9",
    "hue:17,16,8,6,10",
    "elsa:11,13,10,4,13",
]
print(solution(record))
