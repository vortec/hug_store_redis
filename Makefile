.PHONY: test unit style style-verbose clean

test:
	tox

unit:
	py.test -v --cov-report term-missing --cov hug_store_redis tests

style:
	flake8 --show-source hug_store_redis
	flake8 --show-source --ignore=F811,F821 tests

style-verbose:
	flake8 -v --show-source hug_store_redis
	flake8 -v --show-source --ignore=F811,F821 tests


clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find hug_store_redis -name "__pycache__" | xargs rm -rf
	find tests -name "__pycache__" | xargs rm -rf
	rm -f coverage.xml
	rm -rf *.egg-info
	rm -rf .cache/
	rm -rf .eggs/
	rm -rf .tox/
	rm -rf build/
	rm -rf docs/build/
	rm -rf dist/
	rm -rf junit/
