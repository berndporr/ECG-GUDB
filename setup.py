#!/usr/bin/python3

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='ecg_gudb_database',
    version='1.1.1',
    description="API for a high precision ECG Database with annotated R peaks (GUDB)",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author='Bernd Porr',
    author_email='bernd.porr@glasgow.ac.uk',
    py_modules=['ecg_gudb_database'],
    install_requires=['numpy',
                      'scipy',
                      'requests'],
    zip_safe=False,
    url='https://github.com/berndporr/ECG-GUDB',
    license='GPL 3.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
