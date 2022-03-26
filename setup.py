# ///////////////////////////////////////////////////////////////
#
# BY: CHRIS TUDHOPE
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they
# maintain the respective credits.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# https://stackoverflow.com/questions/26804421/python-project-directory-structure-pytest-trouble
# https://github.com/Seanny123/derpland
# https://gist.github.com/nicoddemus/6abbc43236dd042fd053

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
# https://blog.ionelmc.ro/2014/05/25/python-packaging/

# https://tox.wiki/en/latest/
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
# https://packaging.python.org/en/latest/overview/
# https://github.com/pypa/sampleproject/blob/main/setup.py
setup(
    name="app",
    version="0.0.1",
    author="Chris Tudhope",
    author_email="cartoonclouds@gmail.com",
    description="Job Applications App",
    package_dir={"": "app"},
    packages=find_packages("app"),
    # install_requires=[ # https://pip.pypa.io/en/stable/reference/requirements-file-format/#requirements-file-format
    #     'PyYAML',
    #     'pandas==0.23.3',
    #     'numpy>=1.14.5',
    #     'matplotlib>=2.2.0,,
    #     'jupyter'
    # ]
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    python_requires=">=3.6",
)
