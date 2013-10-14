#!/usr/bin/env python
import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='bootstrap_admin',
    version='0.2.5',
    description='Twitter Bootstrap Responsive Skin for Django Admin.',
    long_description=readme,
    author='Douglas Miranda',
    author_email='douglasmirandasilva@gmail.com',
    url='https://github.com/douglasmiranda/django-admin-bootstrap',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='django,admin,skin,theme',
)
