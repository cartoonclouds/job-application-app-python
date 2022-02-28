
import typing
from orator.orm import Factory

from app.models.Job import Job
from app.models.Company import Company
from app.models.JobApplication import JobApplication
from app.models.Person import Person
from app.models.Profession import Profession
from app.models.Address import Address
from app.models.Action import Action

factory = Factory()

EMPLOYMENT_TYPES = ("Full-time", "Part-time", "Casual", "Fixed Term",
                    "Shiftworker", "Daily/Weekly Hire", "Probation", "Apprentice/Trainee", "Outworker")
CONTACT_METHODS = ("Phone call", "Received phone call", "E-mail", "Recruiter",
                   "In-person", "Company website", "Employment website", "Letter", "Online forum")
RATE_UNITS = ('minute', 'hour', 'day')


@factory.define(Profession)
def profession_factory(faker) -> dict[str, typing.Any]:
    return {
        'profession': faker.job()
    }


@factory.define(Address)
def address_factory(faker) -> dict[str, typing.Any]:
    return {
        'address_line_1': faker.street_address(),
        #    'address_line_2': faker,
        'suburb': faker.city(),
        'city': faker.city(),
        'state': faker.city(),
        'postcode': faker.postcode(),
        'country': faker.country(),
    }


@factory.define(Person)
def person_factory(faker) -> dict[str, typing.Any]:
    return {
        'name': faker.name(),
        'title': faker.prefix(),
        'email': faker.email()
    }


@factory.define(Company)
def company_factory(faker) -> dict[str, typing.Any]:
    return {
        'name': faker.company(),
        'email': faker.ascii_company_email(),
        'phone': faker.phone_number(),
        'website': faker.url(),
        'comments': faker.paragraph(),
        'address_id': factory(Address).create().id,
        'person_id': factory(Person).create().id,
    }


@factory.define(JobApplication)
def job_application_factory(faker) -> dict[str, typing.Any]:
    return {
        'title': faker.sentence(),
        'requires_followup': faker.boolean(),
        'pinned': faker.boolean(),
        'company_id': factory(Company).create().id,
    }


@factory.define(Job)
def job_factory(faker) -> dict[str, typing.Any]:
    return {
        'website': faker.url(),
        'comments': faker.paragraph(),
        'title': faker.job(),
        'closing_date': faker.future_datetime().isoformat(),
        'salary': faker.random_int(),
        'rate': faker.random_int(),
        'rate_unit': faker.random_element(elements=RATE_UNITS),
        'employment_type': faker.random_element(elements=EMPLOYMENT_TYPES),
        'profession_id': factory(Profession).create().id,
        'address_id': factory(Address).create().id,
        'job_application_id': factory(JobApplication).create().id,
    }


@factory.define(Action)
def actions_factory(faker) -> dict[str, typing.Any]:
    # actionableModel = faker.random_element(elements=(Job, Action))
    # actionable = factory(actionableModel).create()

    return {
        'title': faker.sentence(),
        'requires_followup': faker.boolean(),
        'pinned': faker.boolean(),
        'contact_method': faker.random_element(elements=CONTACT_METHODS),
        'person_id': factory(Person).create().id,
        # Can be either Action or Job
        # 'actionable_id': actionable.get_key(),
        # 'actionable_type': actionable.get_table()
    }
