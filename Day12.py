from aoc22_utils import read_input_file_without_trailing_newlines
from collections import defaultdict

day_12_input = read_input_file_without_trailing_newlines(12)

class Grid():

    def __init__(self,input):
        self.grid = {}
        self.height_dict = {c:i+1 for i,c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        self.height_dict["S"] = self.height_dict["a"]
        self.height_dict["E"] = self.height_dict["z"]
        self.input = input
        self.build_grid()
        self.shortest_path = None
        self.visited = set()
        self.neighbours_dict = {}
        self.build_neighbours_dict()

    def build_grid(self):
        for y, row in enumerate(self.input):
            for x, letter in enumerate(row):
                self.grid[(x,y)] = letter
                if letter == "S":
                    self.S_pos = (x,y)
                if letter == "E":
                    self.E_pos = (x,y)
    
    def get_reachable_neighbours(self, pos):
        x,y = pos
        candidates = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        neighbours = []
        for n in candidates:
            if n in self.grid and self.height_dict[self.grid[n]] <= self.height_dict[self.grid[pos]] + 1:
                neighbours.append(n)

        return neighbours

    def build_neighbours_dict(self):
        for pos in self.grid:
            self.neighbours_dict[pos] = self.get_reachable_neighbours(pos)

    def dijkstra_shortest_path(self, starting_node=None):

        if starting_node is None:
            starting_node = self.S_pos

        # After googling for shortest distance algos
        # Ended up with Dijkstra's algorithm
        # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm
    
        # 1.
        # Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
        unvisited_set = set(self.grid.keys()) # All nodes

        # 2.
        # Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes.
        # Set the initial node as current.
        tentative_distance_dict = defaultdict(lambda: float("inf")) # Distance to Start
        tentative_distance_dict[starting_node] = 0 # Distance to Start
        current = starting_node # Start node

        # 3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances to the current node.
        while unvisited_set: # While there are still unvisited nodes (re-runs after #6 below)
            # 3. (cont.)
            # Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.
            for neighbour in self.neighbours_dict[current]: # We only consider reachable neighbours
                if neighbour in unvisited_set: # We only consider unvisited neighbours
                    tentative_distance_dict[neighbour] = min(tentative_distance_dict[neighbour], tentative_distance_dict[current] + 1) # For neighbours of the start node this will be min(inf,0+1) = 1, for neighbours of the neighbours of the start node this will be min(inf,1+1) = 2, etc.

            # 4.
            # When we are done considering all of the neighbors of the current node, mark the current node as visited and remove it from the unvisited set.
            unvisited_set.remove(current) # Already have distance to start for evey neighbour so no need to consider again

            # 5
            # If the destination node has been marked visited (when planning a route between two specific nodes) then stop. 
            # The algorithm has finished.
            if current == self.E_pos: # We have the shortest distance to the end node, as (as outlined in #6), we will always select the unvisited node that is marked with the smallest tentative distance on the next iteration
                break

            # 6
            # Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 3.
            current = min(unvisited_set, key=lambda x: tentative_distance_dict[x]) # Select the unvisited node that is marked with the smallest tentative distance

        return tentative_distance_dict[self.E_pos]

    def get_all_elevations(self, elevation):
        # get all points where elevation is equal to elevation
        all_points = []
        for pos in self.grid:
            if self.height_dict[self.grid[pos]] == self.height_dict[elevation]:
                all_points.append(pos)
        return all_points

# Part 1
grid = Grid(day_12_input)
print(grid.dijkstra_shortest_path())

# Part 2
all_starting_points = grid.get_all_elevations("a")
all_shortest_paths = []
for i,starting_point in enumerate(all_starting_points):
    all_shortest_paths.append(grid.dijkstra_shortest_path(starting_point))
    #print(f"{i+1}/{len(all_starting_points)}")
print(min(all_shortest_paths))

