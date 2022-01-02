# -*- coding: utf-8 -*-
from blocks import blocks

def print_screen(arena):
    for row in arena:
        row_output = ""
        for block in row:
            row_output += blocks[str(block)]["color"] + blocks[str(block)]["char"]
        print(row_output)
