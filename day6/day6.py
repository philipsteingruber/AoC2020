from collections import Counter


def questions_per_group(group):
    return len(set(''.join(group)))


def questions_per_group_everyone(group):
    c = Counter(''.join(group))
    return len([question for question in c if c[question] == len(group)])


if __name__ == '__main__':
    with open('input.txt') as file:
        groups = list(map(str.split, file.read().split('\n\n')))

    print('Part 1:', sum(map(questions_per_group, groups)))
    print('Part 2:', sum(map(questions_per_group_everyone, groups)))