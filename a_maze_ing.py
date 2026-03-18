import sys
from typing import Dict
from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator, model_validator, ValidationError


class MazeConfig(BaseModel):
    WIDTH: int = Field(gt=1, le=100)
    HEIGHT: int = Field(gt=1, le=100)
    ENTRY: str
    EXIT: str
    OUTPUT_FILE: str
    PERFECT: bool

    @field_validator("ENTRY", "EXIT")
    @classmethod
    def check_coordinates_format(cls, value) -> str:
        parts = value.split(",")
        if len(parts) != 2:
            raise ValueError("Coordinates must be 'x,y' format")
        return value

    @model_validator(mode="after")
    def validate_maze(self) -> Self:
        x, y = map(int, self.ENTRY.split(","))
        x2, z2 = map(int, self.EXIT.split(","))

        if self.WIDTH * self.HEIGHT < 4:
            raise ValueError("Maze dimensions must be at least 2x2.")
        if not (0 <= x < self.WIDTH and 0 <= y < self.HEIGHT):
            raise ValueError("ENTRY coordinates are out of bounds.")
        if not (0 <= x2 < self.WIDTH and 0 <= z2 < self.HEIGHT):
            raise ValueError("EXIT coordinates are out of bounds.")

        return self


def extract_config() -> Dict[str, str]:
    config = {}
    try:
        with open('config.txt', 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=")
                    config[key] = value

        mandatory_keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE",
                          "PERFECT"]
        for key in mandatory_keys:
            if key not in config:
                print(f"Error: the key {key} is missing")
                sys.exit()

        return config

    except FileNotFoundError:
        print("Error: the file 'config.txt' is missing")
        sys.exit()


if __name__ == "__main__":
    try:
        config_dict = extract_config()
        config = MazeConfig(**config_dict)

        print(f"Config validé: {config}")
        print(f"Entry: {config.ENTRY}, Exit: {config.EXIT}")

    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]["msg"])
        sys.exit()
