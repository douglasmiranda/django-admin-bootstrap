Responsive Django Admin
=======================

If you're looking for a version compatible with Django 1.8 just install **0.3.7.1**.

Features
--------

* Responsive
* Sidebar Menu
* Easy install / setup
* Support Django **1.11**, **2.1**, **2.2** and **3.0**
* Bootstrap 3
* Python 3


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

And don't forget to add **bootstrap\_admin** in ``INSTALLED_APPS`` before
the ``django.contrib.admin``.

Example:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'bootstrap_admin', # always before django.contrib.admin  
        'django.contrib.admin',
        # ...
    )  

CUSTOMIZE
---------

Sidebar Menu
^^^^^^^^^^^^

It is enabled by default. But if you remove ``django.template.context_processors.request`` from your ``context_processors``.

Just disable it:

.. code-block:: python

    BOOTSTRAP_ADMIN_SIDEBAR_MENU = False

Branding - Overriding logo
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to use your own logo, you can achieve this by overriding the **login.html** and **base_site.html**, just like in Django Admin.

First, make sure the ``TEMPLATES`` setting in your settings.py is properly configured:

.. code-block:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'my_django_project/templates')],
            'APP_DIRS': True,
            # other stuff
        },
    ]

`DIRS`: You must set the location of your templates, an absolute path.

I'm assuming ``BASE_DIR`` is:

.. code-block:: python

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

This pattern of creating a global templates folder could be useful for you to use for your **base.html** and other global templates.

More info: https://docs.djangoproject.com/en/2.1/ref/templates/api/#configuring-an-engine

Let me show you a project structure as an example:

.. code-block:: 

    ├── my_django_project
    │   ├── core
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── tests.py
    │   │   └── views.py
    │   ├── settings.py
    │   ├── templates
    │   │   └── admin
    │   │       ├── base_site.html
    │   │       └── login.html
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py

You can see I created a global **templates/** folder, 
with another directory inside **admin/** containing **login.html** and **base_site.html**.

Their respective contents are:

**base_site.html**

.. code-block:: html

    {% extends 'admin/base_site.html' %}
    {% load static %}

    {% block branding %}
        <a href="{% url 'admin:index' %}" class="django-admin-logo">
            <!-- Django Administration -->
            <img height="60" src="{% static "bootstrap_admin/img/logo-140x60.png" %}" alt="{{ site_header|default:_('Django administration') }}">
        </a>
    {% endblock branding %}


**login.html**

.. code-block:: html

    {% extends 'admin/login.html' %}
    {% load i18n static %}

    {% block branding %}
        <a href="{% url 'admin:index' %}" class="django-admin-logo">
            <!-- Django Administration -->
            <img height="60" src="{% static "bootstrap_admin/img/logo-140x60.png" %}" alt="{{ site_header|default:_('Django administration') }}">
        </a>
    {% endblock branding %}

More info: https://docs.djangoproject.com/en/2.1/ref/contrib/admin/#admin-overriding-templates

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
