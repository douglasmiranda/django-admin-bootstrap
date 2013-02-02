#!/usr/bin/env python
import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.markdown'))
readme = f.read()
f.close()

setup(
    name='bootstrap_admin',
    version='0.1.4',
    description='Twitter Bootstrap Responsive Skin for Django Admin.',
    long_description=readme,
    author='Douglas Miranda',
    author_email='douglasmirandasilva@gmail.com',
    url='https://github.com/douglasmiranda/django-admin-bootstrap',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
