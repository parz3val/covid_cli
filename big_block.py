from color_text import *

## Initiate color flags

initColorIt()

def big_block():
    for i in range(3):
        orange_block()

def one_block():
    print(color("#####################################################################",colors.WHITE))

def orange_block():
    print(color("############################################################################",colors.ORANGE))

def four_lines():
    print("\n\n\n\n")

def thank_you():
    four_lines()
    big_block()
    print("\t\t\t\tThank You")
    big_block()
    four_lines