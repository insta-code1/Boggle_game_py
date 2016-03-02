from random import choice
from string import ascii_uppercase

size = 2, 2

grid = {(x, y): choice(ascii_uppercase)
        for x in range(size[0])
        for y in
        range(size[1])}

print grid