import pkg_resources
from setuptools import setup, find_packages

"""
Use this script to create a installable library for Python:

$ python setup.py bdist_wheel

"""

README_FILE = "README.md"
REQUIREMENTS_FILE = "requirements.txt"

with open(README_FILE, 'r', encoding='utf-8') as f:
    long_description = f.read()

with open(REQUIREMENTS_FILE) as requirements:
    reqs = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements)
    ]

setup(
    name='cowskit',
    version='1.0.0',
    author='Krowcia Crew',
    license='MIT',
    description='QuantumAI library for fast model prototyping & testing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    install_requires=reqs,
    include_package_data=True,
    package_data={'': ['files/*.dataset']},
    python_requires='>=3.7',
)