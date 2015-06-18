Responsive Theme for Django Admin (Django 1.7+)
===============================================

.. image:: https://img.shields.io/pypi/dm/bootstrap_admin.svg
    :target: https://pypi.python.org/pypi/bootstrap_admin/
    :alt: Downloads

Ingredients
-----------

New design, templates from Django 1.7+, Bootstrap 3 and Coffee.

Screenshots
-----------

.. image:: https://raw.githubusercontent.com/django-admin-bootstrap/django-admin-bootstrap/master/screenshots/screenshot.png
    :target: https://github.com/django-admin-bootstrap/django-admin-bootstrap/tree/master/screenshots
    :alt: See Screenshots

`More screenshots <https://github.com/django-admin-bootstrap/django-admin-bootstrap/tree/master/screenshots>`_

INSTALL
-------

from pypi (recommended) ::

    $ pip install bootstrap-admin

from github master branch ::

    $ pip install git+https://github.com/django-admin-bootstrap/django-admin-bootstrap

or clone the master branch in your machine ::

    $ git clone https://github.com/django-admin-bootstrap/django-admin-bootstrap

And don't forget to add *bootstrap\_admin* in **INSTALLED\_APPS** before
the *django.contrib.admin*.

Example:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'bootstrap_admin', # always before django.contrib.admin
        'django.contrib.admin',      
        # ...   
    )

    # For Sidebar Menu in Django 1.7 only (List of apps and models) (RECOMMENDED)
    from django.conf import global_settings
    TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
    )
    BOOTSTRAP_ADMIN_SIDEBAR_MENU = True


Contributing
------------

1. Fork it!
2. Create your feature branch: ``git checkout -b my-new-feature``
3. Commit your changes: ``git commit -am 'Add some feature'``
4. Push to the branch: ``git push origin my-new-feature``
5. Submit a pull request =]

See the `full list <https://github.com/django-admin-bootstrap/django-admin-bootstrap/blob/master/AUTHORS.rst>`_ of contributors.

`Open an
issue <https://github.com/django-admin-bootstrap/django-admin-bootstrap/issues/new>`_
if you find a bug or want something more.

TODO
----

- Docs
- Improve Sidebar menu

If you want to install the old version, just install with pip.
(See the `old README <https://github.com/django-admin-bootstrap/django-admin-bootstrap/blob/master/README-old.rst>`_)
