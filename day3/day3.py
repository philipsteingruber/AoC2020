from functools import reduce
from operator import mul


def run_slope(lines, x_delta, y_delta):
    x_pos, y_pos = 0, 0
    trees_hit = 0

    while y_pos <= len(lines) - 1:
        if lines[y_pos][x_pos] == '#':
            trees_hit += 1
        x_pos += x_delta
        x_pos %= len(lines[0])
        y_pos += y_delta
    return trees_hit


def day1(lines):
    print('Part 1:', run_slope(lines, 3, 1))


def day2(lines):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    slope_results = []
    for slope in slopes:
        slope_results.append(run_slope(lines, *slope))

    print('Part 2:', reduce(mul, slope_results))


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        lines = list(map(str.strip, file.readlines()))
    day1(lines)
    day2(lines)
