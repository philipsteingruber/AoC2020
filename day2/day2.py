import re
from collections import Counter


def day1(lines):
    policy_pattern = re.compile(r'(\d+)-(\d+) (\w)')
    password_pattern = re.compile(r': (\w+)')

    valid_passwords_count = 0
    for line in lines:
        min, max, letter = re.match(policy_pattern, line).groups()
        min = int(min)
        max = int(max)
        password = re.search(password_pattern, line).groups()[0]

        letter_count = Counter(password)[letter]

        if min <= letter_count <= max:
            valid_passwords_count += 1

    return valid_passwords_count

def day2(lines):
    policy_pattern = re.compile(r'(\d+)-(\d+) (\w)')
    password_pattern = re.compile(r': (\w+)')

    valid_passwords_count = 0
    for line in lines:
        pos1, pos2, letter = re.match(policy_pattern, line).groups()
        pos1 = int(pos1) - 1
        pos2 = int(pos2) - 1
        password = re.search(password_pattern, line).groups()[0]

        if (password[pos1] == letter) != (password[pos2] == letter):
            valid_passwords_count += 1

    return valid_passwords_count


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        inputlines = file.readlines()
    print(day1(inputlines))
    print(day2(inputlines))
