from itertools import combinations



def part1(lines, preamble_length):
    preamble_start, preamble_end = 0, preamble_length
    preamble = lines[:preamble_length]
    combs = combinations(preamble, 2)

    for line in lines[preamble_length:]:
        if not any([line == sum(comb) for comb in combs]):
            return line
        else:
            preamble_start += 1
            preamble_end += 1
            combs = combinations(lines[preamble_start:preamble_end], 2)


def part2(lines, target):
    for i, line in enumerate(lines):
        sublist = [line]
        pointer = i + 1

        while sum(sublist) < target:
            sublist.append(lines[pointer])
            pointer += 1
        if sum(sublist) == target:
            return min(sublist) + max(sublist)


if __name__ == '__main__':
    with open('input.txt') as file:
        lines = list(map(int, file.readlines()))
    preamble_length = 25
    part1_solution = part1(lines, preamble_length)
    print('Part 1:', part1_solution)
    print('Part 2:', part2(lines, part1_solution))
