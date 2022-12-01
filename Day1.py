from aoc22_utils import read_input_file_without_trailing_newlines

day_1_input = read_input_file_without_trailing_newlines(1)

totals = []

j=0

for i in day_1_input:
    if i == '':
        j+=1
        continue
    else:
        if j == len(totals):
            totals.append(int(i))
        else:
            totals[j] += int(i)

# Part 1 solution
print(max(totals))

# Part 2 solution
running_total = max(totals)
for z in range(2):
    totals.remove(max(totals))
    running_total += max(totals)

print(running_total)