# -*- coding: utf-8 -*-

# ---------- MODULES ------------ #
import create_map as CM
import screen_manager as SM
import os
  
import shutil
term_x = shutil.get_terminal_size()[0]
term_y = shutil.get_terminal_size()[1] - 1

# ---------- SETTINGS ----------- #
cave_itr = 10000        # Number of cave iterations
pool_tries = 5          # Number of pools to attempt to create
pool_itr = 12           # Number of pool iterations

dialogue_height = 10     # height of bottom panel
stats_width = 30        # width of side panel


# -------- GAME FUNCTION -------- #
def main():
    stats = [
        "Pto",
        "HP: 23/23",
        "Str: 16",
        "Dex: 18",
        "Int: 14",
        "Wis: 16",
        "Cha: 17"
    ]
    dialogue = [
        "Narrator",
        "Test test test test test test test test test test..."
    ]
    starting_arena = CM.gen_arena(term_x - stats_width, term_y - dialogue_height, cave_itr, pool_tries, pool_itr) # create arena details
    SM.print_screen(starting_arena, stats, dialogue, term_x,term_y, dialogue_height, stats_width)
    response = input("Action: ")
    
main()