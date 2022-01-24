
""" The conftest.py file serves as a means of providing fixtures for an entire directory. """

import pytest
import time

from app.models.JobApplication import JobApplication
from app.models.Job import Job
from app.models.Person import Person
from app.models.Company import Company
from app.models.Profession import Profession
from app.models.Address import Address


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


@pytest.fixture(scope="module")
def get_job_application():
    """ Returns a function to find a JobApplication with ID. If no ID is passed a random JobApplication is returned. """
    def _get_job_application(id=None):
        if (id is None):
            return JobApplication.get().random()
        else:
            return JobApplication.find(id)

    return _get_job_application


@pytest.fixture(scope="module")
def get_job():
    """ Returns a function to find a Job with ID. If no ID is passed a random Job is returned. """
    def _get_job(id=None):
        if (id is None):
            return Job.get().random()
        else:
            return Job.find(id)

    return _get_job


@pytest.fixture(scope="module")
def get_person():
    """ Returns a function to find a Person with ID. If no ID is passed a random Person is returned. """
    def _get_person(id=None):
        if (id is None):
            return Person.get().random()
        else:
            return Person.find(id)

    return _get_person


@pytest.fixture(scope="module")
def get_company():
    """ Returns a function to find a Company with ID. If no ID is passed a random Company is returned. """
    def _get_company(withHas=None, id=None):
        if (id is None):
            if (withHas is not None):
                return Company.hasWith(withHas).get().random()
            else:
                return Company.get().random()
        else:
            return Company.find(id)

    return _get_company


@pytest.fixture(scope="module")
def get_profession():
    """ Returns a function to find a Profession with ID. If no ID is passed a random Profession is returned. """
    def _get_profession(id=None):
        if (id is None):
            return Profession.get().random()
        else:
            return Profession.find(id)

    return _get_profession


@pytest.fixture(scope="module")
def get_address():
    """ Returns a function to find a Address with ID. If no ID is passed a random Address is returned. """
    def _get_address(withHas=None, id=None):
        if (id is None):
            if (withHas is not None):
                return Address.hasWith(withHas).get().random()
            else:
                return Address.get().random()
        else:
            return Address.find(id)

    return _get_address
