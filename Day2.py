from aoc22_utils import read_input_file_without_trailing_newlines

day_2_input = read_input_file_without_trailing_newlines(2)

# A -> Opponent played Rock
# B -> Opponent played Paper
# C -> Opponent played Scissors

# X -> We played Rock
# Y -> We played Paper
# Z -> We played Scissors

PLAYED_SCORE_DICT = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

OUTCOME_SCORE_DICT = {
    'L': 0,
    'D': 3,
    'W': 6
}

def get_winner(played, opponent_played):
    if (played,opponent_played) in [('X','A'),('Y','B'),('Z','C')]: # If we played the same
        return 'D'
    elif played == 'X' and opponent_played == 'C': # If we played Rock and they played Scissors
        return 'W'
    elif played == 'Y' and opponent_played == 'A': # If we played Paper and they played Rock
        return 'W'
    elif played == 'Z' and opponent_played == 'B': # If we played Scissors and they played Paper
        return 'W'
    else: # All other cases
        return 'L'

def get_score(played, opponent_played):
    return PLAYED_SCORE_DICT[played] + OUTCOME_SCORE_DICT[get_winner(played, opponent_played)]

result = map(lambda x: get_score(x[2], x[0]), day_2_input)

# Part 1 solution
print(sum(result))

# Part 2:

# X -> We need to lose
# Y -> We need to draw
# Z -> We need to win

def get_correct_play(desired_outcome, opponent_played):
    if desired_outcome == 'X': # If we need to lose
        if opponent_played == 'A': # If they played Rock, we need to play Scissors
            return 'Z'
        elif opponent_played == 'B': # If they played Paper, we need to play Rock
            return 'X'
        elif opponent_played == 'C': # If they played Scissors, we need to play Paper
            return 'Y'
    elif desired_outcome == 'Y': # If we need to draw
        if opponent_played == 'A': # If they played Rock, we need to play Rock
            return 'X'
        elif opponent_played == 'B': # If they played Paper, we need to play Paper
            return 'Y'
        elif opponent_played == 'C': # If they played Scissors, we need to play Scissors
            return 'Z'
    elif desired_outcome == 'Z': # If we need to win
        if opponent_played == 'A': # If they played Rock, we need to play Paper
            return 'Y'
        elif opponent_played == 'B': # If they played Paper, we need to play Scissors
            return 'Z'
        elif opponent_played == 'C': # If they played Scissors, we need to play Rock
            return 'X'

played = map(lambda x: get_correct_play(x[2], x[0]), day_2_input)

opponent_played = map(lambda x: x[0], day_2_input)

result = map(lambda x: get_score(x[0], x[1]), zip(played, opponent_played))

# Part 2 solution
print(sum(result))

