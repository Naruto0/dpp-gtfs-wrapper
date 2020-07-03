# dpp-gtfs-wrapper
Project to get, preprocess and serve GTFS Prague public transport data in local database

## Using

[Pygtfs module](https://pygtfs.readthedocs.io/en/latest/)


## Start

Install

Create `.virtualenv`.
```
$ python -m "virtualenv" <name-of-venv>
```

activate it and install requirements

```
$ source <name-of-env>/bin/acitavate
$ pip install -r requirements.txt
```

run setup to migrate data to __sqlite3__ database

```
python backend/setup.py
```

Use ``pygtfs`` module mentioned above to fiddle with data