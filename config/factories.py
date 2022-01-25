
from masoniteorm import Factory

from app.models.Job import Job
from app.models.Company import Company
from app.models.JobApplication import JobApplication
from app.models.Person import Person
from app.models.Profession import Profession
from app.models.Address import Address
from app.models.Action import Action


def profession_factory(faker):
    return {
        'profession': faker.job()
    }


Factory.register(Profession, profession_factory)


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


Factory.register(Address, address_factory)


def job_factory(faker):
    return {
        'website': faker.url(),
        'comments': faker.paragraph(),
        'title': faker.job(),
        'closing_date': faker.future_datetime().isoformat(),
        'salary': faker.random_int(),
        'rate': faker.random_int(),
        'rate_unit': faker.random_element(elements=('minute', 'hour', 'day')),
        'employment_type': faker.random_element(elements=("Full-time", "Part-time", "Casual", "Fixed Term", "Shiftworker", "Daily/Weekly Hire", "Probation", "Apprentice/Trainee", "Outworker")),
        'profession_id': Factory(Profession).create().id,
        'address_id': Factory(Address).create().id,
    }


Factory.register(Job, job_factory)


def person_factory(faker):
    return {
        'name': faker.name(),
        'title': faker.prefix(),
        'email': faker.email()
    }


Factory.register(Person, person_factory)


def company_factory(faker):
    return {
        'name': faker.company(),
        'email': faker.ascii_company_email(),
        'phone': faker.phone_number(),
        'website': faker.url(),
        'comments': faker.paragraph(),
        'address_id': Factory(Address).create().id,
        'person_id': Factory(Person).create().id,
    }


Factory.register(Company, company_factory)


def job_application_factory(faker):
    return {
        'title': faker.sentence(),
        'requires_followup': faker.boolean(),
        'pinned': faker.boolean(),
        'job_id': Factory(Job).create().id,
        'company_id': Factory(Company).create().id,
    }


Factory.register(JobApplication, job_application_factory)


def actions_factory(faker):
    actionable = Factory(Job).create()

    return {
        'title': faker.sentence(),
        'requires_followup': faker.boolean(),
        'pinned': faker.boolean(),
        'contact_method': faker.random_element(elements=("Phone call", "Received phone call", "E-mail", "Recruiter", "In-person", "Company website", "Employment website", "Letter", "Online forum")),
        'person_id': Factory(Person).create().id,
        # Can be either Action or Job
        'actionable_id': actionable.id,
        'actionable_type': actionable.__class__.__name__
    }


Factory.register(Action, actions_factory)
