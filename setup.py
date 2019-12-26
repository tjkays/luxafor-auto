from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='luxafor-auto',
    version='0.1.0',
    description='Luxafor auto management',
    long_description=readme,
    author='Tyler Kays',
    author_email='tylerkays@kntnetworks.com',
    url='https://github.com/tjkays',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
