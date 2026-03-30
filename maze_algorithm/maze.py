
import numpy as np

from abc import ABC, abstractmethod


class MazeGenerator(ABC):
    def __init__(self, width: int, height: int,
                 entry: tuple[int], finish: tuple[int],
                 perfect: bool, seed: str) -> None:

        grid = np.array([[15 for _ in range(width)] for _ in range(height)])

        self.width = width
        self.height = height
        self.entry = entry
        self.finish = finish
        self.perfect = perfect
        self.seed = seed
        self.grid = grid

    @abstractmethod
    def print_fortytwo(self) -> list[list[int]]:

        width_int = int(self.width)
        height_int = int(self.height)

        if (width_int >= 11 and height_int >= 9):

            w: int = int(round(((self.width - 7) / 2), 0))
            h: int = int(round(((self.height - 5) / 2), 0))

            paterns: list[tuple[int, int]] = [
                (0, 0), (1, 0), (1, 0), (0, 1), (0, 1), (1, 0), (1, 0),  # 4
                (-4, 2), (0, 1), (0, 1), (1, 0), (1, 0),  # 2
                (0, -1), (0, -1), (1, 0), (1, 0), (0, 1), (0, 1)]  # 2

            if (self.finish == "before"):
                for p in paterns:
                    h += p[0]
                    w += p[1]
                    self.grid[h][w] = -1

            elif (self.finish == "after"):
                for y in range(len(self.grid)):
                    for x in range(len(self.grid[y])):
                        if (self.grid[y][x] == -1):
                            self.grid[y][x] = 15

        return (self.grid)

    @abstractmethod
    def look_neighbor(self):
        pass
