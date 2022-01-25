# Arena

Intended to simulate a DnD 3.5 rules-based environment with as much proceedural generation as possible.

All unique entities are defined in blocks.py with the following structure:
```
"item index number (int)": {
    "name": "Item Name, human readable",
    "color": "Item Color code",
    "char": "Char to draw on screen for item"
}
```

## Screen Manager
Organizes different panels of information (arrays of text) and arranges them for each draw frame.
```
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
```

## Create Map
Takes in a list of variables from the main logic loop to generate a small patch of dungeon terrain.

### Current Features:
- Caves with edges
- Pools with edges

### To be added:
- Monsters
- Furniture
- Tunnels
- Stairs (up/down)
- Lava
- Chest