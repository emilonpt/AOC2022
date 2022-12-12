from aoc22_utils import read_input_file_without_trailing_newlines, split_input_list_on_empty_string
import math

day_11_input = read_input_file_without_trailing_newlines(11)

split_day_11_input = split_input_list_on_empty_string(day_11_input)

class Monkey():

    def __init__(self, monkey_data, worry_level_divisor=3):
        self.id = int(monkey_data[0].split(' ')[1].split(':')[0])
        self.items = [int(i) for i in monkey_data[1].split(': ')[1].split(', ')]
        self.operation_type = monkey_data[2].split(' old ')[1].split(' ')[0]
        try:
            self.operation_value = int(monkey_data[2].split(self.operation_type+" ")[1])
        except ValueError: # input where the operation_value is a string ('old')
            self.operation_value = monkey_data[2].split(self.operation_type+" ")[1]
        self.test_divisor = int(monkey_data[3].split('by ')[1])
        self.test_true_monkey_id = int(monkey_data[4].split('monkey ')[1])
        self.test_false_monkey_id = int(monkey_data[5].split('monkey ')[1])
        self.num_inspected_items = 0
        self.worry_level_divisor = worry_level_divisor
        self.is_part_2 = worry_level_divisor == 1
        self.is_part_1 = not self.is_part_2
    
    def __repr__(self):
        return "Monkey {}".format(self.id)

    def operate_on_item(self, item):

        op_value = self.operation_value if self.operation_value != 'old' else item

        operation_function = sum if self.operation_type == '+' else math.prod

        return operation_function([item, op_value])

    def inspect_items(self):
        to_remove = []
        for old in self.items:

            new = self.operate_on_item(old)

            if self.is_part_1:
                new = new // self.worry_level_divisor
            else:
                # for part 2 we can't just divide by the worry level divisor
                # but we still need to divide by something as otherwise
                # the numbers will get too big

                # we can divide by the product of all the divisors
                # as this will always be a multiple of all the divisors
                # and so will always give the same result
                # when calculating the remainder of test_divisor
                remainder = new % ALL_DIVISORS_MULTIPLIED
                if new > ALL_DIVISORS_MULTIPLIED:
                    new = ALL_DIVISORS_MULTIPLIED + remainder
                else:
                    new = remainder

            pass_test = new % self.test_divisor == 0

            if pass_test:

                target_monkey = MONKEY_LIST[self.test_true_monkey_id]

            else:
                    
                    target_monkey = MONKEY_LIST[self.test_false_monkey_id]

            target_monkey.items.append(new)
                
            to_remove.append(old)
            self.num_inspected_items += 1
        for i in to_remove:
            self.items.remove(i)

def process_rounds(num_rounds):
    for n in range(1, num_rounds+1):
        for i in range(len(MONKEY_LIST)):
            MONKEY_LIST[i].inspect_items()
        #print("Finished round {}.".format(n))
        #if n in [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
            #inspected_nums = get_num_inspected_items()
            #print("The top 2 monkeys have inspected {} and {} items.".format(sorted(inspected_nums.values())[-1], sorted(inspected_nums.values())[-2]))
def get_num_inspected_items():
    return {monkey.id: monkey.num_inspected_items for monkey in MONKEY_LIST}

# Part 1
MONKEY_LIST = [Monkey(i) for i in split_day_11_input]
process_rounds(20)
inspected_nums = get_num_inspected_items()
print(math.prod(sorted(inspected_nums.values())[-2:]))

# Part 2

MONKEY_LIST = [Monkey(i, 1) for i in split_day_11_input]
ALL_DIVISORS = [i.test_divisor for i in MONKEY_LIST]
ALL_DIVISORS_MULTIPLIED = math.prod(ALL_DIVISORS)

process_rounds(10000)
inspected_nums = get_num_inspected_items()
print(math.prod(sorted(inspected_nums.values())[-2:]))