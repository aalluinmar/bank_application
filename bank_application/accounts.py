
from services import utils
from services import constants


class Accounts():

    def __init__(self, account_type: str, user_id: int):
        self.existing_accounts = utils.read_json_file(constants.ACCOUNT_DETAILS_FILE)
        self.account_number = utils.generate_random_number(list(self.existing_accounts.keys()))
        self.account_type = account_type
        self.routing_number = "123456789"
        self.balance = 0.0
        self.user_id = user_id

    def create_account(self):
        self.existing_accounts[self.account_number] = {
            "account_type": self.account_type,
            "routing_number": self.routing_number,
            "balance": self.balance,
            "user_id": self.user_id
        }
        utils.write_json_file(constants.ACCOUNT_DETAILS_FILE, self.existing_accounts)


class AccountDetails():
    
    def __init__(self):
        self.existing_accounts = utils.read_json_file(constants.ACCOUNT_DETAILS_FILE)

    def get_account_details(self, account_number: int):
        current_account = self.existing_accounts.get(account_number, {})
        self.account_number = account_number
        self.account_type = current_account.get("account_type", None)
        self.routing_number = current_account.get("routing_number", None)
        self.balance = current_account.get("balance", 0.0)
        self.user_id = current_account.get("user_id", None)

    def get_account_balance(self, account_number: int):
        return self.existing_accounts.get(account_number, {}).get("balance", 0.0)

    def update_account_balance(self, account_number: int, amount: float):
        self.existing_accounts[account_number]["balance"] += float(amount)
        utils.write_json_file(constants.ACCOUNT_DETAILS_FILE, self.existing_accounts)
        return self.existing_accounts[account_number]["balance"]

    def delete_account(self, account_number: int):
        self.existing_accounts.pop(account_number)
        utils.write_json_file(constants.ACCOUNT_DETAILS_FILE, self.existing_accounts)
        return True

    def get_user_accounts(self, user_id: int):
        return {
            account_number: account
            for account_number, account in self.existing_accounts.items()
            if account.get("user_id") == user_id
        }

    def get_user_account_numbers(self, user_id):
        return [
            account_number
            for account_number, account in self.existing_accounts.items()
            if account.get("user_id") == user_id
        ]

    def get_account_user_id(self, account_number):
        return self.existing_accounts.get(account_number, {}).get("user_id", None)

    def get_account_routing_number(self, account_number):
        return self.existing_accounts.get(account_number, {}).get("routing_number", None)

    def get_account_type(self, account_number):
        return self.existing_accounts.get(account_number, {}).get("account_type", None)

    def display_account_details(self, account_number: int):
        account = {
            "Account Number": account_number,
            "Account Type": self.account_type,
            "Routing Number": self.routing_number,
            "Balance": self.balance,
            "User ID": self.user_id
        }
        utils.display_table(account, "Account Details", "vertical")
