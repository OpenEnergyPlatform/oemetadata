#!/usr/bin/env bash

isort -rc ./metadata/ ./tests/
black *.py metadata/ tests/
