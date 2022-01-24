
# https://stackoverflow.com/questions/26804421/python-project-directory-structure-pytest-trouble
# https://github.com/Seanny123/derpland
# https://gist.github.com/nicoddemus/6abbc43236dd042fd053

from setuptools import setup, find_packages

# https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
# https://blog.ionelmc.ro/2014/05/25/python-packaging/

# https://tox.wiki/en/latest/
setup(
    name="app",
    version='0.0.1',
    packages=find_packages('app'),
    package_dir={'': 'app'},
    description="Job Applications App",
    author="Chris Tudhope",
    author_email="cartoonclouds@gmail.com",
    # install_requires=[ # https://pip.pypa.io/en/stable/reference/requirements-file-format/#requirements-file-format
    #     'PyYAML',
    #     'pandas==0.23.3',
    #     'numpy>=1.14.5',
    #     'matplotlib>=2.2.0,,
    #     'jupyter'
    # ]
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
