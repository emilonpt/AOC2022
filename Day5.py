from aoc22_utils import read_input_file_without_trailing_newlines

def split_input(input):
    crates_input = []
    instructions_input = []
    for i, line in enumerate(input):
        if line == '':
            crates_input = input[:i]
            instructions_input = input[i+1:]
    return crates_input, instructions_input

def create_crate_stacks_original_state(crates_input):
    stack_numbers = [int(s) for s in crates_input[-1].split(' ') if s != '']
    stack_original_state = {i:[] for i in stack_numbers}
    crates_input_without_last_line = crates_input[:-1]
    # read crates input from bottom to top
    for i, line in enumerate(crates_input_without_last_line[::-1]):
        # split line into groups of 1 characters, ignore a character after each group
        split_line = [line[i:i+3] for i in range(0, len(line)) if i % 4 == 0]
        split_line = [s.replace('[', '').replace(']', '') for s in split_line]
        for j, crate in enumerate(split_line):
            if crate != '   ':
                stack_original_state[stack_numbers[j]].append(crate)
    return stack_original_state

def build_instructions_dict(instructions_input):
    instructions_dict = {i:{} for i in range(len(instructions_input))}
    instructions_ints = [line.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ') for line in instructions_input]

    for i, line in enumerate(instructions_ints):
        instructions_dict[i]['qty'] = int(line.split(' ')[0])
        instructions_dict[i]['from'] = int(line.split(' ')[1])
        instructions_dict[i]['to'] = int(line.split(' ')[2])
    return instructions_dict

def move_crates(instructions_dict, original_stack_state,part):
    stack_state = original_stack_state
    for i, instruction in instructions_dict.items():
        qty = instruction['qty']
        from_stack = instruction['from']
        to_stack = instruction['to']
        if part == 1:
            # crates are moved one at a time
            for j in range(qty):
                stack_state[to_stack].append(stack_state[from_stack].pop())
        elif part == 2:
            # crates are moved in a group
            crates_to_move = stack_state[from_stack][-qty:]
            stack_state[from_stack] = stack_state[from_stack][:-qty]
            stack_state[to_stack] = stack_state[to_stack] + crates_to_move

    return stack_state

day_5_input = read_input_file_without_trailing_newlines(5)

crates_input, instructions_input = split_input(day_5_input)

original_stack_state = create_crate_stacks_original_state(crates_input)

instructions_dict = build_instructions_dict(instructions_input)

# Part 1
stack_state = move_crates(instructions_dict, original_stack_state, 1)
result = [stack[-1] for stack in stack_state.values()]
print("".join(result))

# Part 2
original_stack_state = create_crate_stacks_original_state(crates_input) # reset stack state - do not understand why this is necessary
stack_state = move_crates(instructions_dict, original_stack_state, 2)
result = [stack[-1] for stack in stack_state.values()]
print("".join(result))