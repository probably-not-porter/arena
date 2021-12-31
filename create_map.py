# -*- coding: utf-8 -*-

import random

# colors
class bcolors:
    CHAR = '\033[00m\033[5m\033[35m'
    BG = '\033[00m\033[90m'
    BORDER = '\033[00m\033[31m'
    ERR = '\033[00m'
    WATER = '\033[00m\033[34m'

# settings
wall_char = "▒"
blank_char = " "
fill_char = "█"
player_char = "@"
border_char = "%"
water_char = "▓"
water_edge_char = "░"
x_dim = 204
y_dim = 60


def print_arena(a):
    for line in a:
        outline = ""
        for square in line:
            if square == wall_char:
                outline += bcolors.BG + str(square)
            elif square == fill_char:
                outline += bcolors.BG + str(square)
            elif square == player_char:
                outline += bcolors.CHAR + str(square)
            elif square == border_char:
                outline += bcolors.BORDER + str(square)
            elif square == water_char:
                outline += bcolors.WATER + str(square)
            else:
                outline += bcolors.ERR + str(square)
        print(outline)

def gen_arena(board):
    # Caves
    for x in range(20):
        init_x = random.randint(1, len(board[0]) - 2)
        init_y = random.randint(1, len(board) - 2)
        squares = len(board) * len(board[0])

        
        mod_count = 1
        target_x = init_x
        target_y = init_y
        while mod_count < 800:
            mod_count += 1
            board[target_y][target_x] = blank_char
            seed = random.randint(1, 100)

            if (seed > 0 and seed <= 25) and target_x < len(board[0]) - 1:
                target_x = target_x + 1
            if (seed > 25 and seed <= 50) and target_x > 0:
                target_x = target_x - 1
            if (seed > 50 and seed <= 75) and target_y < len(board) - 1:
                target_y = target_y + 1
            if (seed > 75 and seed <= 100) and target_y > 0:
                target_y = target_y - 1

    

    # Walls
    for y in range(len(board)):
        for x in range(len(board[y])):
            target = board[y][x]
            if target != blank_char:
                if y > 0:
                    if board[y-1][x] == blank_char:
                        board[y][x] = wall_char
                if y < len(board) - 1:
                    if board[y+1][x] == blank_char:
                        board[y][x] = wall_char
                if x > 0:
                    if board[y][x-1] == blank_char:
                        board[y][x] = wall_char
                if x < len(board[0]) - 1:
                    if board[y][x+1] == blank_char:
                        board[y][x] = wall_char
    # Pools
    pools = []
    orig_pools = []
    for x in range(5): # create pools (up to 10)
        point_x = random.randint(1, len(board[0]) - 2)
        point_y = random.randint(1, len(board) - 2)
        if board[point_y][point_x] == blank_char:
            pools.append([point_y, point_x])
            orig_pools.append([point_y, point_x])
    
    for x in range(8):
        new_pools = []
        for pool in orig_pools:
            seed = random.randint(1, 100)

            if (seed > 0 and seed <= 25) and board[pool[0] - 1][pool[1]] == blank_char:
                pools.append([pool[0] - 1, pool[1]])
                if (random.randint(1, 100) > 50):
                    new_pools.append([pool[0] - 1, pool[1]])
            if (seed > 25 and seed <= 50) and board[pool[0] + 1][pool[1]] == blank_char:
                pools.append([pool[0] + 1, pool[1]])
                if (random.randint(1, 100) > 50):
                    new_pools.append([pool[0] + 1, pool[1]])
            if (seed > 50 and seed <= 75) and board[pool[0]][pool[1] - 1] == blank_char:
                pools.append([pool[0], pool[1] - 1])
                if (random.randint(1, 100) > 50):
                    new_pools.append([pool[0], pool[1] - 1])
            if (seed > 75 and seed <= 100) and board[pool[0]][pool[1] + 1] == blank_char:
                pools.append([pool[0], pool[1] + 1])
                if (random.randint(1, 100) > 50):
                    new_pools.append([pool[0], pool[1] + 1])
        orig_pools = orig_pools + new_pools
    
    for pool in pools:
        board[pool[0]][pool[1]] = water_char

    # Borders
    for line in board:
        line[0] = border_char
        line[-1] = border_char
    for x in range(len(board[0])):
        board[0][x] = border_char
        board[-1][x] = border_char

    board[init_y][init_x] = player_char
    return board

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