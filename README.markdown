# Twitter Bootstrap Skin for Django Admin 

I once had to code my own **Custom Responsible Skin for Django Admin**, so I did it with the Twitter Bootstrap framework. I hope you like and help me make it better.

## Screenshots

<img src="https://raw.github.com/douglasmiranda/django-admin-bootstrap/master/static/screenshot-github.jpg">

## Install
```
>>> pip install git+https://github.com/douglasmiranda/django-admin-bootstrap
```
**NOTE:** I'm assuming you use [pip](http://www.pip-installer.org/) to install the Python Packages.

And don't forget it to add *bootstrap_admin* in **INSTALLED_APPS** before the *django.contrib.admin*.

Example:
```python
INSTALLED_APPS = (
    # ...
    'bootstrap_admin',
    'django.contrib.admin',
    # ...
)
```

## Last but not least

Works with django>=1.4

Fork if you want to contribute, [open an issue](https://github.com/douglasmiranda/django-admin-bootstrap/issues/new) if you find a bug or want something more.