from backend.helpers import *
from backend.checks import run_check

# TODO: modify setup to handle updates of source data

if __name__ == '__main__':
    retrieve_data()
    run_check()
    update_database()
