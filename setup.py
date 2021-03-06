from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='awuproject',
    version=version,
    description="ActWithUs: Django project",
    long_description="""\
    What does this project do?
    ==========================

    - Helps groups of volunteers take action toward a common goal.
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='ElevenCraft Inc.',
    author_email='actwithus@11craft.com',
    url='http://actwithus.com/',
    license='Apache 2.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'awucontacts',
        'awufundraiser',
        'Django >= 1.2.3, < 1.3',
        'psycopg2',
    ],
    entry_points="""
    """,
)
