"""
    Virtual die roll of size argument: int
    default 6
"""


from sys import argv
from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides) if self.sides > 0 else 0

if __name__ == '__main__':

    SIDES = 6 if len(argv) == 1 else int(argv[1])
    die = Die(SIDES)
    print(die.roll())
