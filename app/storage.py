

import typing

from app.repositories.JobApplicationRepository import JobApplicationRepository


class Storage:
    jobApplications = JobApplicationRepository()
    jobApplications.loadAll()

    WINDOW_WIDTH: typing.Final = 1500
    WINDOW_HEIGHT: typing.Final = 800
