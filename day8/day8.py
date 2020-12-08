import copy


def execute_instruction(instruction, current_acc, current_address):
    operation, argument = instruction

    if operation == 'nop':
        new_acc = current_acc
        new_address = current_address + 1
    elif operation == 'acc':
        new_acc = current_acc + int(argument)
        new_address = current_address + 1
    elif operation == 'jmp':
        new_acc = current_acc
        new_address = current_address + int(argument)

    return new_acc, new_address


def part1(instructions):
    accumulator = 0
    visited_instructions = []

    current_instruction = 0
    while current_instruction not in visited_instructions:
        visited_instructions.append(current_instruction)
        accumulator, current_instruction = execute_instruction(instructions[current_instruction],
                                                               accumulator,
                                                               current_instruction)
    return accumulator


def part2(instructions):
    possible_solutions = [i for i, instruction in enumerate(instructions) if instruction[0] in ['nop', 'jmp']]
    for possible_solution in possible_solutions:
        temp_instructions = copy.deepcopy(instructions)
        if temp_instructions[possible_solution][0] == 'nop':
            temp_instructions[possible_solution][0] = 'jmp'
        else:
            temp_instructions[possible_solution][0] = 'nop'

        accumulator = 0
        visited_instructions = []

        current_instruction = 0
        while current_instruction not in visited_instructions:
            visited_instructions.append(current_instruction)
            accumulator, current_instruction = execute_instruction(temp_instructions[current_instruction],
                                                                   accumulator,
                                                                   current_instruction)
            if current_instruction >= len(temp_instructions):
                return accumulator


if __name__ == '__main__':
    with open('input.txt') as file:
        instructions = list(map(str.split, file.readlines()))
        instructions = [[instruction[0], int(instruction[1])] for instruction in instructions]
    print('Part 1:', part1(instructions))
    print('Part 2:', part2(instructions))
