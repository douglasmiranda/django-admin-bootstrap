Responsible Skin for Django Admin
=================================

django-admin-bootstrap is a **Custom Responsible Skin for Django Admin
1.5.\***. I hope you like and help me make it better.

.. image:: https://pypip.in/d/bootstrap_admin/badge.png
    :target: https://crate.io/packages/bootstrap_admin/

Screenshots
-----------

.. image:: https://raw.github.com/douglasmiranda/django-admin-bootstrap/master/static/screenshot-github.jpg

PS: the wysiwyg editor you see on the screenshot is the `django-wysiwyg-redactor <https://github.com/douglasmiranda/django-wysiwyg-redactor>`_

Features (beyond what you already know)
---------------------------------------

-  a bit of responsiveness
-  search directly from the apps list
-  sidebar logs for specific app (on app index)

Install
-------

**NOTE:** I'm assuming you use `pip <http://www.pip-installer.org/>`_ to
install the Python Packages.

from latest version on pypi (fully compatible with django1.5) ::

    $ pip install bootstrap-admin

from github master branch ::

    $ pip install git+https://github.com/douglasmiranda/django-admin-bootstrap

or clone the master branch in your machine ::

    $ git clone https://github.com/douglasmiranda/django-admin-bootstrap

And don't forget to add *bootstrap\_admin* in **INSTALLED\_APPS** before
the *django.contrib.admin*.

Example: :: 

   INSTALLED_APPS = (     
       # ...       
       'bootstrap_admin',       
       'django.contrib.admin',      
       # ...   
    )

Contributing
------------

1. Fork it!
2. Create your feature branch: ``git checkout -b my-new-feature``
3. Commit your changes: ``git commit -am 'Add some feature'``
4. Push to the branch: ``git push origin my-new-feature``
5. Submit a pull request =]

`Open an
issue <https://github.com/douglasmiranda/django-admin-bootstrap/issues/new>`_
if you find a bug or want something more.

History
-------
-  0.2.8 Nov 07, 2013

   -   Fix: Forgot to add README.rst on MANIFEST.in (shame on me)

-  0.2.7 Nov 07, 2013

   -   Fix: bug when retrieving message.tags ( pull #32 )

-  0.2.6 Nov 05, 2013

   -   django-mptt templates ( pull #30 )

-  0.2.5 Oct 14, 2013

   -  Enhancement: Separate field template to allow easy customizations.
      ( pull #26 )

-  0.2.4 Oct 13, 2013

   -  Fix: Do not add span8 class to inputs of CheckboxSelectMultiple. (
      pull #24 )

-  0.2.3 Oct 7, 2013

   -  Fix: Style for errors list on tabular inline.
   -  Fix: issue #22

-  0.2.2 Aug 11, 2013

   -  Fix: "shaking" effect that nav-bar causes when is affixed on top.
   -  Fix: search input width (responsive)
   -  Fix: adding overflow ellipsis on the form search input
   -  Fix: margin for "add-another" option

-  0.2.1 May 23, 2013

   -  Fix: the issue #17 (about the MANIFEST.in)

-  0.2.0 May 14, 2013

   -  Final touches
   -  Show the search input properly considering the permissions
   -  Fix: z-index nav-bar bug

-  early versions

   -  Have some little bugs, it is usable, but I recommend the latest
      version


