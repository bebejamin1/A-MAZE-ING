#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   bfs_algorithm.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/21 15:22:46 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/27 10:33:16 by bbeaurai           ###   ########.fr      #
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
    oposite: dict[str, str] = {"N": "S", "E": "W", "S": "N",
                               "W": "E", "Z": "Z"}
    virgin_neighbor: list[str] = []

    for x, y, c, b, bo in directions:
        nx, ny = x1 + x, y1 + y
        if (x1+x >= 0 and y1+y >= 0 and x1+x < w and y1+y < h
                and c != oposite[prec]
                and grid[y1][x1] & b == 0 and grid[ny][nx] & bo == 0):

            virgin_neighbor.append(c)

    return virgin_neighbor


def find_way(grid: list[list[int]], start: tuple[int],
             finish: tuple[int], width: int, height: int, ) -> list[str]:

    x, y = start
    prec = "Z"
    save_dir = ["Z"]
    save = [(x, y)]
    path = [(x, y)]
    mouv: list[str, tuple[int]] = {
        "N": (0, -1),
        "E": (1, 0),
        "S": (0, 1),
        "W": (-1, 0)
    }

    while (path[-1] != finish):

        neighbors = look_neighbor(grid, x, y, width, height, prec)

        if (len(neighbors) > 1):
            save.append((x, y))
            for direction in neighbors:
                while (len(neighbors) == 1):
                    neighbors = look_neighbor(grid, x, y, width, height, prec)

                    dir = mouv[neighbors]
                    x += dir[0]
                    y += dir[1]
                    path.append((x, y))

        if (len(neighbors) == 1):

        else:
            while (save[-1] != path[-1]):
                path.pop()
            while (len(save) > 2):
                del save[0]
                del save_dir[0]
            prec = save_dir[-1]
            x, y = path[-1]

    return (path)


if __name__ == "__main__":

    grid = [
        [11,  9,  5,  3,  9,  1,  5,  5,  5,  7],
        [12,  6, 11, 10, 14, 12,  5,  5,  5,  3],
        [13,  5,  2, 12,  5,  5,  5,  5,  5,  2],
        [9,  3, 10,  9,  5,  1,  7,  9,  5,  6],
        [10, 12,  6, 10,  9,  6,  9,  6,  9,  3],
        [8,  5,  3, 10, 12,  3, 10,  9,  6, 10],
        [10, 11, 12,  6, 11, 12,  6, 10, 11, 10],
        [10,  8,  5,  3, 12,  5,  1,  6, 10, 10],
        [10, 12,  3, 12,  5,  3, 10, 11,  8,  6],
        [12,  5,  6, 13,  5,  4,  6, 12,  4,  7],

    ]

    width = height = 10

    start = (0, 0)
    finish = (9, 9)

    debug_display(grid, width, height, start, finish, (0, 0))
    way = find_way(grid, start, finish, width, height)
    debug_display(grid, width, height, start, finish, (0, 0), way)
