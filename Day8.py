from aoc22_utils import read_input_file_without_trailing_newlines

day_8_input = read_input_file_without_trailing_newlines(8)

def build_forest_grid(trees):
    trees_grid = {r+1:{} for r in range(len(trees))}
    for r, row in enumerate(trees):
        for c, tree in enumerate(row):
            trees_grid[r+1][c+1] = tree

    return trees_grid

def get_direction_trees(grid,r,c):
    above_trees = [grid[ar][c] for ar in range(1,r)]
    below_trees = [grid[br][c] for br in range(r+1, len(grid.keys())+1)]
    left_trees = [grid[r][lc] for lc in range(1,c)]
    right_trees = [grid[r][rc] for rc in range(c+1, len(grid[r].keys())+1)]

    return {'ab':above_trees,'be':below_trees,'le':left_trees,'ri':right_trees}


def is_visible(grid,r,c):

    t = get_direction_trees(grid,r,c)

    if grid[r][c] > max(t['ab']) or grid[r][c] > max(t['be']) or grid[r][c] > max(t['le']) or grid[r][c] > max(t['ri']):
        return True

    else:
        return False

def get_visibility_score(grid,r,c):

    tree_height = int(grid[r][c])

    t = get_direction_trees(grid,r,c)

    v = {d:0 for d in t.keys()}

    for d in t.keys():
        if d == 'ab':
            td = t[d][::-1] # reverse the list
        if d == 'le':
            td = t[d][::-1] # reverse the list
        if d == 'be':
            td = t[d]
        if d == 'ri':
            td = t[d]
        
        if td != []:
            for i, ht in enumerate(td):
                ht = int(ht)
                v[d] += 1
                if ht >= tree_height:
                    break

    res = 1
    for s in v.values():
        res *= s
    
    return res

def get_visibility_scores(grid):
    visibility_scores = {}
    for r in grid.keys():
        for c in grid[r].keys():
            visibility_scores[(r,c)] = get_visibility_score(grid,r,c)
    return visibility_scores

def get_visible_trees(grid):
    visible_trees = []
    # edge trees are visible
    for r in grid.keys():
        if r == 1 or r == len(grid.keys()): # top and bottom rows
            visible_trees.extend((r, c) for c in grid[r].keys())
        else:
            visible_trees.extend([(r, 1), (r, len(grid[r].keys()))]) # left and right columns

            # corners will be duplicated, so remove them
            visible_trees = list(set(visible_trees))

            # for the rest of the trees, check if they are visible
            for c in grid[r].keys():
                if c == 1 or c == len(grid[r].keys()) or r == 1 or r == len(grid.keys()):
                    continue
                else:
                    v = is_visible(grid,r,c)
                    if v:
                        visible_trees.append((r,c))

    return visible_trees

forest = build_forest_grid(day_8_input)
visible_trees = get_visible_trees(forest)

# Part 1

print(len(visible_trees))

# Part 2

visibility_scores = get_visibility_scores(forest)

max_score = max(visibility_scores.values())

print(max_score)