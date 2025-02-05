# Description: This file contains the main entry point of the bank application.

from services import utils
from users import (
    UserDetails,
    read_and_validate_user_input_data,
    read_and_validate_user_login_data
)


def initiate_bank_application_process(invalid_user_input_retry: int = 0):
    """
    Initiate the bank application process
    :param invalid_user_input_retry (Optional): Number of retries for invalid user input
    :return: None
    """
    utils.typewriter_effect("\n Are you an existing customer? (Enter Y/N) - ")
    user_input = input().lower()

    if user_input == "y":
        utils.typewriter_effect("\n\n ----- Please enter your login details ----- \n")
        user_login_details = UserDetails(read_and_validate_user_login_data())

    elif user_input == "n":
        utils.typewriter_effect("\n Would you like to create an account? (Enter Y/N) - ")
        account_creation_input = input().lower()

        if account_creation_input == "y":
            utils.typewriter_effect("\n\n ----- Please enter your details to create an account ----- \n")
            user_login_details = UserDetails(read_and_validate_user_input_data())

        elif account_creation_input == "n":
            utils.typewriter_effect("\n\n      Thank you for visiting. Have a great day! 😊🌟\n\n\n")
            exit()

        else:
            utils.typewriter_effect("\n\n      😞Invalid input😞. Please enter Y/N\n\n")
            initiate_bank_application_process(invalid_user_input_retry)

    else:
        utils.typewriter_effect("\n\n            😞Invalid input😞. Please enter Y/N\n\n")
        invalid_user_input_retry += 1
        if invalid_user_input_retry < 3:
            initiate_bank_application_process(invalid_user_input_retry)
        else:
            utils.typewriter_effect("\n     😞You have exceeded the maximum number of retries. Exiting the application.😞\n\n")
            exit()


if __name__ == "__main__":
    # Display the welcome message
    utils.loading_animation()
    utils.minimal_text()

    # Initiate the bank application process
    initiate_bank_application_process()
