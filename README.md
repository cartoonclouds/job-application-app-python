# job-application-app-python

https://wiki.gnome.org/Apps/Accerciser

!!! https://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html

## Packages

- orator https://orator-orm.com/
- colorama https://github.com/tartley/colorama
- pytest https://docs.pytest.org/en/6.2.x/g
- coverage https://coverage.readthedocs.io/en/6.2/
- pytest-xdist https://github.com/pytest-dev/pytest-xdist
- mypy http://mypy-lang.org/
- backpack (Collections) https://github.com/sdispater/backpack
- Pendulum
- QtAwesome https://github.com/spyder-ide/qtawesome
  https://fontawesome.com/v5.15/icons?d=gallery&m=free
  https://phosphoricons.com/
  https://remixicon.com/
  https://microsoft.github.io/vscode-codicons/dist/codicon.html
  https://pictogrammers.github.io/@mdi/font/6.5.95/

# Dev

https://docs.python-guide.org/writing/gotchas/#bytecode-pyc-files-everywhere

- python devtools https://github.com/samuelcolvin/python-devtools

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL

Well supported, but not part of the standard:
Fore: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
Back: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX

- faker https://faker.readthedocs.io/en/master/

## Environment setup

[* python -m pip install --upgrade pip - Upgrade PIP]

- pip install orator - ActiveRecord/ORM
- pip install -U pytest - Unit testing
- GUI framework

```bash
python -m venv env
source env/bin/activate
pip install pyside6
```

## Create Models

```bash

```

## Create Database

- Create migrations

```bash

```

- Migrate

```bash
orator migrate --config ./config/database.py --path ./databases/migrations/ -v
```

- Create seeders

```bash
orator make:seed --path ./databases/seeds/ job_application_table_seeder
orator make:seed --path ./databases/seeds/ job_table_seeder
orator make:seed --path ./databases/seeds/ company_table_seeder
orator make:seed --path ./databases/seeds/ profession_table_seeder
orator make:seed --path ./databases/seeds/ action_table_seeder
orator make:seed --path ./databases/seeds/ address_table_seeder
orator make:seed --path ./databases/seeds/ person_table_seeder
```

- Seed

```bash
# https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html
# export PYTHONPATH="$PWD/app/models:$PYTHONPATH"
# https://docs.python.org/3/tutorial/modules.html#packages
orator db:seed --config ./config/database.py --path ./databases/seeds -v
```

# Testing

```bash
python -m pytest
```

with coverage reports

```bash
coverage run -m pytest -s
coverage report
```

add `-n 4` to run multiple processes

- Profile tests

```bash
pytest --durations=10 --durations-min=1.0
```

# Typing

- Match statment - not supported and no way to ignore yet
  ** https://github.com/python/mypy/issues/11829
  ** https://github.com/python/mypy/pull/10191

