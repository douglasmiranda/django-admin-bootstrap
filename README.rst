Responsive Django Admin With Sidebar Menu (Django 1.11)
=======================================================

If you're looking for a version compatible with Django 1.8 just install **0.3.7.1**.

Screenshots
-----------

.. image:: https://raw.githubusercontent.com/douglasmiranda/django-admin-bootstrap/master/screenshots/screenshot.png
    :target: https://github.com/douglasmiranda/django-admin-bootstrap/tree/master/screenshots
    :alt: See Screenshots

`More screenshots <https://github.com/douglasmiranda/django-admin-bootstrap/tree/master/screenshots>`_

INSTALL
-------

from pypi (recommended) ::

    $ pip install bootstrap-admin

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

**Sidebar Menu**

It is enabled by default. But if you remove `django.template.context_processors.request` from your `context_processors`.

Just disable it:

.. code-block:: python

    BOOTSTRAP_ADMIN_SIDEBAR_MENU = False


Contributing
------------

1. Fork it!
2. Create your feature branch: ``git checkout -b my-new-feature``
3. Commit your changes: ``git commit -am 'Add some feature'``
4. Push to the branch: ``git push origin my-new-feature``
5. Submit a pull request =]

See the `full list <https://github.com/douglasmiranda/django-admin-bootstrap/blob/master/AUTHORS.rst>`_ of contributors.

`Open an issue <https://github.com/douglasmiranda/django-admin-bootstrap/issues/new>`_
if you find a bug or want something more.
