
""" The conftest.py file serves as a means of providing fixtures for an entire directory. """

import pytest
import time

from app.models import JobApplication, Job, Person, Company, Profession, Address


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
        Collect test results
    """
    terminalreporter.section("Final Results")

    # print(terminalreporter.stats)
    #  TerminalReporter._sessionStartTime session start time
    duration = time.time() - terminalreporter._sessionstarttime

    table_data = [
        ["Statistics", ""],
        ['Total', terminalreporter._numcollected],
        ['Passed', len(terminalreporter.stats.get('passed', []))],
        ['Failed', len(terminalreporter.stats.get('failed', []))],
        ['Error', len(terminalreporter.stats.get('error', []))],
        ['Skipped', len(terminalreporter.stats.get('skipped', []))],
        ['Total Times', str(duration) + " secs"],
    ]

    for row in table_data:
        print("{: >14}   {: <10}".format(*row))

    terminalreporter.currentfspath = 1
    terminalreporter.ensure_newline()


# Global Fixtures

""" Returns a function to find a JobApplication with ID. If no ID is passed a random JobApplication is returned. """


@pytest.fixture(scope="module")
def get_job_application():
    def _get_job_application(id=None):
        if (id is None):
            return JobApplication.all().random()
        else:
            return JobApplication.find(id)

    return _get_job_application


""" Returns a function to find a Job with ID. If no ID is passed a random Job is returned. """


@pytest.fixture(scope="module")
def get_job():
    def _get_job(id=None):
        if (id is None):
            return Job.all().random()
        else:
            return Job.find(id)

    return _get_job


""" Returns a function to find a Person with ID. If no ID is passed a random Person is returned. """


@pytest.fixture(scope="module")
def get_person():
    def _get_person(id=None):
        if (id is None):
            return Person.all().random()
        else:
            return Person.find(id)

    return _get_person


""" Returns a function to find a Company with ID. If no ID is passed a random Company is returned. """


@pytest.fixture(scope="module")
def get_company():
    def _get_company(id=None):
        if (id is None):
            return Company.all().random()
        else:
            return Company.find(id)

    return _get_company


""" Returns a function to find a Profession with ID. If no ID is passed a random Profession is returned. """


@pytest.fixture(scope="module")
def get_profession():
    def _get_profession(id=None):
        if (id is None):
            return Profession.all().random()
        else:
            return Profession.find(id)

    return _get_profession


""" Returns a function to find a Address with ID. If no ID is passed a random Address is returned. """


@pytest.fixture(scope="module")
def get_address():
    def _get_address(id=None):
        if (id is None):
            return Address.with_('companies').with_('jobs').all().random()
        else:
            return Address.find(id)

    return _get_address
