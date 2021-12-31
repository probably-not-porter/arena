import random

# colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# settings
wall_char = "#"
blank_char = " "
fill_char = "."
x_dim = 100
y_dim = 100


def print_arena(a):
    for line in a:
        outline = ""
        for square in line:
            if square == wall_char:
                outline += bcolors.WARNING + str(square)
            elif square == fill_char:
                outline += bcolors.OKGREEN + str(square)
            else:
                outline += bcolors.OKCYAN + str(square)
        print(outline)

def gen_arena(input):
    squares = len(input) * len(input[0])

    # Pathing 1
    mod_count = 1
    target_x = random.randint(0, len(input[0]) - 1)
    target_y = random.randint(0, len(input) - 1)
    while mod_count < squares*2:
        mod_count += 1
        input[target_y][target_x] = blank_char
        seed = random.randint(1, 100)

        """
        if (seed > 0 and seed <= 12.5) and target_x > 0 and target_y > 0:
            target_x = target_x - 1
            target_y = target_y - 1
        if (seed > 12.5 and seed <= 25) and target_x < len(input[0]) - 1 and target_y < len(input) - 1:
            target_x = target_x + 1
            target_y = target_y + 1
        if (seed > 25 and seed <= 37.5) and target_x > 0 and target_y < len(input) - 1:
            target_x = target_x - 1
            target_y = target_y + 1
        if (seed > 37.5 and seed <= 50) and target_x < len(input[0]) - 1 and target_y > 0:
            target_x = target_x + 1
            target_y = target_y - 1
        """

        if (seed > 50 and seed <= 62.5) and target_x < len(input[0]) - 1:
            target_x = target_x + 1
        if (seed > 62.5 and seed <= 75) and target_x > 0:
            target_x = target_x - 1
        if (seed > 75 and seed <= 87.5) and target_y < len(input) - 1:
            target_y = target_y + 1
        if (seed > 87.5 and seed <= 100) and target_y > 0:
            target_y = target_y - 1

    # Walling
    for y in range(len(input)):
        for x in range(len(input[y])):
            target = input[y][x]
            if target != blank_char:
                if y > 0:
                    if input[y-1][x] == blank_char:
                        input[y][x] = wall_char
                if y < len(input) - 1:
                    if input[y+1][x] == blank_char:
                        input[y][x] = wall_char
                if x > 0:
                    if input[y][x-1] == blank_char:
                        input[y][x] = wall_char
                if x < len(input[0]) - 1:
                    if input[y][x+1] == blank_char:
                        input[y][x] = wall_char
    return input


template = []
for y in range(y_dim):
    new_row = []
    for x in range(x_dim):
        new_row.append(fill_char)
    template.append(new_row)

a = gen_arena(template)
print_arena(a)