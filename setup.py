import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-authorize',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to provide role based authentication for users.',
    long_description=README,
    url='https://github.com/hchockarprasad/django-authorize/',
    author='hchockarprasad',
    author_email='hchockarprasad@gmail.com',
    test_suite='runtests.run_tests',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ], install_requires=[
        'Django~=2.0',
        'djangorestframework~=3.7.0',
    ],
)
