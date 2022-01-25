####################################################################                                                           
#     __     _ __    __    ___      __         _____   __  __      #
#   /'__`\  /\`'__\/'__`\/' _ `\  /'__`\      /\ '__`\/\ \/\ \     #
#  /\ \L\.\_\ \ \//\  __//\ \/\ \/\ \L\.\_  __\ \ \L\ \ \ \_\ \    #
#  \ \__/.\_\\ \_\\ \____\ \_\ \_\ \__/.\_\/\_\\ \ ,__/\/`____ \   #
#   \/__/\/_/ \/_/ \/____/\/_/\/_/\/__/\/_/\/_/ \ \ \/  `/___/> \  #
#                                                \ \_\     /\___/  #
#                                                 \/_/     \/__/   #
#  Porter Libby                                                    #
#  2021 - 2022                                                     #
#                                                                  #
####################################################################

# ---------- MODULES ------------ #
import os, sys, shutil, random
sys.path.insert(0, os.path.abspath(".."))

import scripts.create_map as CM
import scripts.screen_manager as SM

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
    game = True
    # Permanent settings
    race_ls = ["DWARF", "HUMAN", "ELF", "HALF-ORC", "HALFLING"]
    clas_ls = ["ROGUE", "FIGHTER", "CLERIC", "WIZARD", "BARD"]
    name = ""
    race = ""
    clas = ""
    stats = {
        "name":"",
        "race":"",
        "class":"",
        "level": 1,
        "str":"",
        "dex":"",
        "con":"",
        "int":"",
        "wis":"",
        "cha":"",
        "food": 5,
        "hp-max": 22,
        "hp-current": 22,
        "xp-max": 1000,
        "xp-current": 0,
    }
    arena = CM.gen_arena(term_x - stats_width, term_y - dialogue_height, cave_itr, pool_tries, pool_itr)


    # Print Welcome Screen
    dialogue = ["Welcome to Dungeon Arena v0.1", "(press enter to continue)"]
    SM.print_screen(arena, stats, dialogue, term_x,term_y, dialogue_height, stats_width)
    input(":\033[00m\033[35m")

    # Print Name Selection
    dialogue = ["Type a name for your character", "(Choose any combination of letters and numbers, enter to proceed)"]
    SM.print_screen(arena, stats, dialogue, term_x,term_y, dialogue_height, stats_width)
    name = input(":\033[00m\033[35m")
    stats["name"] = name.capitalize()

    # Print Race Selection
    while race.upper() not in race_ls:
        dialogue = ["Select a race for your character", "Options are Human, Elf, Drawf, Half-Orc, Halfling"]
        SM.print_screen(arena, stats, dialogue, term_x,term_y, dialogue_height, stats_width)
        race = input(":\033[00m\033[35m")
    stats["race"] = race.capitalize()

    # Print class Selection
    while clas.upper() not in clas_ls:
        dialogue = ["Select a class for your character", "Options are Rogue, Fighter, Cleric, Wizard, Bard"]
        SM.print_screen(arena, stats, dialogue, term_x,term_y, dialogue_height, stats_width)
        clas = input(":\033[00m\033[35m")
    stats["class"] = clas.capitalize()

    # Print Stat Gen
    std_arr = [15, 14, 13, 12, 10, 8]
    answer = 'REROLL'
    while answer.upper() != "ACCEPT":
        if answer.upper() == "REROLL":
            random.shuffle(std_arr)
        dialogue = ["Your lv1 stats have been auto-rolled for you.", "Str: " + str(std_arr[0]) + ", Dex: " + str(std_arr[1]) + ", Con: " + str(std_arr[2]) + ", Int: " + str(std_arr[3]) + ", Wis: " + str(std_arr[4]) +  ", Cha: " + str(std_arr[5]), "", "Type 'accept' to proceed or 'reroll' to roll again."]
        SM.print_screen(arena, stats, dialogue, term_x,term_y, dialogue_height, stats_width)
        answer = input(":\033[00m\033[35m")
    stats['str'] = std_arr[0]
    stats['dex'] = std_arr[1]
    stats['con'] = std_arr[2]
    stats['int'] = std_arr[3]
    stats['wis'] = std_arr[4]
    stats['cha'] = std_arr[5]

    # Dialogue Start
    dialogue = ["Narrator", "Now we can begin...", "", "If you need help at any point, use the 'help' command."]
    SM.print_screen(arena, stats, dialogue, term_x,term_y, dialogue_height, stats_width)
    

    ##### MAIN LOOP #####
    prev_dialogue = None
    while game == True:
        r = input("What will you do? \033[00m\033[35m")

        if r.upper() in ["NORTH", "N", "UP", "U"]:
            print("move")
        if r.upper() in ["SOUTH", "S", "DOWN", "D"]:
            print("move")
        if r.upper() in ["EAST", "E", "RIGHT", "R"]:
            print("move")
        if r.upper() in ["WEST", "W", "LEFT", "L"]:
            print("move")

        if r.upper() == "HELP":
            prev_dialogue = dialogue
            dialogue = [
                "~~~ HELP MENU ~~~      ('back' to exit help)",
                "north/n/up/u      to move up", 
                "south/s/down/d    to move down", 
                "east/e/right/r    to move right", 
                "west/w/left/l     to move left",
                "eat               consume 1 food, restore health",
            ]
        if r.upper() == "BACK":
            if prev_dialogue != None:
                dialogue = prev_dialogue
                prev_dialogue = None
        
        # render screen at the end of each loop
        SM.print_screen(arena, stats, dialogue, term_x,term_y, dialogue_height, stats_width) 
    
main()