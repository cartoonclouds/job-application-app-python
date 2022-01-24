# job-application-app-python

## Packages

- masoniteorm https://orm.masoniteproject.com/
- colorama https://github.com/tartley/colorama
- pytest https://docs.pytest.org/en/6.2.x/g
- coverage https://coverage.readthedocs.io/en/6.2/
- pytest-xdist https://github.com/pytest-dev/pytest-xdist

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
masonite-orm model JobApplication
masonite-orm model Job
masonite-orm model Company
masonite-orm model Profession
masonite-orm model EmploymentType
masonite-orm model Action
masonite-orm model Address
masonite-orm model Person
```

## Create Database

- Create migrations

```bash
masonite-orm migration create_job_applications_table --create job_applications
...
...
```

- Migrate

```bash
masonite-orm migrate
```

- Create seeders

```bash
masonite-orm seed JobApplication
masonite-orm seed Job
masonite-orm seed Company
masonite-orm seed Profession
masonite-orm seed EmploymentType
masonite-orm seed Action
masonite-orm seed Address
masonite-orm seed Person
```

- Seed

```bash
masonite-orm seed:run Seeder
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
