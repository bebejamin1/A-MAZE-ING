#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   test_display.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/20 10:52:30 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/20 11:15:09 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def debug_display(grid: list[list[int]], width: int, height: int,
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
