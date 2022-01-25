# -*- coding: utf-8 -*-
import random

def gen_arena(x_dim, y_dim, cave_itr, pool_tries, pool_itr):
    board = []

    for y in range(y_dim):
        new_row = []
        for x in range(x_dim):
            new_row.append(2) # wall middle fill
        board.append(new_row)

    # Caves
    for x in range(1):
        init_x = random.randint(1, len(board[0]) - 2)
        init_y = random.randint(1, len(board) - 2)
        squares = len(board) * len(board[0])

        
        mod_count = 1
        target_x = init_x
        target_y = init_y
        while mod_count < cave_itr:
            mod_count += 1
            board[target_y][target_x] = 0 # blank square
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
            if target != 0:
                if y > 0:
                    if board[y-1][x] == 0:
                        board[y][x] = 1 # wall edge
                if y < len(board) - 1:
                    if board[y+1][x] == 0:
                        board[y][x] = 1 # wall edge
                if x > 0:
                    if board[y][x-1] == 0:
                        board[y][x] = 1 # wall edge
                if x < len(board[0]) - 1:
                    if board[y][x+1] == 0:
                        board[y][x] = 1 # wall edge
    # Pools
    pools = []
    orig_pools = []
    for x in range(pool_tries):
        point_x = random.randint(1, len(board[0]) - 2)
        point_y = random.randint(1, len(board) - 2)
        if board[point_y][point_x] == 0:
            pools.append([point_y, point_x])
            orig_pools.append([point_y, point_x])
    
    for x in range(pool_itr):
        new_pools = []
        for pool in orig_pools:
            seed = random.randint(1, 100)

            if (seed > 0 and seed <= 25) and board[pool[0] - 1][pool[1]] == 0:
                pools.append([pool[0] - 1, pool[1]])
                if (random.randint(1, 100) > 50):
                    new_pools.append([pool[0] - 1, pool[1]])
            if (seed > 25 and seed <= 50) and board[pool[0] + 1][pool[1]] == 0:
                pools.append([pool[0] + 1, pool[1]])
                if (random.randint(1, 100) > 50):
                    new_pools.append([pool[0] + 1, pool[1]])
            if (seed > 50 and seed <= 75) and board[pool[0]][pool[1] - 1] == 0:
                pools.append([pool[0], pool[1] - 1])
                if (random.randint(1, 100) > 50):
                    new_pools.append([pool[0], pool[1] - 1])
            if (seed > 75 and seed <= 100) and board[pool[0]][pool[1] + 1] == 0:
                pools.append([pool[0], pool[1] + 1])
                if (random.randint(1, 100) > 50):
                    new_pools.append([pool[0], pool[1] + 1])
        orig_pools = orig_pools + new_pools
    
    for pool in pools:
        board[pool[0]][pool[1]] = 5 # water block
    for pool in pools:
        if board[pool[0] - 1][pool[1]] != 5 and board[pool[0] - 1][pool[1]] != 6:
            board[pool[0]][pool[1]] = 6 # water edge block
        if board[pool[0] + 1][pool[1]] != 5 and board[pool[0] + 1][pool[1]] != 6:
            board[pool[0]][pool[1]] = 6 # water edge block
        if board[pool[0]][pool[1] - 1] != 5 and board[pool[0]][pool[1] - 1] != 6:
            board[pool[0]][pool[1]] = 6 # water edge block
        if board[pool[0]][pool[1] + 1] != 5 and board[pool[0]][pool[1] + 1] != 6:
            board[pool[0]][pool[1]] = 6 # water edge block

    # Borders
    for line in board:
        line[0] = 4 # border
        line[-1] = 4 # border
    for x in range(len(board[0])):
        board[0][x] = 4 # border
        board[-1][x] = 4 # border

    board[init_y][init_x] = 3 # player
    return board