from itertools import combinations

def part1():
    with open('input.txt', 'r') as file:
        input_numbers = file.readlines()
        input_numbers = list(map(int, input_numbers))

    combs_2 = combinations(input_numbers, 2)
    combs_3 = combinations(input_numbers, 3)

    for comb in combs_2:
        if sum(comb) == 2020:
            print('Part 1 answer:', comb[0] * comb[1])
            break

    for comb in combs_3:
        if sum(comb) == 2020:
            print('Part 2 answer:', comb[0] * comb[1] * comb[2])
            break


if __name__ == '__main__':
    part1()