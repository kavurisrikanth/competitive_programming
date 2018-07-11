import random


def rand5():
    return random.randint(1, 5)


def rand7():
    # Implement rand7() using rand5()

    while True:
        x = 5 * (rand5() - 1)
        y = rand5()

        if x + y <= 21:
            return (x + y) % 7 + 1


for j in range(20):
    results = [0] * 7
    for i in range(700000):
        results[rand7() - 1] += 1

    print(results)