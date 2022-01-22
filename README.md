# job-application-app-python

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
orator make:model JobApplication -m
orator make:model Job -m
orator make:model Company -m
orator make:model Profession -m
orator make:model EmploymentType -m
orator make:model Action -m
orator make:model Address -m
orator make:model Person -m
```

## Create Database

- Update migrations

- Migrate

```bash
orator migrate -c ./config/database.py
```

- Create seeders

```bash
orator make:seed job_applications_table_seeder
orator make:seed jobs_table_seeder
orator make:seed companies_table_seeder
orator make:seed professions_table_seeder
orator make:seed employment_types_table_seeder
orator make:seed actions_table_seeder
orator make:seed addresses_table_seeder
orator make:seed people_table_seeder
```

- Seed

```bash
orator db:seed -c ./config/database.py  -p ./
```
