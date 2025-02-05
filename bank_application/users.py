# This file contains the services related to user registration, login and user details

from services.retry_helpers import retry_wrapper
from services import constants, read_input_data, utils


class UserLoginService():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_details = utils.read_json_file(constants.USER_DETAILS_FILE)

    def validate_login(self):
        if self.username in self.user_details:
            return self.user_details[self.username]["password"] == self.password
        return False


class UserRegistrationService():

    def __init__(self, firstname: str, lastname: str, username: str, password: str, email: str, phonenumber: str, address: str):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.phonenumber = phonenumber
        self.address = address
        self.user_details = utils.read_json_file(constants.USER_DETAILS_FILE)

    def register_user(self):
        self.user_details[self.username] = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "password": self.password,
            "email": self.email,
            "phonenumber": self.phonenumber,
            "address": self.address
        }
        utils.write_json_file(constants.USER_DETAILS_FILE, self.user_details)


class UserDetails():

    def __init__(self, username, firstname=None, lastname=None, password=None, email=None, phonenumber=None, address=None):
        self.username = username
        self.user_details = utils.read_json_file(constants.USER_DETAILS_FILE)

        # Fetch the user details from the USER_DETAILS dictionary
        if self.username in self.user_details:
            self.firstname = self.user_details[self.username]["firstname"]
            self.lastname = self.user_details[self.username]["lastname"]
            self.password = self.user_details[self.username]["password"]
            self.email = self.user_details[self.username]["email"]
            self.phonenumber = self.user_details[self.username]["phonenumber"]
            self.address = self.user_details[self.username]["address"]
        else:
            self.firstname = firstname
            self.lastname = lastname
            self.password = password
            self.email = email
            self.phonenumber = phonenumber
            self.address = address


def read_and_validate_user_input_data():
    """
    Read and validate user input data
    :param: None
    :return: firstname, lastname, username, password, email, phonenumber, address
    """
    firstname, lastname, username, password, email, phonenumber, address = read_input_data.read_user_registration_details()

    user_registration_service = UserRegistrationService(
        firstname=firstname,
        lastname=lastname,
        username=username,
        password=password,
        email=email,
        phonenumber=phonenumber,
        address=address,
    )

    # Register the user
    user_registration_service.register_user()
    utils.typewriter_effect("\n     ✅ User registered successfully! 🎉\n\n")

    return firstname, lastname, username, password, email, phonenumber, address


@retry_wrapper(attempts=3)
def read_and_validate_user_login_data(user_login_details_entry_retry: int = 0):
    """
    Read and validate user login data
    :param user_login_details_entry_retry: Number of retries for user login data entry
    :return: username
    """
    username, password = read_input_data.read_user_login_details()

    # Validate the user login details
    if not UserLoginService(username, password).validate_login():
        utils.typewriter_effect("\n      😞 Login failed. Please check your credentials and try again.\n")
        raise ValueError("Invalid login credentials")  # This triggers a retry

    utils.typewriter_effect("\n\n      🎉 Login successful.\n\n")
    return username
