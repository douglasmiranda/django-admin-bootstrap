clean:
	@find . -name "*.pyc" -delete
	@rm -R dist/

release:
	@sed -ic -e s/`cat VERSION`/$(version)/ setup.py bootstrap_admin/__init__.py
	@echo $(version) > VERSION
	@git add setup.py VERSION bootstrap_admin/__init__.py
	@git commit -m "setup: bump to $(version)"
	@git tag $(version)
	@git push --tags
	@git push origin master
	@make clean
	@python setup.py sdist bdist_wheel
	@twine upload dist/*