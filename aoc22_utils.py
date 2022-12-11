def read_input_file_without_trailing_newlines(day:int) -> list[str]:
    with open('./Day{}/input.txt'.format(day)) as f:
        l = f.readlines()
        for i in range(len(l)):
            if l[i][-1] == '\n':
                l[i] = l[i][:-1]
    return l

def split_input_list_on_empty_string(input_list):
    output_list = []
    temp_list = []
    for i in input_list:
        if i == '':
            output_list.append(temp_list)
            temp_list = []
        else:
            temp_list.append(i)
    output_list.append(temp_list)
    return output_list