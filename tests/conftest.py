
""" The conftest.py file serves as a means of providing fixtures for an entire directory. """

import pytest
import time

from app.models.JobApplication import JobApplication
from app.models.Job import Job
from app.models.Person import Person
from app.models.Company import Company
from app.models.Profession import Profession
from app.models.Address import Address
from app.models.Action import Action


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

# @pytest.fixture(scope="module")
# def get_address():
#     """ Returns a function to find a Address with ID. If no ID is passed a random Address is returned. """
#     def _get_address(withHas=None, id=None):
#         if (id is None):
#             if (withHas is not None):
#                 return Address.has(withHas).with_(withHas).first()
#             else:
#                 return Address.first()
#         else:
#             return Address.find(id)

#     return _get_address
