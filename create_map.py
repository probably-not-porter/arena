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
player_char = "@"
border_char = "%"
x_dim = 50
y_dim = 50


def print_arena(a):
    for line in a:
        outline = ""
        for square in line:
            if square == wall_char:
                outline += bcolors.WARNING + str(square)
            elif square == fill_char:
                outline += bcolors.OKGREEN + str(square)
            elif square == player_char:
                outline += bcolors.OKBLUE + str(square)
            elif square == border_char:
                outline += bcolors.FAIL + str(square)
            else:
                outline += bcolors.OKCYAN + str(square)
        print(outline)

def gen_arena(input):
    init_x = random.randint(0, len(input[0]) - 1)
    init_y = random.randint(0, len(input) - 1)
    squares = len(input) * len(input[0])

    # Pathing 1
    mod_count = 1
    target_x = init_x
    target_y = init_y
    while mod_count < squares*2:
        mod_count += 1
        input[target_y][target_x] = blank_char
        seed = random.randint(1, 100)

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
    # Borders
    for line in input:
        line[0] = border_char
        line[-1] = border_char
    for x in range(len(input[0])):
        input[0][x] = border_char
        input[-1][x] = border_char

    input[init_y][init_x] = player_char
    return input

def main():
    template = []
    for y in range(y_dim):
        new_row = []
        for x in range(x_dim):
            new_row.append(fill_char)
        template.append(new_row)

    a = gen_arena(template)
    print_arena(a)

main()