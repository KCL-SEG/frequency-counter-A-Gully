"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    frequencies = {}
    mySet = set(items)
    print(mySet)
    for item in mySet:
        count = 0
        print(item)
        for x in items:
            if f'{x}' == f'{item}':
                count += 1
        frequencies[f'{item}'] = count
        print(frequencies)
    return frequencies


frequencies(['0', 4, 4, '4', 'd', 'd', 'e', 0, 'a', 'd', '4'])
