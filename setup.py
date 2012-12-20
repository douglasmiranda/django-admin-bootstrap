#!/usr/bin/env python
from setuptools import setup, find_packages


template_dirs = [
    'templates/admin/auth/user/*.html',
    'templates/admin/edit_inline/*.html',
    'templates/admin/includes/*.html',
    'templates/admin/*.html',
    'templates/registration/*.html',
    'static/admin/css/*.css',
    'static/admin/js/*.js',
    'static/admin/js/admin/*.js',
    'static/admin/img/*.png',
    'templatetags/*',
]

setup(
    name='bootstrap_admin',
    version='0.1',
    description='Responsive Templates para o Django Admin, customizados com Twitter Bootstrap.',
    author='Douglas Miranda',
    author_email='douglasmirandasilva@gmail.com',
    url='https://github.com/douglasmiranda/django-admin-bootstrap',
    packages=find_packages(),
    package_data={'bootstrap_admin': template_dirs},
    license='GPL',
    include_package_data=True,
    zip_safe=False,
)
