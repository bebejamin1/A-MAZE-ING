#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   test_display.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/20 10:52:30 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/20 16:58:03 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def debug_display(
    grid: list[list[int]],
    width: int,
    height: int,
    start: tuple[int, int],
    end: tuple[int, int],
    current: tuple[int, int] | None = None,
    path: list[tuple[int, int]] | None = None) -> None:

    # Configuration des styles (ANSI colors)
    WALL = "██"
    SPACE = "  "
    C_START = "\033[92mS \033[0m"  # Vert
    C_END   = "\033[94mF \033[0m"  # Bleu (EXIT)
    C_CURR  = "\033[93mX \033[0m"  # Jaune (Position actuelle)
    C_PATH  = "\033[91m··\033[0m"  # Rouge (Chemin)

    # 1. Initialisation de la grille étendue remplie de murs
    disp = [[WALL for _ in range(2 * width + 1)] for _ in range(2 * height + 1)]

    # 2. Sculpture des passages et des murs
    for y in range(height):
        for x in range(width):
            nx, ny = 2 * x + 1, 2 * y + 1
            disp[ny][nx] = SPACE  # La cellule elle-même

            val = grid[y][x]
            # On ouvre les murs si le bit correspondant est à 0
            if not (val & 1): disp[ny - 1][nx] = SPACE  # Nord
            if not (val & 2): disp[ny][nx + 1] = SPACE  # Est
            if not (val & 4): disp[ny + 1][nx] = SPACE  # Sud
            if not (val & 8): disp[ny][nx - 1] = SPACE  # Ouest

    # 3. Marquage du chemin (Path)
    if path:
        for i, (px, py) in enumerate(path):
            rx, ry = 2 * px + 1, 2 * py + 1
            # Ne pas écraser Start/End/Current avec les points du chemin
            if disp[ry][rx] == SPACE:
                disp[ry][rx] = C_PATH

            # Relier les points du chemin entre eux pour une ligne continue
            if i < len(path) - 1:
                next_x, next_y = path[i+1]
                bx, by = rx + (next_x - px), ry + (next_y - py)
                disp[by][bx] = C_PATH

    # 4. Marquage des points spéciaux (Prioritaires)
    disp[2 * start[1] + 1][2 * start[0] + 1] = C_START
    disp[2 * end[1] + 1][2 * end[0] + 1] = C_END
    if current:
        disp[2 * current[1] + 1][2 * current[0] + 1] = C_CURR

    # 5. Affichage final
    print("\n" + "═" * (width * 4))
    for row in disp:
        print("".join(row))
    print("═" * (width * 4) + "\n")
