# Twitter Bootstrap Skin for Django Admin 

django-admin-bootstrap is a __Custom Responsible Skin for Django Admin 1.5.*__. I hope you like and help me make it better.

<a href="https://crate.io/packages/bootstrap_admin/"><img src="https://pypip.in/d/bootstrap_admin/badge.png"></a>

## Screenshots

<img src="https://raw.github.com/douglasmiranda/django-admin-bootstrap/master/static/screenshot-github.jpg">
PS: the wysiwyg editor you see on the screenshot is the [django-wysiwyg-redactor](https://github.com/douglasmiranda/django-wysiwyg-redactor)

## Features (beyond what you already know)

* a bit of responsiveness
* search directly from the apps list
* sidebar logs for specific app (on app index)

## Install

from latest version on pypi (fully compatible with django1.5)
```shell
$ pip install bootstrap-admin
```

from github master branch
```shell
$ pip install git+https://github.com/douglasmiranda/django-admin-bootstrap
```

or clone the master branch in your machine
```shell
$ git clone https://github.com/douglasmiranda/django-admin-bootstrap
```
**NOTE:** I'm assuming you use [pip](http://www.pip-installer.org/) to install the Python Packages.

And don't forget to add *bootstrap_admin* in **INSTALLED_APPS** before the *django.contrib.admin*.

Example:
```python
INSTALLED_APPS = (
    # ...
    'bootstrap_admin',
    'django.contrib.admin',
    # ...
)
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request =]

[Open an issue](https://github.com/douglasmiranda/django-admin-bootstrap/issues/new) if you find a bug or want something more.

## History

* 0.2.1 May 23, 2013
    * Fix: the issue #17 (about the MANIFEST.in)
* 0.2.0 May 14, 2013
    * Final touches
    * Show the search input properly considering the permissions
    * Fix: z-index nav-bar bug
* early versions
    * Have some little bugs, it is usable, but I recommend the latest version
