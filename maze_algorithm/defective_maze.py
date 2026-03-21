#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   defective_maze.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/21 12:17:31 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/21 12:38:48 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Optional

import numpy as np
import random

from test_display import debug_display


# *****************************************************************************
# *                        print_fortytwo()                                   *
# *             generates 42 if the size is large enough                      *


def print_fortytwo(grid: list[list[int]], finish: str,
                   width: int, height: int) -> list[list[int]]:

    if (width >= 11 and height >= 9):  # voir avec fleur🌻​ 11 \ 9

        w: int = int(round(((width - 7) / 2), 0))
        h: int = int(round(((height - 5) / 2), 0))

        paterns: list[tuple[int, int]] = [
            (0, 0), (1, 0), (1, 0), (0, 1), (0, 1), (1, 0), (1, 0),  # 4
            (-4, 2), (0, 1), (0, 1), (1, 0), (1, 0),  # 2
            (0, -1), (0, -1), (1, 0), (1, 0), (0, 1), (0, 1)]  # 2

        if (finish == "before"):
            for p in paterns:
                h += p[0]
                w += p[1]
                grid[h][w] = -1

        elif (finish == "after"):
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    if (grid[y][x] == -1):
                        grid[y][x] = 15

    return (grid)


# *****************************************************************************
# *                         look_neighbor()                                   *
# *  Check to see if the current position can move to an virgin square        *


def look_neighbor(grid: list[list[int]], x1: int, y1: int,
                  w: int, h: int, perfect: bool) -> list:

    x_axes: list[int] = [0, 1, 0, -1]
    y_axes: list[int] = [-1, 0, 1, 0]
    compass: list[str] = ["N", "E", "S", "W"]
    virgin_neighbor: list[str] = []

    for x, y, c in zip(x_axes, y_axes, compass):
        if (x1+x >= 0 and y1+y >= 0 and x1+x < w and y1+y < h
                and grid[y1+y][x1+x] == 15 and grid[y1+y][x1+x] != -1):

            virgin_neighbor.append(c)

    return (virgin_neighbor)


# *****************************************************************************
# *                         growing_tree()                                    *
# *         Generate the maze using the growing tree algorithm                *


def deficient_maze(grid: list[list[int]], width: int, height: int,
                   entry: tuple[int, int],
                   seed: Optional[str]) -> list[list[int]]:

    if seed:
        random.seed(seed)

    grid: list[list[int]] = print_fortytwo(grid, "before", width, height)

    x: int = entry[0]
    y: int = entry[1]
    back: int = -1
    parkour: list[tuple[int, int]] = [x, y]

    while (np.max(grid) == 15):
        neighbor: list[str] = look_neighbor(grid, x, y, width, height)
        print(neighbor)
        print(*grid, sep="\n")
        debug_display(grid, width, height, entry, (1, 1), (x, y))

        if (neighbor):
            dir: str = random.choice(neighbor)
            if (dir == "N"):
                grid[y][x] -= 1  # N
                y += -1
                grid[y][x] -= 4  # S

            elif (dir == "E"):
                grid[y][x] -= 2  # E
                x += 1
                grid[y][x] -= 8  # W

            elif (dir == "S"):
                grid[y][x] -= 4  # S
                y += 1
                grid[y][x] -= 1  # N

            elif (dir == "W"):
                grid[y][x] -= 8  # W
                x += -1
                grid[y][x] -= 2  # E
            parkour.append((x, y))

        else:
            parkour.pop()
            x, y = parkour[-1]
            back -= 1

    grid = print_fortytwo(grid, "after", width, height)
    return (grid)


# =============================================================================
# ============================== MAIN ========================================
# =============================================================================

def main() -> None:
    width = height = 10
    # width = 8
    # height = 6

    entry = (0, 0)
    finish = ((width - 1), (height - 1))

    grid = np.array([[15 for _ in range(width)] for _ in range(height)])

    grid = deficient_maze(grid, width, height, entry, False, "")
    print(*grid, sep="\n")

    debug_display(grid, width, height, entry, finish, entry)


if __name__ == "__main__":
    main()
