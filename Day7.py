from aoc22_utils import read_input_file_without_trailing_newlines

day_7_input = read_input_file_without_trailing_newlines(7)

def change_directory(current_directory, new_directory):
    if new_directory == '..':
        return '/'.join(current_directory.split('/')[:-1])
    elif new_directory.startswith('/'):
        return new_directory
    else:
        return current_directory + '/' + new_directory

def build_file_tree(input):
    tree = {}
    current_dir = ''
    for i,line in enumerate(input):
        if line.startswith('$ cd'):
            current_dir = change_directory(current_dir, line.split(' ')[2])
            if current_dir not in tree:
                tree[current_dir] = []
        if line[:4] not in ['$ cd', '$ ls']:
            tree[current_dir].append(line)
    return tree

def sum_directory_filesizes(dir):
    filesizes = 0
    for file in dir:
        if file[:3] != 'dir':
            filesizes += int(file.split(' ')[0])
    return filesizes

def create_file_size(tree):

    filesizes = {}

    for dir in tree:
        filesizes[dir] = sum_directory_filesizes(tree[dir])

    return filesizes

def add_subdirectory_filesizes(filesizes):
    for dir in filesizes:
        # add subdirectory filesizes
        for subdir in filesizes:
            if subdir.startswith(dir) and subdir != dir:
                filesizes[dir] += filesizes[subdir]
    return filesizes

tree = build_file_tree(day_7_input)

filesizes = create_file_size(tree)
filesizes_with_subdirs = add_subdirectory_filesizes(filesizes)

# Part 1
print(sum([filesizes_with_subdirs[dir] for dir in filesizes_with_subdirs if filesizes_with_subdirs[dir] < 100000]))

# Part 2

total_disk_space = 70000000
used_disk_space = filesizes_with_subdirs['/']
free_space = total_disk_space - used_disk_space
update_size = 30000000
space_to_free = update_size - free_space

def find_smallest_suitable_del_dir(filesizes_with_subdirs, space_to_free):
    candidates = {}
    for dir in filesizes_with_subdirs:
        if filesizes_with_subdirs[dir] > space_to_free:
            candidates[dir] = filesizes_with_subdirs[dir]

    smallest_suitable_del_dir = min(candidates, key=candidates.get)
    return smallest_suitable_del_dir

smallest_suitable_del_dir = find_smallest_suitable_del_dir(filesizes_with_subdirs, space_to_free)

print(filesizes_with_subdirs[smallest_suitable_del_dir])