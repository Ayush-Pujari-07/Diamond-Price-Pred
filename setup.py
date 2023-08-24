from setuptools import (
    find_packages,
    setup,
)  # Import necessary functions from setuptools module
from typing import List

HYPEN_E_DOT = "-e ."  # Define a constant variable


def get_requirements(file_path: str) -> List[str]:
    """
    This function retrieves the requirements from a file and returns them as a list.
    """
    requirements = []  # Initialize an empty list to store requirements
    with open(file_path) as file_obj:  # Open the specified file
        requirements = file_obj.readlines()  # Read all lines from the file
        requirements = [
            req.replace("\n", "") for req in requirements
        ]  # Remove newline characters

        if HYPEN_E_DOT in requirements:  # Check if '-e .' is present in requirements
            requirements.remove(HYPEN_E_DOT)  # Remove '-e .' from the list
    return requirements  # Return the list of requirements


setup(
    name='Diamond_predectionProject',
    version='0.0.1',
    author='Ayush Pujari',
    author_email='ayush08.pujari@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
