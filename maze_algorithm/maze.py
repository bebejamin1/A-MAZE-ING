#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   maze.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/18 11:31:23 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/20 09:19:23 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from typing import Optional
import numpy as np
import random


def look_neighbor(grid: list[list[int]], x1: int, y1: int,
                  w: int, h: int) -> list:

    x_axes = [0, 1, 0, -1]
    y_axes = [-1, 0, 1, 0]
    compass = ["N", "E", "S", "W"]
    virgin_neighbor = []

    for x, y, c in zip(x_axes, y_axes, compass):
        if (x1+x >= 0 and y1+y >= 0 and x1+x < w and y1+y < h
                and grid[y1+y][x1+x] == 15):

            virgin_neighbor.append(c)

    return (virgin_neighbor)


def maze(grid: list[list[int]], width: int, height: int,
         entry: tuple[int, int], perfect: bool,
         seed: Optional[str]) -> list[list[int]]:

    x1, y1 = entry
    n, e, s, w = 1, 2, 4, 8
    back = -1
    parkour = []

    while (np.max(grid) == 15):

        test: list[str] = look_neighbor(grid, x1, y1, width, height)

        if (test):
            back = -1
            dir = random.choice(test)
            if (dir == "N"):
                grid[y1][x1] -= n  # N
                y1 += -1
                grid[y1][x1] -= s  # S

            elif (dir == "E"):
                grid[y1][x1] -= e  # E
                x1 += 1
                grid[y1][x1] -= w  # W

            elif (dir == "S"):
                grid[y1][x1] -= s  # S
                y1 += 1
                grid[y1][x1] -= n  # N

            elif (dir == "W"):
                grid[y1][x1] -= w  # W
                x1 += -1
                grid[y1][x1] -= e  # E
            parkour.append((x1, y1))

        else:
            x1, y1 = parkour[back][0], parkour[back][1]
            back -= 1

        # print(test_display(grid, width, height, entry, finish, (x1, y1)))

    return (grid)


def test_display(grid: list[list[int]], width: int, height: int,
                 start: tuple[int, int], end: tuple[int, int],
                 current: tuple[int, int]) -> None:
    """
    Affiche la matrice avec les points stratégiques du sujet.
    S = Start (ENTRY), F = Finish (EXIT), X = Current Position.
    """
    # Configuration visuelle
    WALL = "██"  # Double bloc pour l'épaisseur
    SPACE = "  "
    C_START = "\033[92mS \033[0m"  # Vert
    C_END = "\033[91mF \033[0m"    # Rouge
    C_CURR = "\033[93mX \033[0m"   # Jaune (Position actuelle)

    # Création de la grille d'affichage (2W+1 x 2H+1)
    disp = [[WALL for _ in range(2 * width + 1)]
            for _ in range(2 * height + 1)]

    for y in range(height):
        for x in range(width):
            val = grid[y][x]
            # Coordonnées dans la grille étendue
            dx, dy = 2 * x + 1, 2 * y + 1

            # 1. Déterminer le contenu de la cellule
            if (x, y) == current:
                disp[dy][dx] = C_CURR
            elif (x, y) == start:
                disp[dy][dx] = C_START
            elif (x, y) == end:
                disp[dy][dx] = C_END
            else:
                disp[dy][dx] = SPACE

            # 2. Ouvrir les murs (si le bit est à 0, le mur est ouvert)
            if not (val & 1): disp[dy - 1][dx] = SPACE  # noqa
            if not (val & 2): disp[dy][dx + 1] = SPACE  # noqa
            if not (val & 4): disp[dy + 1][dx] = SPACE  # noqa
            if not (val & 8): disp[dy][dx - 1] = SPACE  # noqa

    # Rendu final
    for row in disp:
        print("".join(row))


def main() -> None:
    width = height = 10
    x1, x2 = random.randint(0, (width - 1)), random.randint(0, (width - 1))
    y1, y2 = random.randint(0, (height - 1)), random.randint(0, (height - 1))
    entry = (x1, y1)
    finish = (x2, y2)
    grid = np.array([[15 for _ in range(width)] for _ in range(height)])
    print("Grille:", grid.shape)

    maze_finish = maze(grid, width, height, entry, True, "")
    print(*maze_finish, sep="\n")

    test_display(maze_finish, width, height, entry, finish, entry)


if __name__ == "__main__":
    main()
