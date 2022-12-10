from aoc22_utils import read_input_file_without_trailing_newlines

day_9_input = read_input_file_without_trailing_newlines(9)

class Knot():

    def __init__(self, id):
        self.id = id
        self.x = 0
        self.y = 0
        self.before = None

    def move(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return f'Knot {self.id} at ({self.x}, {self.y})'

class Head(Knot):

    def __init__(self):
        super().__init__(0)
        self.after = 1
        self.before = None

    def move_one_step(self, direction):
        if direction == 'U':
            self.move(0, 1)
        elif direction == 'D':
            self.move(0, -1)
        elif direction == 'R':
            self.move(1, 0)
        elif direction == 'L':
            self.move(-1, 0)

    def __repr__(self):
        return f'Head {self.id} at ({self.x}, {self.y})'

class Tail(Knot):
    
        def __init__(self, id, Rope):
            super().__init__(id)
            self.before = self.id - 1 - 1 # -1 for 0-indexing, -1 for before (?)
            self.seen = set([(0,0)])
            self.rope = Rope
    
        def __repr__(self):
            return f'Tail {self.id} at ({self.x}, {self.y})'

        def need_to_move(self):

            if self.id == 1:
                #print(f'Checking if tail {self} needs to move towards head')
                # check against head
                if self.x == self.rope.head.x and self.y == self.rope.head.y: # overlap
                    return False
                elif self.x == self.rope.head.x and abs(self.y - self.rope.head.y) == 1: # adjacent in x
                    return False
                elif self.y == self.rope.head.y and abs(self.x - self.rope.head.x) == 1: # adjacent in y
                    return False
                elif abs(self.x - self.rope.head.x) <= 1 and abs(self.y - self.rope.head.y) <= 1: # diagonally adjacent
                    return False
                else: # not adjacent
                    return True

            # cases where tail is not the first tail
            #print(f'Checking if {self} needs to move towards {self.rope.tails[self.before]}')
            # check against tail before
            if self.x == self.rope.tails[self.before].x and self.y == self.rope.tails[self.before].y: # overlap
                return False
            elif self.x == self.rope.tails[self.before].x and abs(self.y - self.rope.tails[self.before].y) == 1: # adjacent in x
                return False
            elif self.y == self.rope.tails[self.before].y and abs(self.x - self.rope.tails[self.before].x) == 1: # adjacent in y
                return False
            elif abs(self.x - self.rope.tails[self.before].x) <= 1 and abs(self.y - self.rope.tails[self.before].y) <= 1: # diagonally adjacent
                return False
            else: # not adjacent
                return True

        def move_one_step_towards_before(self):
            if self.id == 1:
                if self.x == self.rope.head.x: # if in the same column
                    if self.y < self.rope.head.y: # if below head
                        self.move(0, 1)
                        return
                    elif self.y > self.rope.head.y: # if above head
                        self.move(0, -1)
                        return
                elif self.y == self.rope.head.y: # if in the same row
                    if self.x < self.rope.head.x: # if to the left of head
                        self.move(1, 0)
                        return
                    elif self.x > self.rope.head.x: # if to the right of head
                        self.move(-1, 0)
                        return
                else: # if not in the same row or column
                    if self.x < self.rope.head.x: # if to the left of head
                        self.move(1, 0)
                    if self.x > self.rope.head.x: # if to the right of head
                        self.move(-1, 0)
                    if self.y < self.rope.head.y: # if below head
                        self.move(0, 1)
                    if self.y > self.rope.head.y: # if above head
                        self.move(0, -1)
                    return

            else:
                if self.x == self.rope.tails[self.before].x:
                    if self.y < self.rope.tails[self.before].y:
                        self.move(0, 1)
                        return
                    elif self.y > self.rope.tails[self.before].y:
                        self.move(0, -1)
                        return
                elif self.y == self.rope.tails[self.before].y:
                    if self.x < self.rope.tails[self.before].x:
                        self.move(1, 0)
                        return
                    elif self.x > self.rope.tails[self.before].x:
                        self.move(-1, 0)
                        return
                else:
                    if self.x < self.rope.tails[self.before].x:
                        self.move(1, 0)
                    if self.x > self.rope.tails[self.before].x:
                        self.move(-1, 0)
                    if self.y < self.rope.tails[self.before].y:
                        self.move(0, 1)
                    if self.y > self.rope.tails[self.before].y:
                        self.move(0, -1)
                    return

        def update_seen(self):
            self.seen = self.seen.union({(self.x, self.y)})

class Rope():
    
    def __init__(self, instructions, num_knots):
        self.num_knots = num_knots
        self.instructions = instructions
        self.head = Head()
        self.tails = [Tail(i,self) for i in range(1, num_knots+1)]
        self.process_instructions()

    def move_head_one_step(self, direction):
        self.head.move_one_step(direction)
    
    def move(self, instruction):
        direction, distance = instruction[0], int(instruction[1:])
        for _ in range(distance):
            #print("--")
            #print(f'Moving head {self.head} {direction}')
            self.move_head_one_step(direction)
            #print(self.head)
            if self.tails[0].need_to_move():
                #print(f'Moving tail {self.tails[0]} towards {self.head}')
                self.tails[0].move_one_step_towards_before()
                self.tails[0].update_seen()
                #print(self.tails[0])
            for tail in self.tails[1:]:
                if tail.need_to_move():
                    #print(f'Moving tail {tail} towards {self.tails[tail.before]}')
                    tail.move_one_step_towards_before()
                    tail.update_seen()
                    #print(tail)

    
    def process_instructions(self):
        for instruction in self.instructions:
            self.move(instruction)

    def answer(self):
        return len(self.tails[-1].seen)

Part1 = Rope(day_9_input, 1)
Part2 = Rope(day_9_input, 9)

print(Part1.answer())
print(Part2.answer())

