from aoc22_utils import read_input_file_without_trailing_newlines

day_3_input = read_input_file_without_trailing_newlines(3)

LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

PRIORITIES = {c:i+1 for i,c in enumerate(LOWERCASE_LETTERS)}
PRIORITIES.update({c:i+1+len(LOWERCASE_LETTERS) for i,c in enumerate(UPPERCASE_LETTERS)})

def find_common_letters(lines):
    line_sets = [set(line) for line in lines]
    common_letters = set.intersection(*line_sets)
    return list(common_letters)[0]

lines_split_in_half = [(line[:len(line)//2], line[len(line)//2:]) for line in day_3_input]
common_letters = [find_common_letters([line1, line2]) for line1, line2 in lines_split_in_half]
common_letters_priorities = [PRIORITIES[c] for c in common_letters]

# Part 1
print(sum(common_letters_priorities))

# Part 2

groups_of_3 = [day_3_input[i:i+3] for i in range(0, len(day_3_input), 3)]
common_letters_g3 = [find_common_letters(group) for group in groups_of_3]
common_letters_g3_priorities = [PRIORITIES[c] for c in common_letters_g3]

print(sum(common_letters_g3_priorities))





