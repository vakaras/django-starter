from distutils.core import setup

setup(
    name='$(name)',
    version='0.1',
    author='$(author)',
    author_email='$(author)@localhost',
    packages=['$(name)',],
    url='http://pypi.python.org/pypi/$(name)/',
    license='Commercial',
    description='$(name).',
    long_description=open('README.txt').read(),
)

