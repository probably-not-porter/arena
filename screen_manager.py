# -*- coding: utf-8 -*-
from blocks import blocks

##########################################
#  Map                      #  Stats     #
#  Width: max - 20          #  Width: 20 #
#  height: max - 6          #            #
#                           #            #
#                           #            #
#                           #            #
#                           #            #
#                           #            #
##########################################
#  Dialogue                              #
#  Height: 6                             #
##########################################

border_color = '\033[00m\033[31m'
text_color = '\033[00m'
text_color_2 = '\033[00m\033[35m'

def print_screen(arena, stats, dialogue,x_dim,y_dim, dialogue_height, stats_width):
    # parse arena
    arena_p = []
    for row in arena:
        row_p = []
        for item in row:
            row_p.append(blocks[str(item)]["color"] + blocks[str(item)]["char"])
        arena_p.append(row_p)

    # create subscreens
    dia = render_dialogue(dialogue, x_dim, dialogue_height)
    stats = render_stats(stats, stats_width, y_dim - dialogue_height)

    # arrange
    out_arr = []
    for x in range(len(arena_p)):
        out_arr.append(arena_p[x] + stats[x])
    for row in dia:
        out_arr.append(row)

    for row in out_arr:
        row_out = ""
        for item in row:
            row_out += str(item)
        print(row_out)

            

def render_dialogue(text, x,y):
    # create array
    out_arr = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(" ")
        out_arr.append(row)

    # render text
    for x in range(len(text)):
        stat = text[x]
        for j in range(len(stat)):
            char = stat[j]
            if x == 0:
                out_arr[x+1][j+3] = text_color_2 + char
            else:
                out_arr[x+1][j+3] = text_color + char

    # create borders
    for x in range(len(out_arr[-1])):
        out_arr[-1][x] = border_color + "%"
    for x in range(len(out_arr)):
        out_arr[x][0] = border_color + "%"
    for x in range(len(out_arr)):
        out_arr[x][-1] = border_color + "%"

    return out_arr

def render_stats(text, x,y):
    out_arr = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(" ")
        out_arr.append(row)

    # render text
    for x in range(len(text)):
        stat = text[x]
        for j in range(len(stat)):
            char = stat[j]
            out_arr[x+2][j+2] = text_color + char
        
    
    # create borders
    for x in range(len(out_arr[-1])):
        out_arr[-1][x] = border_color + "%"
    for x in range(len(out_arr[0])):
        out_arr[0][x] = border_color + "%"
    for x in range(len(out_arr)):
        out_arr[x][-1] = border_color + "%"

    return out_arr
