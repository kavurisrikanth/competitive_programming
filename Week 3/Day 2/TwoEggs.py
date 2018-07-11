import random


def func():
    floors = list(range(100))

    ans = random.randint(0, 99)
    # ans = 50

    cur = 0
    jump = 14
    moves = 0

    while floors[cur] != ans:
        cur += jump
        moves += 1
        # if floors[cur] == ans:
        #     return moves, cur

        if floors[cur] > ans:
            start = cur - jump
            while start <= cur:
                moves += 1
                if floors[start] == ans:
                    return moves, start
                start += 1

        jump -= 1

    return moves, cur


for i in range(5):
    steps, number = func()
    print('found ' + str(number) + ' in ' + str(steps) + ' steps.')