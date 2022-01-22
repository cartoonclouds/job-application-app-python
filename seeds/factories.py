
from orator.orm import Factory


from .models.job import Job
from .models.job_application import JobApplication
from .models.company import Company


factory = Factory()


@factory.define(JobApplication)
def job_applications_factory(faker):
    return {
        'requires_followup': faker.boolean(),
        'pinned': faker.boolean(),
        'job_id': faker.random_int(),
        'company_id': faker.random_int(),
    }


@factory.define(Job)
def job_factory(faker):
    return {
        'website': faker.url(),
        'comments': faker.paragraph(),
        'title': faker.job(),
        'closing_date': faker.future_datetime().isoformat(),
        'salary': faker.random_int(),
        'rate': faker.random_int(),
        'rate_unit': faker.random_element(elements=('minute', 'hour', 'day'))
    }


@factory.define(Company)
def company_factory(faker):
    return {
        'name': faker.company(),
        'email': faker.ascii_company_email(),
        'phone': faker.phone_number(),
        'website': faker.url(),
        'comments': faker.paragraph(),
    }
