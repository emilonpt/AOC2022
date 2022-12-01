def read_input_file_without_trailing_newlines(day:int) -> list[str]:
    with open('./Day{}/input.txt'.format(day)) as f:
        l = f.readlines()
        for i in range(len(l)):
            if l[i][-1] == '\n':
                l[i] = l[i][:-1]
    return l