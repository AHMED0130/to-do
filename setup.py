from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='to-do',
    version='3.0',
    author='ahmed elshnawy',
    description='to do application to manage every day tasks in an effective way',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
)


