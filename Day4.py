from aoc22_utils import read_input_file_without_trailing_newlines

day_4_input = read_input_file_without_trailing_newlines(4)

pairs = [line.split(",") for line in day_4_input] # [[1-3],[2-5]]

def pairs_to_list_of_nums(pairs):
    list_of_nums = []
    for i, pair in enumerate(pairs):
        p1_start, p1_end = pair[0].split("-")
        p2_start, p2_end = pair[1].split("-")
        list_of_nums.append([list(range(int(p1_start), int(p1_end)+1)), list(range(int(p2_start), int(p2_end)+1))])
    return list_of_nums

list_of_nums = pairs_to_list_of_nums(pairs)

def is_sublist(sublist, list):
    for i in range(len(list)):
        if list[i:i+len(sublist)] == sublist:
            return True
    return False

def find_sublists(lists):
    sublists = []
    for i, list in enumerate(lists):
        for j, sublist in enumerate(lists):
            if i != j and is_sublist(sublist, list):
                sublists.append(sublist)
    return sublists

sublists = list(map(find_sublists, list_of_nums))

sublists = [sl for sl in sublists if sl != []]

# Part 1
print(len(sublists))

def lists_intersect(lists):
    for i, list in enumerate(lists):
        for j, sublist in enumerate(lists):
            if i != j and set(list).intersection(sublist):
                return True
    return False

#intersections for lists in list_of_nums
intersections = list(map(lists_intersect, list_of_nums))

intersections = [i for i in intersections if i == True]

# Part 2
print(len(intersections))