import random


def rand7():
    return random.randint(1, 7)


def rand5():

    # Implement rand5() using rand7()
    x = rand7()
    while x > 5:
        x = rand7()
    return x


for j in range(20):
    results = [0] * 5
    for i in range(500000):
        results[rand5() - 1] += 1

    print(results)