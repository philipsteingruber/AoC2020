import re


def passport_valid_part1(passport):
    required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', ]
    return all(map(lambda field: field in passport, required_fields))


def part2(passports):
    valid_passports = 0
    for passport in passports:
        # Check birthyear (has to be >= 1920 and <= 2002)
        byr = re.search(r'byr:(\d{4})', passport)
        if bool(byr):
            byr = int(byr.group(1))
            if not 1920 <= byr <= 2002:
                continue
        else:
            continue

        # Check issued year (has to be >= 2010 and <= 2020)
        iyr = re.search(r'iyr:(\d{4})', passport)
        if bool(iyr):
            iyr = int(iyr.group(1))
            if not 2010 <= iyr <= 2020:
                continue
        else:
            continue

        # Check expiration year (has to be >= 2020 and <= 2030
        eyr = re.search(r'eyr:(\d{4})', passport)
        if bool(eyr):
            eyr = int(eyr.group(1))
            if not 2020 <= eyr <= 2030:
                continue
        else:
            continue

        # Check height (if cm, has to be 150-193, if in, has to be 59-76)
        hgt = re.search(r'hgt:(\d+)(\w{2})', passport)
        if bool(hgt):
            value = int(hgt.group(1))
            unit = hgt.group(2)

            if unit == 'cm':
                if not 150 <= value <= 193:
                    continue
            elif unit == 'in':
                if not 59 <= value <= 76:
                    continue
            else:
                continue
        else:
            continue

        # Check hair color (# followed by 6 characters 0-9 or a-f)
        hcl = re.search(r'hcl:(#[0-9a-f]*)', passport)
        if not bool(hcl):
            continue
        else:
            if len(hcl.group(1)) != 7:
                print(passport)
                continue

        # Check eye color (has to be on of amb blu brn gry grn hzl oth)
        valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth', ]
        ecl = re.search(r'ecl:(\w{3})', passport)
        if not (bool(ecl) and ecl.group(1) in valid_eye_colors):
            continue

        # Check passport ID (has to be 9 digits)
        pid = re.search(r'pid:(\d*)', passport)
        if not bool(pid) or len(pid.group(1)) != 9:
            continue

        # If all checks have passed, increment number of valid passports.
        valid_passports += 1

    return valid_passports


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        passports = file.read().split('\n\n')
    print('Part 1:', sum(map(lambda pp: passport_valid_part1(pp), passports)))
    print('Part 2:', part2(passports))
