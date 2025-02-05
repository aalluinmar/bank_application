import re

from typing import List

from services import constants, utils
from services.retry_helpers import retry_wrapper


# --------------------------------------------
# Constants
# --------------------------------------------

# Declare the regular expressions pattern
EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
PHONENUMBER_PATTERN = r"^\+?(\d{1,3})?[-. ]?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}$"


# --------------------------------------------
# Functions
# --------------------------------------------

def is_valid_first_name(firstname: str) -> bool:
    # Check if the first name is less than 2 characters
    return True if len(firstname) >= 2 else False


def is_valid_last_name(lastname: str) -> bool:
    # Check if the last name is less than 1 characters
    return True if len(lastname) >= 1 else False


def is_valid_username(username: str) -> bool:
    # Check if the username is less than 4 characters
    return True if len(username) >= 4 else False


def is_valid_password(password: str) -> bool:
    # Check if the password is less than 8 characters
    return True if len(password) >= 8 else False


def is_valid_email(email: str) -> bool:
    """Validate email format with support for subdomains (e.g., mail.uc.edu, gov.in)."""
    return re.match(EMAIL_PATTERN, email) is not None


def is_valid_phonenumber(phone: str) -> bool:
    """Validate phone numbers with or without country codes, spaces, dashes, and parentheses."""
    return re.fullmatch(PHONENUMBER_PATTERN, phone) is not None


def is_valid_address(address: str) -> bool:
    # Check if the address is less than 5 characters
    return True if len(address) >= 5 else False


def is_username_available(username: str, user_details = utils.read_json_file(constants.USER_DETAILS_FILE)):
    return username not in user_details


def is_email_available(email: str, user_details = utils.read_json_file(constants.USER_DETAILS_FILE)):
    for user in user_details.values():
        if user["email"] == email:
            return False
    return True


def is_phonenumber_available(phonenumber: str, user_details = utils.read_json_file(constants.USER_DETAILS_FILE)):
    # Fetch the digits from the phone number and check the last 10 digits with the existing phone numbers
    for user in user_details.values():
        if utils.fetch_digits_from_phone_number(user["phonenumber"]) == utils.fetch_digits_from_phone_number(phonenumber):
            return False
    return True


@retry_wrapper(attempts=3)
def get_valid_input(prompt: str, validators: List[callable], error_messages_list: List[str]) -> str:
    utils.typewriter_effect(prompt)
    user_input = input().strip()
    for index, validator in enumerate(validators):
        if not validator(user_input):
            utils.typewriter_effect(error_messages_list[index])
            raise ValueError(error_messages_list[index])
    return user_input
