import json
import time
import random

from typing import Any, List

from tabulate import tabulate


def loading_animation() -> None:
    print(" Loading", end="", flush=True)
    for _ in range(4):
        time.sleep(0.1601)
        print(".", end="", flush=True)
    print("\n")


def minimal_text() -> None:
    print("\n" + "*" * 50)
    print("  Welcome to The Great Bank".center(50))
    print("*" * 50)


def typewriter_effect(text: str, delay: float = 0.0080) -> None:
    """Displays text with a typewriter animation effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)  # Adjust speed of typewriter effect


def read_json_file(file_path: str) -> dict:
    # Read the json file and return the data
    with open(file_path, "r") as file:
        return json.load(file)


def write_json_file(file_path: str, data: dict) -> None:
    # Write the data to the json file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def fetch_digits_from_phone_number(phonenumber: str) -> str:
    # Fetch the digits from the phone number and get the last 10 digits
    return "".join([char for char in phonenumber if char.isdigit()])[-10:]


def generate_random_number(existing_numbers: List, start_range: int = 100000000, end_range: int = 999999999) -> int:
    # Generate a random 9 digit number which doesn't exist in the existing numbers list
    random_number = random.randint(start_range, end_range)
    while random_number in existing_numbers:
        random_number = random.randint(start_range, end_range)
    return random_number


def display_table(data: Any, heading: str, layout: str ="horizontal") -> None:
    """
    Displays data in a table format with a white border.
    :param data: List of dictionaries for horizontal format or a dictionary for vertical format
    :param heading: Heading for the table
    :param layout: "horizontal" or "vertical"
    :return: None
    """
    print(f"\n          \033[1;97m{heading}\033[0m \n")  # Bold white heading
    if layout == "horizontal":
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))

    elif layout == "vertical":
        formatted_data = [[f"\033[1;97m{key}\033[0m", value] for key, value in data.items()]
        print(tabulate(formatted_data, tablefmt="fancy_grid"))

    else:
        print("\033[91mInvalid layout type! Use 'horizontal' or 'vertical'.\033[0m")
