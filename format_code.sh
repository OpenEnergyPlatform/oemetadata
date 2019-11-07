#!/usr/bin/env bash

isort -rc ./metadata/ ./tests/
black metadata/ tests/
