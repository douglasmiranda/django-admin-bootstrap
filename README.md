# Twitter Bootstrap Skin for Django Admin 

I once had to code my own **Custom Responsible Skin for Django Admin**, so I did it with the Twitter Bootstrap framework. I hope you like and help me make it better.

## Screenshots

<img src="https://raw.github.com/douglasmiranda/django-admin-bootstrap/master/static/screenshot-github.jpg">

## Features (beyond what you already know)

* a bit of responsiveness
* search directly from the apps list
* sidebar logs for specific app (on app index)

## Install

from latest version on pypi (fully compatible with django1.5)
```
>>> pip install bootstrap-admin
```

from github master branch
```
>>> pip install git+https://github.com/douglasmiranda/django-admin-bootstrap
```

or clone the master branch in your machine
```
>>> git clone https://github.com/douglasmiranda/django-admin-bootstrap
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

If you using Django >=1.4.* and <1.5

```
>>> pip install bootstrap-admin==0.1.5
```
**NOTE:** bootstrap-admin==0.1.5 is not so much stable, so the recommended use is with django >=1.5.* and bootstrap-admin>=0.2.*

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request =]

[Open an issue](https://github.com/douglasmiranda/django-admin-bootstrap/issues/new) if you find a bug or want something more.