# job-application-app-python

## Packages

- orator https://orator-orm.com/
- colorama https://github.com/tartley/colorama
- pytest https://docs.pytest.org/en/6.2.x/g
- coverage https://coverage.readthedocs.io/en/6.2/
- pytest-xdist https://github.com/pytest-dev/pytest-xdist
- mypy http://mypy-lang.org/

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
orator migrate --config ./config/database.py --path ./databases/migrations/
```

- Create seeders

```bash
orator make:seed job_application_table_seeder
orator make:seed job_table_seeder
orator make:seed company_table_seeder
orator make:seed profession_table_seeder
orator make:seed action_table_seeder
orator make:seed address_table_seeder
orator make:seed person_table_seeder
```

- Seed

```bash
# https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html
# export PYTHONPATH="$PWD/app/models:$PYTHONPATH"
orator db:seed --config ./config/database.py
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

https://github.com/pytest-dev/pytest-reportlog

        with capsys.disabled():
            print('))))))))))))))))' + address.id)

print(\*a, sep = "\n")

print str(a)[1:-1]

print(' '.join(map(str, a)))

print"in new line"
print('\n'.join(map(str, a)))
