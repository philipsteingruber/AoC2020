from itertools import count

def generate_seat_ids(boarding_passes):
    seat_ids = []
    for boarding_pass in boarding_passes:
        row_modifiers = boarding_pass[:7]
        column_modifiers = boarding_pass[7:]

        possible_rows = range(128)
        for row_modifier in row_modifiers:
            if row_modifier == 'F':
                possible_rows = possible_rows[:len(possible_rows)//2]
            else:
                possible_rows = possible_rows[len(possible_rows)//2:]
        row = possible_rows[0]

        possible_columns = range(8)
        for column_modifier in column_modifiers:
            if column_modifier == 'R':
                possible_columns = possible_columns[len(possible_columns) // 2:]
            else:
                possible_columns = possible_columns[:len(possible_columns) // 2]
        column = possible_columns[0]

        seat_id = row * 8 + column
        seat_ids.append(seat_id)
    return seat_ids


if __name__ == '__main__':
    with open('input.txt') as file:
        boarding_passes = map(str.strip, file.readlines())

    seat_ids = sorted(generate_seat_ids(boarding_passes))
    print('Part 1:', max(seat_ids))

    for seat in range(min(seat_ids), max(seat_ids)+1):
        if seat not in seat_ids:
            print('Part 2:', seat)
            break
