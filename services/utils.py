import json
import time


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
