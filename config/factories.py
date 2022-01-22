
from markupsafe import re
from masoniteorm import Factory

from app.models.Job import Job
from app.models.Company import Company
from app.models.JobApplication import JobApplication
from app.models.Person import Person
from app.models.Profession import Profession
from app.models.Address import Address


def job_application_factory(faker):
    return {
        'title': faker.sentence(),
        'requires_followup': faker.boolean(),
        'pinned': faker.boolean(),
        'job_id': faker.random_int(),
        'company_id': faker.random_int(),
    }


def job_factory(faker):
    return {
        'website': faker.url(),
        'comments': faker.paragraph(),
        'title': faker.job(),
        'closing_date': faker.future_datetime().isoformat(),
        'salary': faker.random_int(),
        'rate': faker.random_int(),
        'rate_unit': faker.random_element(elements=('minute', 'hour', 'day')),
        'employment_type': faker.random_element(elements=("Full-time", "Part-time", "Casual", "Fixed Term", "Shiftworker", "Daily/Weekly Hire", "Probation", "Apprentice/Trainee", "Outworker"))
    }


def company_factory(faker):
    return {
        'name': faker.company(),
        'email': faker.ascii_company_email(),
        'phone': faker.phone_number(),
        'website': faker.url(),
        'comments': faker.paragraph(),
        'address_id': faker.random_int(),
        'person_id': faker.random_int(),
    }


def profession_factory(faker):
    return {
        'profession': faker.job()
    }


def address_factory(faker):
    return {
        'address_line_1': faker.street_address(),
        #    'address_line_2': faker,
        'suburb': faker.city(),
        'city': faker.city(),
        'state': faker.city(),
        'postcode': faker.postcode(),
        'country': faker.country(),
    }


def person_factory(faker):
    return {
        'name': faker.name(),
        'title': faker.prefix(),
        'email': faker.email()
    }


Factory.register(JobApplication, job_application_factory)
Factory.register(Job, job_factory)
Factory.register(Company, company_factory)
Factory.register(Profession, profession_factory)
Factory.register(Address, address_factory)
Factory.register(Person, person_factory)
