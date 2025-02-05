import os


# Get the file paths for the data files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Check if the data directory exists
if not os.path.exists(DATA_DIR):
    raise FileNotFoundError(f"Data directory not found: {DATA_DIR}")


# Define the file paths for the data files
USER_DETAILS_FILE = os.path.join(DATA_DIR, "users.json")
ACCOUNT_DETAILS_FILE = os.path.join(DATA_DIR, "accounts.json")
TRANSACTION_DETAILS_FILE = os.path.join(DATA_DIR, "transactions.json")
