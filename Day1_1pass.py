with open("./Day1/input.txt") as f:
    data = f.read()

groups = data.strip().split("\n")

top_3 = []
group_sum = 0
for item in groups:
    if item == "":
        if len(top_3) < 3:
            top_3.append(group_sum)
        else:
            if group_sum > min(top_3):
                top_3.remove(min(top_3))
                top_3.append(group_sum)
        group_sum = 0
    else:
        group_sum += int(item)

#part 1
print(max(top_3))
#part 2
print(sum(top_3))

