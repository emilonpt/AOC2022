from aoc22_utils import read_input_file_without_trailing_newlines

day_6_input = read_input_file_without_trailing_newlines(6)

#print(day_6_input)

def find_signals(transmission,length):
    transmission = transmission[0]
    last_n = []
    for i,c in enumerate(transmission):
        if len(last_n) < length:
            last_n.append(c)
        else:
            if len(last_n) == len(set(last_n)):
                return i
            else:
                last_n = last_n[1:]
                last_n.append(c)

start_of_packet = find_signals(day_6_input, 4)

# Part 1
print(start_of_packet)

# Part 2

start_of_message = find_signals(day_6_input, 14)

print(start_of_message)
            