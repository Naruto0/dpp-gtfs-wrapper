from backend.helpers import retrieve_data, update_database
from backend.checks import run_check

# TODO: modify setup to handle updates of source data

if __name__ == "__main__":
    retrieve_data()
    run_check()
    update_database()
