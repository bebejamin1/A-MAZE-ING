#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   gen_output.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/20 09:02:11 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/25 13:33:30 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


# from bfs_algorithm import find_way

red = "\033[31m\033[5m\033[1m"
reset = "\033[0m"


def output(grid: list[list[int]], start: tuple[int], finish: tuple[int],
           way: list[str]):

    entry = f"{start[0]},{start[1]}"
    end = f"{finish[0]},{finish[1]}"

    try:
        with open("../output_maze.txt", "w") as f:
            for y, row in enumerate(grid):  # rangee
                for x, value in enumerate(row):
                    number = hex(value)[2:]
                    f.write(number)
                f.write("\n")
            f.write("\n")
            f.write(entry)
            f.write("\n")
            f.write(end)
            f.write("\n")
            for w in way:
                f.write(w)
    except (ValueError, AttributeError) as e:
        print(f"{red}[ERROR]{reset}: in gen_output.py {e}")
        exit()


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

    # way = find_way(grid, start, finish)
    way = ["N", "N", "W", "S", "W", "W", "E", "S", "D"]

    output(grid, start, finish, way)
