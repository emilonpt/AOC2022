from aoc22_utils import read_input_file_without_trailing_newlines
from collections import defaultdict

day_10_input = read_input_file_without_trailing_newlines(10)

def get_num_cycles(commands):
    # 2 for each 'addx' command
    # 1 for each 'noop' command

    return 2 * sum(1 for c in commands if c.startswith('addx')) + sum(1 for c in commands if c.startswith('noop'))

def get_queued_additions(commands):
    #pad commands with 'noop' commands to match the number of cycles
    commands += ['noop'] * (get_num_cycles(commands) - len(commands))
    queued_additions = defaultdict(lambda: None)
    queued_additions[0] = 0
    for c, command in enumerate(commands):
        if command.startswith('addx'):
            queued_additions[c+1+len(queued_additions)] = int(command.split(' ')[1])
    return queued_additions

def draw_pixel(canvas,row,col,sprite):
    symbol = '#' if col in sprite else '.'
    canvas[row][col] = symbol
    return canvas


def process_commands(commands, canvas=None):

    if canvas:
        commands += ['noop'] * (get_num_cycles(commands) - len(commands))

    state = {i:{'before':None, 'after':None} for i in range(1,get_num_cycles(commands)+1)}

    x = 1
    
    queued_additions = get_queued_additions(commands)

    if canvas:
        sprite = [0,1,2]

    for cycle, command in enumerate(commands):

        state[cycle+1]['before'] = x

        # if there is a queued addition, do it
        if queued_additions[cycle+1] is not None:
            x += queued_additions[cycle+1]

        if canvas:
            # col goes from 0 to 39
            col = cycle % 40

            row = cycle // 40

            if row == 6:
                return canvas, state

            canvas = draw_pixel(canvas,row,col,sprite)
        
        state[cycle+1]['after'] = x

        if canvas:
            # sprite moves so that middle pixel is x_after
            sprite = [x-1,x,x+1]
            # sprite bounded by 0 and 39 (if any of the pixels is out of bounds, replace by first possible sprite)
            for c in sprite:
                if c < 0:
                    sprite = [0,1,2]
                    break
                if c > 39:
                    sprite = [37,38,39]
                    break

    if canvas:
        return canvas,state
    else:
        return state

def get_score(state, cycles):
    scores = defaultdict(lambda: None)
    for c in cycles:
        scores[c] = state[c]['before']*c
    return sum(scores.values())

def process_commands_crt(commands):
    canvas = [[' ' for _ in range(40)] for _ in range(6)]
    canvas,state = process_commands(commands, canvas)
    return canvas

def print_canvas(canvas):
    for row in canvas:
        print(''.join(row))


#Part 1
state = process_commands(day_10_input)

cycles = range(20,220+1,40)
score = get_score(state, cycles)
print(score)

#Part 2

canvas = process_commands_crt(day_10_input)

print_canvas(canvas)