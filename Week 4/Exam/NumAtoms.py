import re

from collections import defaultdict


def count_of_atoms(formula):
    criterion = r'([A-Z]{1}[a-z]?|\(|\)|\d+)'
    stack = []
    tokens = list(filter(lambda c: c, re.split(criterion, formula)))
    count = defaultdict(int)
    i = 0

    while i < len(tokens):
        token = tokens[i]
        if token == '(':
            stack.append(count)
            stack.append(token)
            count = defaultdict(int)
        elif token == ')':
            tmp = stack.pop()
            while tmp != '(':
                for k, v in tmp.items():
                    count[k] += v
                tmp = stack.pop()
        elif token.isdigit():
            if tokens[i - 1] == ')':
                for k, v in count.items():
                    count[k] = v * int(token)
            else:
                count[tokens[i - 1]] += int(token) - 1
        else:
            count[token] += 1
        i += 1
    while stack:
        tmp = stack.pop()
        for k, v in tmp.items():
            count[k] += v

    sorted_count = sorted(count.items(), key=lambda x: x[0])
    result = ''

    for k, v in sorted_count:
        result += k
        if v != 1:
            result += str(v)

    return result


print(count_of_atoms('K4(ON(SO3)2)2'))