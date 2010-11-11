from setuptools import setup, find_packages

setup(
    name = '$(name)',
    version = '0.1',
    author = '$(author)',
    author_email = '$(author)@localhost',
    packages = find_packages(),
    namespace_packages = [],
    install_requires = [],
    url = 'http://pypi.python.org/pypi/$(name)/',
    license = 'Commercial',
    description = '$(name).',
    long_description = open('README.txt').read(),
)

