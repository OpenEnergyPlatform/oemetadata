#!/usr/bin/env bash

isort -rc ./oemetadata/ ./tests/
black *.py oemetadata/ tests/
