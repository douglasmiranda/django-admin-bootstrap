WARNING
=======

I'm working on a new interface for django-admin-bootstrap. Click on the image below so you take a look. =]

If you want to install this new version, (which is under development), install from master branch (See section INSTALL below) and give me a feedback.

If you want to install the old (and current) version, just install with pip.
(See the `old README <https://github.com/douglasmiranda/django-admin-bootstrap/blob/master/README-old.rst>`_)

Screenshots
-----------

.. image:: https://raw.githubusercontent.com/douglasmiranda/django-admin-bootstrap/master/screenshots/screenshot.png
    :target: https://github.com/douglasmiranda/django-admin-bootstrap/tree/master/screenshots
    :alt: See Screenshots

`More screenshots <https://github.com/douglasmiranda/django-admin-bootstrap/tree/master/screenshots>`_

What's new (for now)
--------------------

-  Completely new interface
-  Django 1.7 (only and higher)
-  Bootstrap 3
-  Sidebar menu with apps (and filters on change_list)


INSTALL: Please help-me test the master branch
----------------------------------------------

from github master branch ::

    $ pip install git+https://github.com/douglasmiranda/django-admin-bootstrap

or clone the master branch in your machine ::

    $ git clone https://github.com/douglasmiranda/django-admin-bootstrap

And don't forget to add *bootstrap\_admin* in **INSTALLED\_APPS** before
the *django.contrib.admin*.

Example:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'bootstrap_admin', # always before 
        'django.contrib.admin',      
        # ...   
    )

    # For Sidebar Menu (List of apps and models)
    from django.conf import global_settings
    TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
    )
    BOOTSTRAP_ADMIN_SIDEBAR_MENU = True
