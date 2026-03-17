import sys
from typing import Dict


def extract_config() -> Dict[str]:
    config = {}
    try:
        with open('config.txt', 'r', encoding="utf-8") as file:
            for line in file:
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=")
                    config[key] = value

        mandatory_keys = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", 
                          "PERFECT"]
        for key in mandatory_keys:
            if key not in config:
                print(f"Error: the key {key} is mising")
                sys.exit()

        return config

    except FileNotFoundError as e:
        print(f"Error: the file 'config.txt' is missing")
        sys.exit()

if __name__=="__main__":
    