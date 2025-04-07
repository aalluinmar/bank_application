from typing import List
from tenacity import RetryError

from services import validations


# --------------------------------------------
# Constants
# --------------------------------------------

# User input fields with their prompts, validators, and error messages
USER_REGISTRATION_INPUT_FIELDS = [
    (
        "\nEnter your first name (Eg: John) - ",
        [validations.is_valid_first_name],
        ["\n      ❌ Invalid Input ❌  First name should be greater than 2 characters\n"]
    ),
    (
        "\nEnter your last name (Eg: Doe) - ",
        [validations.is_valid_last_name],
        ["\n     ❌ Invalid Input ❌  Last name should be greater than 1 characters\n"]
    ),
    (
        "\nEnter your username (Eg: john) - ",
        [validations.is_valid_username, validations.is_username_available],
        [
            "\n     ❌ Invalid Input ❌  Username should be greater than 4 characters\n",
            "\n      🤔 User already exists 🤔. Please try with a different username.\n"
        ]
    ),
    (
        "\nEnter your password (Eg: John@123) - ",
        [validations.is_valid_password],
        ["\n     ❌ Invalid Input ❌  Password should be greater than 8 characters\n"]
    ),
    (
        "\nEnter your email (Eg: john@gmail.com) - ",
        [validations.is_valid_email, validations.is_email_available],
        [
            "\n     ❌ Invalid Input ❌  Please enter a valid email\n",
            "\n      🤔 Email already exists 🤔. Please try with a different email.\n"
        ]
    ),
    (
        "\nEnter your phone number (Eg: +1 1234567890) - ",
        [validations.is_valid_phonenumber, validations.is_phonenumber_available],
        [
            "\n     ❌ Invalid Input ❌  Please enter a valid phone number\n",
            "\n      🤔 Phone number already exists 🤔. Please try with a different phone number.\n"
        ]
    ),
    (
        "\nEnter your address (Eg: 123, Main Street, New York, USA, 10001) - ",
        [validations.is_valid_address],
        ["\n     ❌ Invalid Input ❌  Please enter a valid address\n"]
    ),
]

# User login input fields with their prompts, validators, and error messages
USER_LOGIN_INPUT_FIELDS = [
    (
        "\nEnter your username (Eg: john) - ",
        [validations.is_valid_username],
        ["\n     ❌ Invalid Input ❌  Username should be greater than 4 characters\n"]
    ),
    (
        "\nEnter your password (Eg: John@123) - ",
        [validations.is_valid_password],
        ["\n     ❌ Invalid Input ❌  Password should be greater than 8 characters\n"]
    ),
]

# Account type input fields with their prompts, validators, and error messages
ACCOUNT_TYPE_INPUT_FIELDS = [
        (
            "\nEnter the account type (Eg: Savings/Checking) - ",
            [validations.is_valid_account_type],
            ["\n     ❌ Invalid Input ❌  Please enter a valid account type\n"]
        )
    ]


# --------------------------------------------
# Functions
# --------------------------------------------

def read_user_registration_details():
    """
    Read and validate user input details
    :return: firstname, lastname, username, password, email, phonenumber, address
    """
    return read_input_details(USER_REGISTRATION_INPUT_FIELDS)


def read_user_login_details():
    """
    Read and validate user login details
    :return: username, password
    """
    return read_input_details(USER_LOGIN_INPUT_FIELDS)


def read_account_type_details():
    """
    Read and validate account type details
    :return: account_type
    """
    return read_input_details(ACCOUNT_TYPE_INPUT_FIELDS)


def read_input_details(input_fields: List):
    """
    Read and validate user input details
    :param input_fields: List of input fields with their prompts, validators_list, and error messages list
    :return: user inputs as a tuple
    """
    # Loop through input fields, validating each one
    inputs_list = []
    for prompt, validators_list, error_messages_list in input_fields:
        user_input = validations.get_valid_input(prompt, validators_list, error_messages_list)
        inputs_list.append(user_input)

    return tuple(inputs_list)
