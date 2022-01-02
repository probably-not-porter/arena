# -*- coding: utf-8 -*-

# ---------- MODULES ------------ #
import create_map as CM
import screen_manager as SM


# ---------- SETTINGS ----------- #
x_dim = 204
y_dim = 60


# -------- GAME FUNCTION -------- #
def main():
    starting_arena = CM.gen_arena(x_dim, y_dim) # create arena details
    SM.print_screen(starting_arena)
    
main()