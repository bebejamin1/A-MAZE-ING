#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   bfs_algorithm.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/21 15:22:46 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/25 15:53:06 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any

import random

from test_display import debug_display

red = "\033[31m"
reset = "\033[0m"


def look_neighbor(grid: list[list[int]], x1: int, y1: int,
                  w: int, h: int, prec: str) -> list:

    directions: list[tuple[Any]] = [(0, -1, "N", 1, 4), (1, 0, "E", 2, 8),
                                    (0, 1, "S", 4, 1), (-1, 0, "W", 8, 2)]
    oposite = {"N": "S", "E": "W", "S": "N", "W": "E", "Z": "Z"}
    virgin_neighbor: list[str] = []

    for x, y, c, b, bo in directions:
        nx, ny = x1 + x, y1 + y

        if (c != oposite[prec] and grid[y][x] & b == 0
                and grid[ny][nx] & bo == 0):

            virgin_neighbor.append(c)

    return (virgin_neighbor)


# algorithme bfs
def find_way(grid: list[list[int]], start: tuple[int],
             finish: tuple[int], width: int, height: int, ) -> list[str]:

    prec = "Z"
    save_dir = "Z"
    save = (0, 0)
    x, y = start
    path = [(x, y)]
    mouv: list[str, tuple[int]] = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }

    while (path[-1] != finish):

        neighbors = look_neighbor(grid, x, y, width, height, prec)
        print(neighbors)
        if (neighbors):
            direction = random.choice(neighbors)
            prec = direction

            dir = mouv[direction]
            x += dir[0]
            y += dir[1]
            path.append((x, y))

            if (len(neighbors) > 1):
                save = (x, y)
                save_dir = direction

        else:
            print(f"{red}[NOOON]{reset}")
            while (path[-1] != save):
                path.pop()
            prec = save_dir
            x, y = path[-1]

        debug_display(grid, 15, 15, start, finish, (x, y))

    return (path)


if __name__ == "__main__":

    grid = [
        [11,  9,  3, 13,  1,  3, 11,  9,  5,  5,  1,  5,  5,  5,  3],
        [10, 10, 10,  9,  6, 10, 10,  8,  5,  7, 12,  3, 13,  3, 10],
        [12,  6, 10, 10, 11, 10, 12,  6,  9,  5,  3, 12,  3, 10, 10],
        [11,  9,  6, 10,  8,  6,  9,  3, 10, 11, 12,  5,  6, 10, 10],
        [10, 12,  3, 10, 12,  5,  6,  8,  6, 12,  5,  1,  5,  6, 10],
        [8,  5,  6, 10, 15,  9,  7, 10, 15, 15, 15,  8,  5,  5,  6],
        [12,  3, 13,  2, 15, 12,  5,  0,  5,  7, 15, 10, 13,  1,  3],
        [11, 12,  3, 10, 15, 15, 15, 10, 15, 15, 15, 12,  5,  6, 10],
        [8,  7, 10, 12,  5,  3, 15, 10, 15, 13,  5,  1,  5,  3, 10],
        [8,  5,  6,  9,  5,  6, 15, 14, 15, 15, 15, 14,  9,  2, 10],
        [12,  3, 13,  4,  5,  5,  5,  5,  5,  5,  3,  9,  6, 14, 10],
        [9,  6,  9,  5,  5,  5,  5,  5,  5,  3, 10, 12,  3,  9,  6],
        [12,  3,  8,  3, 11,  9,  5,  5,  3, 10, 12,  3, 10, 12,  3],
        [11, 10, 14, 10,  8,  6,  9,  3, 12,  6,  9,  6,  8,  7, 10],
        [12,  4,  5,  6, 12,  5,  6, 12,  5,  5,  6, 13,  4,  5,  6],
    ]

    start = (0, 0)
    finish = (14, 14)

    debug_display(grid, 15, 15, start, finish, (0, 0))
    way = find_way(grid, start, finish, 15, 15)
    print(way)
    debug_display(grid, 15, 15, start, finish, (0, 0), way)
