
import collections
from app.models.JobApplication import JobApplication

# https://docs.python.org/3/library/collections.html#collections.UserDict
# https://stackoverflow.com/questions/7148419/subclass-dict-userdict-dict-or-abc
# https://stackoverflow.com/questions/61112684/how-to-subclass-a-dictionary-so-it-supports-generic-type-hints


class JobApplicationRepository(collections.UserDict):
    def __init__(self, d: dict[str | int, JobApplication]):
        super().__init__(d)

    def printList(self):
        print('\n'.join(map(str, self.values())))
