clean:
    @find . -name "*.pyc" -delete

release:
    @make clean
    @sed -ic -e s/`cat VERSION`/$(version)/ bootstrap_admin/__init__.py
    @echo $(version) > VERSION
    @git add setup.py VERSION bootstrap_admin/__init__.py
    @git commit -m "setup: bump to $(version)"
    @git tag $(version)
    @git push --tags
    @git push origin master
    @python setup.py sdist upload