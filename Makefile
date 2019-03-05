
#
# JEA :: SANDBOX
# --------------
#
# Makefile for project tasks
#

containers_build:
	./bin/docker-compose build

containers:
	./bin/docker-compose up

clean:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

